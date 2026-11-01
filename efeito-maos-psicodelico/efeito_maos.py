"""Efeito "moldura de mãos psicodélica" (recriação do projeto TouchDesigner do vídeo).

As duas mãos formam um retângulo com polegar + indicador. Dentro dele aparece a
própria imagem da câmera, com cores psicodélicas e deformada em perspectiva
para acompanhar os dedos.

Uso:
    python efeito_maos.py                      # webcam 0
    python efeito_maos.py --source video.mp4   # arquivo de vídeo
    python efeito_maos.py --source video.mp4 --output saida.mp4 --no-window

Teclas: q/ESC sair | e trocar efeito | m espelhar | d mostrar pontos das mãos
"""
import argparse
import os
import sys
import time
import urllib.request

import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks.python import BaseOptions, vision

MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/hand_landmarker/"
             "hand_landmarker/float16/1/hand_landmarker.task")
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hand_landmarker.task")

THUMB_TIP, INDEX_TIP = 4, 8
EFFECTS = ["psicodelico", "solarizado", "neon"]


def ensure_model(path):
    if not os.path.exists(path):
        print("Baixando modelo de mãos do MediaPipe (~8 MB)...")
        urllib.request.urlretrieve(MODEL_URL, path)
    return path


# ---------------------------------------------------------------- efeitos ---
def efeito_psicodelico(frame, t):
    """Hue girando + canais trocados + solarização + leve ondulação."""
    h, w = frame.shape[:2]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv[..., 0] = (hsv[..., 0].astype(np.int32) + int(t * 60)) % 180
    hsv[..., 1] = 255
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    inv = np.where(frame > 128, 255 - frame, frame)  # solarize
    img = cv2.addWeighted(img, 0.65, inv[..., ::-1], 0.35, 0)
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    mapx = xs + 6 * np.sin(ys / 25 + t * 3)
    mapy = ys + 6 * np.cos(xs / 25 + t * 3)
    return cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)


def efeito_solarizado(frame, t):
    lut = np.array([i if i < 128 else 255 - i for i in range(256)], np.uint8) * 2
    img = cv2.LUT(frame, lut.astype(np.uint8))
    img = img[..., ::-1] if int(t * 2) % 2 else img
    return cv2.applyColorMap(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.COLORMAP_RAINBOW)


def efeito_neon(frame, t):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 60, 140)
    edges = cv2.dilate(edges, np.ones((2, 2), np.uint8))
    hsv = np.zeros_like(frame)
    hsv[..., 0] = (gray // 2 + int(t * 40)) % 180
    hsv[..., 1] = 255
    hsv[..., 2] = np.clip(edges.astype(np.int32) + gray // 3, 0, 255)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


FUNCS = {"psicodelico": efeito_psicodelico, "solarizado": efeito_solarizado, "neon": efeito_neon}


# ------------------------------------------------------------------ mãos ----
def quad_from_hands(landmarks_list, w, h):
    """Devolve 4 cantos (TL, TR, BR, BL) ou None.

    Cada mão contribui com polegar e indicador; a mão mais à esquerda da tela
    fica com os cantos da esquerda.
    """
    if len(landmarks_list) < 2:
        return None
    hands = []
    for lm in landmarks_list[:2]:
        pts = [np.array([lm[i].x * w, lm[i].y * h], np.float32) for i in (THUMB_TIP, INDEX_TIP)]
        pts.sort(key=lambda p: p[1])  # [cima, baixo]
        hands.append(pts)
    hands.sort(key=lambda p: p[0][0] + p[1][0])
    (ltl, lbl), (rtr, rbr) = hands
    return np.array([ltl, rtr, rbr, lbl], np.float32)


def convex_ok(quad, w, h):
    area = cv2.contourArea(quad)
    return area > 0.003 * w * h and cv2.isContourConvex(quad.astype(np.int32))


def draw_hands(img, landmarks_list):
    h, w = img.shape[:2]
    for lm in landmarks_list:
        for i in (THUMB_TIP, INDEX_TIP):
            cv2.circle(img, (int(lm[i].x * w), int(lm[i].y * h)), 7, (0, 255, 255), -1)


# ------------------------------------------------------------------ main ----
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", default="0", help="índice da câmera ou caminho de vídeo")
    ap.add_argument("--output", help="grava o resultado neste arquivo .mp4")
    ap.add_argument("--no-window", action="store_true", help="não abre janela (útil com --output)")
    ap.add_argument("--no-mirror", action="store_true", help="não espelhar a imagem")
    ap.add_argument("--model", default=MODEL_PATH)
    ap.add_argument("--smooth", type=float, default=0.5, help="suavização 0..0.95 dos cantos")
    args = ap.parse_args()

    src = int(args.source) if args.source.isdigit() else args.source
    cap = cv2.VideoCapture(src)
    if not cap.isOpened():
        sys.exit(f"Não foi possível abrir a fonte: {args.source}")

    options = vision.HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=ensure_model(args.model)),
        running_mode=vision.RunningMode.VIDEO, num_hands=2,
        min_hand_detection_confidence=0.5, min_tracking_confidence=0.5)
    landmarker = vision.HandLandmarker.create_from_options(options)

    writer = None
    mirror = not args.no_mirror
    show_dbg = False
    fx = 0
    quad_s = None
    lost = 0
    t0 = time.time()
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    last_ts = -1

    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if mirror:
            frame = cv2.flip(frame, 1)
        h, w = frame.shape[:2]
        t = time.time() - t0

        ts = int(cap.get(cv2.CAP_PROP_POS_MSEC)) if isinstance(src, str) else int(t * 1000)
        ts = max(ts, last_ts + 1)
        last_ts = ts
        rgb = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        res = landmarker.detect_for_video(rgb, ts)

        quad = quad_from_hands(res.hand_landmarks, w, h)
        if quad is not None and convex_ok(quad, w, h):
            a = min(max(args.smooth, 0.0), 0.95)
            quad_s = quad if quad_s is None else a * quad_s + (1 - a) * quad
            lost = 0
        else:
            lost += 1
            if lost > 5:
                quad_s = None

        out = frame.copy()
        if quad_s is not None:
            efeito = FUNCS[EFFECTS[fx]](frame, t)
            src_pts = np.array([[0, 0], [w, 0], [w, h], [0, h]], np.float32)
            M = cv2.getPerspectiveTransform(src_pts, quad_s)
            warped = cv2.warpPerspective(efeito, M, (w, h))
            mask = np.zeros((h, w), np.uint8)
            cv2.fillConvexPoly(mask, quad_s.astype(np.int32), 255)
            out = np.where(mask[..., None] > 0, warped, out)
            cv2.polylines(out, [quad_s.astype(np.int32)], True, (255, 255, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(out, "Forme um retangulo com polegar e indicador das duas maos",
                        (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        if show_dbg:
            draw_hands(out, res.hand_landmarks)

        if args.output:
            if writer is None:
                writer = cv2.VideoWriter(args.output, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
            writer.write(out)
        if not args.no_window:
            cv2.imshow("Efeito Maos", out)
            k = cv2.waitKey(1) & 0xFF
            if k in (27, ord("q")):
                break
            elif k == ord("e"):
                fx = (fx + 1) % len(EFFECTS)
            elif k == ord("m"):
                mirror = not mirror
            elif k == ord("d"):
                show_dbg = not show_dbg

    cap.release()
    if writer:
        writer.release()
    landmarker.close()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
