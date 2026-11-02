# Efeito "moldura de mãos psicodélica"

Recriação em Python (OpenCV + MediaPipe) do efeito do vídeo, originalmente feito em TouchDesigner:
as duas mãos formam um retângulo com polegar e indicador e, dentro dele, aparece a imagem da câmera
com cores psicodélicas, deformada em perspectiva acompanhando os dedos.

## Como usar
```bash
pip install -r requirements.txt
python efeito_maos.py                 # webcam
python efeito_maos.py --source video.mp4 --output saida.mp4 --no-window
```
O modelo de mãos (~8 MB) é baixado automaticamente na primeira execução.

Teclas: `q`/ESC sair · `e` trocar efeito (psicodélico, solarizado, neon) · `m` espelhar · `d` mostrar pontos dos dedos.

Obs.: este projeto é independente do sistema da ONG (`sistema.py`).

## Versão web (iPhone / Android / qualquer navegador)
`web/index.html` é uma versão em JavaScript (MediaPipe + WebGL) que roda no Safari do iPhone.
A câmera só funciona em **HTTPS**, então hospede a pasta (ex.: GitHub Pages) e abra o link no celular,
toque em "Ativar câmera" e permita o acesso. Botões: trocar efeito e virar câmera.
