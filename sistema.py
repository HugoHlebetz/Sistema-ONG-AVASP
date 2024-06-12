import customtkinter as ctk
from tkinter import messagebox, PhotoImage
import mysql.connector

# Configuração inicial
ctk.set_appearance_mode("dark")  # Modos: "dark" (padrão), "light", "system"
ctk.set_default_color_theme("dark-blue")  # Temas: "blue" (padrão), "green", "dark-blue")

# Criando a janela principal
root = ctk.CTk()
root.title("Verbo Amar")
root.iconbitmap('WhatsApp-Image-2024-06-10-at-15.31.43.ico')
root.state("zoomed")  # Definindo a janela para tela cheia


def connect_to_db():
    return mysql.connector.connect(
        host='verbo-amar2.c3emqawq4ond.sa-east-1.rds.amazonaws.com',
        user='admin',
        password='verboamar',
        database='verboAmar',
        port='3306'
    )


# Função de callback para o botão de login

def consultar_beneficiario(documento_entry):
    try:
        # Extrair o valor de texto do campo de entrada
        documento = documento_entry.get()

        connection = connect_to_db()
        if connection is None:
            return None

        cursor = connection.cursor()

        query = "SELECT * FROM beneficiarios WHERE documento = %s"
        cursor.execute(query, (documento,))
        beneficiario = cursor.fetchone()

        cursor.close()
        connection.close()

        if beneficiario:
            # Formatar as informações do beneficiário para exibição
            beneficiario_info = (
                f"Documento: {beneficiario[0]}\n"
                f"Condição: {beneficiario[1]}\n"
                f"Nome: {beneficiario[2]}\n"
                f"Data de Nascimento: {beneficiario[3]}\n"
                f"Sexo: {beneficiario[4]}\n"
                f"Raça/Cor: {beneficiario[5]}\n"
                f"Telefone/WhatsApp: {beneficiario[6]}\n"
                f"Endereço: {beneficiario[7]}\n"
                f"Email: {beneficiario[8]}\n"
                f"Escolaridade: {beneficiario[9]}\n"
                f"Deficiência: {beneficiario[10]}\n"
                f"Tipo de Deficiência: {beneficiario[11]}\n"
                f"Atividades: {beneficiario[12]}\n"
                f"Observações: {beneficiario[13]}"
            )
            messagebox.showinfo("Informações do Beneficiário", beneficiario_info)
        else:
            messagebox.showinfo("Não encontrado", "Beneficiário não encontrado.")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao consultar beneficiário: {err}")



# Função para excluir beneficiário
def excluir_beneficiario(documento_entry):
    try:
        # Extrair o valor de texto do campo de entrada
        documento = documento_entry.get()

        connection = connect_to_db()
        if connection is None:
            return

        cursor = connection.cursor()

        query = "DELETE FROM beneficiarios WHERE documento = %s"
        cursor.execute(query, (documento,))
        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Exclusão", "Beneficiário excluído com sucesso!")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao excluir beneficiário: {err}")


# Função para alterar beneficiário
def alterar_beneficiario(documento_entry, nome_entry, data_nascimento_entry, sexo_entry, telefone_entry, condicao_entry,
                         raca_etnia_entry, endereco_entry, email_entry, escolaridade_entry, deficiencia_entry,
                         tipo_deficiencia_entry, atividades_entry, obs_entry):
    try:
        # Extrair os valores de texto dos campos de entrada
        documento = documento_entry.get()
        nome = nome_entry.get()
        data_nascimento = data_nascimento_entry.get()
        sexo = sexo_entry.get()
        telefone = telefone_entry.get()
        condicao = condicao_entry.get()
        raca_etnia = raca_etnia_entry.get()
        endereco = endereco_entry.get()
        email = email_entry.get()
        escolaridade = escolaridade_entry.get()
        deficiencia = deficiencia_entry.get()
        tipo_deficiencia = tipo_deficiencia_entry.get()
        atividades = atividades_entry.get()
        obs = obs_entry.get()

        connection = connect_to_db()
        if connection is None:
            return

        cursor = connection.cursor()

        query = """
            UPDATE beneficiarios SET nome=%s, data_nascimento=%s, sexo=%s, telefone_whatsapp=%s,
            condicao=%s, raca_etnia=%s, endereco=%s, email=%s, escolaridade=%s, deficiencia=%s,
            tipo_deficiencia=%s, atividades=%s, obs=%s WHERE documento=%s
        """
        cursor.execute(query, (
        nome, data_nascimento, sexo, telefone, condicao, raca_etnia, endereco, email, escolaridade, deficiencia,
        tipo_deficiencia, atividades, obs, documento))
        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Alteração", "Beneficiário alterado com sucesso!")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao alterar beneficiário: {err}")


def registrar():
    username = entry_username.get()
    password = entry_password.get()

    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao cadastrar: {err}")


# Função de login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Erro", "Usuário e senha são obrigatórios")
        return

    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        query = "SELECT * FROM usuarios WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            open_menu()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
def save_beneficiario(entryNome, entryDataNasc, entrySexo, entryDocumento, entryTelefone, entryCondicao, entryRaca, entryEndereco, entryEmail, entryEscolaridade, entryDeficiencia, entryTipoDeficiencia, \
                      entryAtividades, entryOBS):
    # Obtendo os valores dos campos de entrada
    nome = entryNome.get()
    data_nascimento = entryDataNasc.get()
    sexo = entrySexo.get()
    documento = entryDocumento.get()
    telefone = entryTelefone.get()
    condicao = entryCondicao.get()
    raca_etnia = entryRaca.get()
    endereco = entryEndereco.get()
    email = entryEmail.get()
    escolaridade = entryEscolaridade.get()
    deficiencia = entryDeficiencia.get()
    tipo_deficiencia = entryTipoDeficiencia.get()
    atividades = entryAtividades.get()
    obs = entryOBS.get()

    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # Comando SQL para inserir dados na tabela de beneficiários
        query = """
            INSERT INTO beneficiarios (documento, condicao, nome, data_nascimento, sexo, raca_etnia, telefone_whatsapp,
                                       endereco, email, escolaridade, deficiencia, tipo_deficiencia, atividades)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (documento, condicao, nome, data_nascimento, sexo, raca_etnia, telefone,
                               endereco, email, escolaridade, deficiencia, tipo_deficiencia, atividades))

        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Cadastro", "Beneficiário cadastrado com sucesso!")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao cadastrar beneficiário: {err}")

def open_menu():
    # Remove todos os widgets da janela principal
    for widget in root.winfo_children():
        widget.destroy()

    # Cria um frame centralizado para o menu
    menu_frame = ctk.CTkFrame(root)
    menu_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Adiciona os widgets do menu
    label_menu = ctk.CTkLabel(menu_frame, text="Menu Principal", font=("Arial", 24))
    label_menu.grid(row=0, column=0, columnspan=2, pady=20)

    buttons = [
        ("Cadastrar Beneficiários", show_cadastro_beneficiario),
        ("Gerar Relatórios", show_gerar_relatorios),
        ("Projetos", show_projetos),
        ("Financeiro", show_financeiro),
        ("Voluntários", show_voluntarios),
        ("Indicadores", show_indicadores)
    ]

    row, col = 1, 0
    for btn_text, btn_command in buttons:
        button = ctk.CTkButton(menu_frame, text=btn_text, width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=btn_command)
        button.grid(row=row, column=col, padx=20, pady=20)
        col += 1
        if col == 2:
            col = 0
            row += 1

    button_logout = ctk.CTkButton(menu_frame, text="Logout", command=logout, width=200, height=40, font=("Arial", 16), fg_color="#B22222")
    button_logout.grid(row=row+1, column=0, columnspan=2, pady=20)

def logout():
    # Remove todos os widgets do menu
    for widget in root.winfo_children():
        widget.destroy()

    # Adiciona de volta os widgets da tela de login
    show_login_screen()

def show_login_screen():
    # Remover tudo o que está na tela
    for widget in root.winfo_children():
        widget.destroy()

    # Criar um frame para a tela de login
    bg_frame = ctk.CTkFrame(root, width=1920, height=1080, fg_color="#B22222")
    bg_frame.place(relx=0.5, rely=0.5, anchor="center")

    login_frame = ctk.CTkFrame(root, width=600, height=600)  # Aumento do tamanho do frame
    login_frame.place(x=960, y=180)

    logo_frame = ctk.CTkFrame(root, width=600, height=1500)
    logo_frame.place(x=0, y=0)

    # Rótulo e entrada para o nome de usuário
    label_username = ctk.CTkLabel(login_frame, text="Usuário:", font=("Arial", 18))
    label_username.place(x=150, y=170)

    global entry_username
    entry_username = ctk.CTkEntry(login_frame, width=300, height=40, font=("Arial", 16))
    entry_username.place(x=150, y=200)

    # Rótulo e entrada para a senha
    label_password = ctk.CTkLabel(login_frame, text="Senha:", font=("Arial", 18))
    label_password.place(x=150, y=270)

    global entry_password
    entry_password = ctk.CTkEntry(login_frame, show="*", width=300, height=40, font=("Arial", 16))
    entry_password.place(x=150, y=300)

    # Botão de login
    button_login = ctk.CTkButton(login_frame, text="Entrar", command=login, width=300, height=40, font=("Arial", 16), fg_color="#B22222")
    button_login.place(x=150, y=400)

    button_registrar = ctk.CTkButton(login_frame, text="Registrar", command=registrar, width=300, height=40, font=("Arial", 16), fg_color="#B22222")
    button_registrar.place(x=150, y=450)

    img = PhotoImage(file='WhatsApp-Image-2024-06-10-at-15.31.20-removebg-preview.png')
    l_img = ctk.CTkLabel(root, image=img, text='')
    l_img.place(x=150, y=250)


def show_cadastro_beneficiario():
    # Remove todos os widgets da janela principal
    for widget in root.winfo_children():
        widget.destroy()

    # Cria um frame para o cadastro de beneficiários
    cadastro_frame = ctk.CTkFrame(root, width=1600, height=1500)
    cadastro_frame.place(relx=0.5, rely=0.5, anchor="center")

    label_title = ctk.CTkLabel(cadastro_frame, text="Cadastro de Beneficiários", font=("Arial", 24))
    label_title.grid(row=0, column=0, columnspan=2, pady=20)

    labels = [
        "Nome", "Condição", "Documento", "Data de Nascimento", "Sexo",
        "Raça/Etnia", "Telefone", "Endereço", "E-mail", "Escolaridade",
        "Deficiência", "Tipo Deficiencia", "Atividades praticadas", "OBS"
    ]

    entries = {}
    row = 1
    for label_text in labels:
        label = ctk.CTkLabel(cadastro_frame, text=f"{label_text}:", font=("Arial", 16))
        label.grid(row=row, column=0, pady=10, padx=10, sticky="e")

        row += 1
    entryNome = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryNome.grid(row=1, column=1, pady=10, padx=10, sticky="w")

    entryCondicao = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryCondicao.grid(row=2, column=1, pady=10, padx=10, sticky="w")

    entryDocumento = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryDocumento.grid(row=3, column=1, pady=10, padx=10, sticky="w")

    entryDataNasc = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryDataNasc.grid(row=4, column=1, pady=10, padx=10, sticky="w")

    entrySexo = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entrySexo.grid(row=5, column=1, pady=10, padx=10, sticky="w")

    entryRaca = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryRaca.grid(row=6, column=1, pady=10, padx=10, sticky="w")

    entryTelefone = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryTelefone.grid(row=7, column=1, pady=10, padx=10, sticky="w")

    entryEndereco = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryEndereco.grid(row=8, column=1, pady=10, padx=10, sticky="w")

    entryEmail = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryEmail.grid(row=9, column=1, pady=10, padx=10, sticky="w")

    entryEscolaridade = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryEscolaridade.grid(row=10, column=1, pady=10, padx=10, sticky="w")

    entryDeficiencia = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryDeficiencia.grid(row=11, column=1, pady=10, padx=10, sticky="w")

    entryTipoDeficiencia = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryTipoDeficiencia.grid(row=12, column=1, pady=10, padx=10, sticky="w")

    entryAtividades = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryAtividades.grid(row=13, column=1, pady=10, padx=10, sticky="w")

    entryOBS = ctk.CTkEntry(cadastro_frame, width=400, font=("Arial", 16))
    entryOBS.grid(row=14, column=1, pady=10, padx=10, sticky="w")

    button_save = ctk.CTkButton(cadastro_frame, text="Salvar", width=150, height=40, font=("Arial", 16),
                                fg_color="#B22222",
                                command=lambda: save_beneficiario(entryNome, entryDataNasc, entrySexo, entryDocumento,
                                                                  entryTelefone, entryCondicao, entryRaca,
                                                                  entryEndereco, entryEmail, entryEscolaridade,
                                                                  entryDeficiencia, entryTipoDeficiencia,
                                                                  entryAtividades, entryOBS))

    button_save.grid(row=row, column=0, columnspan=2, pady=20)

    button_back = ctk.CTkButton(cadastro_frame, text="Voltar", width=150, height=40, font=("Arial", 16), fg_color="#B22222", command=open_menu)
    button_back.grid(row=row+1, column=0, columnspan=2, pady=20)

    button_excluir = ctk.CTkButton(cadastro_frame, text='Excluir', width=150, height=40, font=("Arial", 16),
                                     fg_color="#B22222", command=lambda: excluir_beneficiario(entryDocumento))
    button_excluir.grid(row=row+2, column=0, columnspan=2, pady=20)

    button_consultar = ctk.CTkButton(cadastro_frame, text='Consultar', width=150, height=40, font=("Arial", 16),
                                     fg_color="#B22222", command=lambda: consultar_beneficiario(entryDocumento))
    button_consultar.place(x=420, y=760)
    button_atualizar = ctk.CTkButton(cadastro_frame, text='Atualizar', width=150, height=40, font=("Arial", 16),
                                     fg_color="#B22222", command=lambda: alterar_beneficiario(entryNome, entryDataNasc, entrySexo, entryDocumento,
                                                                  entryTelefone, entryCondicao, entryRaca,
                                                                  entryEndereco, entryEmail, entryEscolaridade,
                                                                  entryDeficiencia, entryTipoDeficiencia,
                                                                  entryAtividades, entryOBS))
    button_atualizar.place(x=420, y=840)

def show_projetos():
    # Remove todos os widgets da janela principal
    for widget in root.winfo_children():
        widget.destroy()

    # Cria um frame para o cadastro de projetos
    projeto_frame = ctk.CTkFrame(root, width=1600, height=800)
    projeto_frame.place(relx=0.5, rely=0.5, anchor="center")

    label_title = ctk.CTkLabel(projeto_frame, text="Cadastro de Projetos", font=("Arial", 24))
    label_title.grid(row=0, column=0, columnspan=2, pady=20)

    labels = [
        "Nome do projeto", "Data de início", "Data de término", "Participantes"
    ]

    entries = {}
    row = 1
    for label_text in labels:
        label = ctk.CTkLabel(projeto_frame, text=f"{label_text}:", font=("Arial", 16))
        label.grid(row=row, column=0, pady=10, padx=10, sticky="e")

        entry = ctk.CTkEntry(projeto_frame, width=400, font=("Arial", 16))
        entry.grid(row=row, column=1, pady=10, padx=10, sticky="w")
        entries[label_text] = entry

        row += 1

    button_save = ctk.CTkButton(projeto_frame, text="Salvar", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=lambda: save_projeto(entries))
    button_save.grid(row=row, column=0, columnspan=2, pady=20)

    button_list = ctk.CTkButton(projeto_frame, text="Listar Projetos", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=listar_projetos)
    button_list.grid(row=row+1, column=0, columnspan=2, pady=20)

    button_back = ctk.CTkButton(projeto_frame, text="Voltar", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=open_menu)
    button_back.grid(row=row+2, column=0, columnspan=2, pady=20)

def show_voluntarios():
    # Remove todos os widgets da janela principal
    for widget in root.winfo_children():
        widget.destroy()

    # Cria um frame para a lista de beneficiários
    voluntario_frame = ctk.CTkFrame(root, width=1600, height=800)
    voluntario_frame.place(relx=0.5, rely=0.5, anchor="center")

    label_title = ctk.CTkLabel(voluntario_frame, text="Lista de Beneficiários", font=("Arial", 24))
    label_title.grid(row=0, column=0, columnspan=20, pady=20)

    # Simulação da lista de beneficiários
    beneficiarios = [
        " tabela ",
    ]

    for i, beneficiario in enumerate(beneficiarios, start=1):
        label = ctk.CTkLabel(voluntario_frame, text=beneficiario, font=("Arial", 16))
        label.grid(row=i, column=0, pady=10, padx=100)

    button_back = ctk.CTkButton(voluntario_frame, text="Voltar", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=open_menu)
    button_back.grid(row=i+1, column=0, pady=20)

def show_gerar_relatorios():
    # Remove todos os widgets da janela principal
    for widget in root.winfo_children():
        widget.destroy()

    # Cria um frame para gerar relatórios
    relatorio_frame = ctk.CTkFrame(root, width=1600, height=800)
    relatorio_frame.place(relx=0.5, rely=0.5, anchor="center")

    label_title = ctk.CTkLabel(relatorio_frame, text="Gerar Relatórios", font=("Arial", 24))
    label_title.grid(row=0, column=0, columnspan=2, pady=20)

    text_relatorio = ctk.CTkTextbox(relatorio_frame, width=500, height=500, font=("Arial", 16))
    text_relatorio.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

    button_save = ctk.CTkButton(relatorio_frame, text="Salvar Relatório", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=lambda: save_relatorio(text_relatorio))
    button_save.grid(row=2, column=0, columnspan=2, pady=20)

    button_list = ctk.CTkButton(relatorio_frame, text="Listar Relatórios", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=listar_relatorios)
    button_list.grid(row=3, column=0, columnspan=2, pady=20)

    button_back = ctk.CTkButton(relatorio_frame, text="Voltar", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=open_menu)
    button_back.grid(row=4, column=0, columnspan=2, pady=20)

def show_financeiro():
    # Remove todos os widgets da janela principal
    for widget in root.winfo_children():
        widget.destroy()

    # Cria um frame para o menu financeiro
    financeiro_frame = ctk.CTkFrame(root, width=1600, height=800)
    financeiro_frame.place(relx=0.5, rely=0.5, anchor="center")

    label_title = ctk.CTkLabel(financeiro_frame, text="Menu Financeiro", font=("Arial", 24))
    label_title.grid(row=0, column=0, columnspan=2, pady=20)

    buttons = [
        ("Cadastrar Empresas", show_cadastro_empresa),
        ("Cadastrar ONGs", show_cadastro_ong),
        ("Cadastrar Editais", show_cadastro_edital)
    ]

    row, col = 1, 0
    for btn_text, btn_command in buttons:
        button = ctk.CTkButton(financeiro_frame, text=btn_text, width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=btn_command)
        button.grid(row=row, column=col, padx=20, pady=20)
        col += 1
        if col == 2:
            col = 0
            row += 1

    button_back = ctk.CTkButton(financeiro_frame, text="Voltar", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=open_menu)
    button_back.grid(row=row+1, column=0, columnspan=2, pady=20)



def show_cadastro_empresa():
    show_cadastro_financeiro("Empresa")

def show_cadastro_ong():
    show_cadastro_financeiro("ONG")

def show_cadastro_edital():
    show_cadastro_financeiro("Edital")

def show_cadastro_financeiro(tipo):
    # Remove todos os widgets da janela principal
    for widget in root.winfo_children():
        widget.destroy()

    # Cria um frame para o cadastro financeiro
    financeiro_frame = ctk.CTkFrame(root, width=1600, height=800)
    financeiro_frame.place(relx=0.5, rely=0.5, anchor="center")

    label_title = ctk.CTkLabel(financeiro_frame, text=f"Cadastro de {tipo}s", font=("Arial", 24))
    label_title.grid(row=0, column=0, columnspan=2, pady=20)

    labels = [
        "Nome", "Telefone/WhatsApp", "Endereço", "E-mail", "Data de aniversário",
        "Documento", "Profissão", "Valor", "Forma de pagamento", "Apadrinhamento",
        "Data de entrada", "Data de saída", "OBS"
    ]

    entries = {}
    row = 1
    for label_text in labels:
        label = ctk.CTkLabel(financeiro_frame, text=f"{label_text}:", font=("Arial", 16))
        label.grid(row=row, column=0, pady=10, padx=10, sticky="e")

        entry = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
        entry.grid(row=row, column=1, pady=10, padx=10, sticky="w")
        entries[label_text] = entry

        row += 1

    button_save = ctk.CTkButton(financeiro_frame, text="Salvar", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=lambda: save_financeiro(entries))
    button_save.grid(row=row, column=0, columnspan=2, pady=20)

    button_back = ctk.CTkButton(financeiro_frame, text="Voltar", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=show_financeiro)
    button_back.grid(row=row+1, column=0, columnspan=2, pady=20)

def listar_projetos():
    # Função para listar projetos
    messagebox.showinfo("Lista de Projetos", "Lista de projetos cadastrados:\n- Projeto 1\n- Projeto 2")

def listar_relatorios():
    # Função para listar relatórios
    messagebox.showinfo("Lista de Relatórios", "Lista de relatórios gerados:\n- Relatório 1\n- Relatório 2")

def save_projeto(entries):
    data = {label: entry.get() for label, entry in entries.items()}
    print(data)  # Aqui você pode adicionar a lógica para salvar os dados
    messagebox.showinfo("Sucesso", "Projeto salvo com sucesso!")

def save_relatorio(text_widget):
    data = text_widget.get("1.0", "end-1c")
    print(data)  # Aqui você pode adicionar a lógica para salvar o relatório
    messagebox.showinfo("Sucesso", "Relatório salvo com sucesso!")

def save_financeiro(entries):
    data = {label: entry.get() for label, entry in entries.items()}
    print(data)  # Aqui você pode adicionar a lógica para salvar os dados
    messagebox.showinfo("Sucesso", "Dados financeiros salvos com sucesso!")

def show_indicadores():
    # Remove todos os widgets da janela principal
    for widget in root.winfo_children():
        widget.destroy()

    # Cria um frame para a lista de beneficiários
    indicador_frame = ctk.CTkFrame(root, width=1600, height=800)
    indicador_frame.place(relx=0.5, rely=0.5, anchor="center")

    label_title = ctk.CTkLabel(indicador_frame, text="Indicadores", font=("Arial", 24))
    label_title.grid(row=0, column=0, columnspan=2, pady=20)

    # Simulação da lista de beneficiários
    indicadores = [
        "tabela"
    ]
    for i, beneficiario in enumerate(indicadores, start=1):
        label = ctk.CTkLabel(indicador_frame, text=beneficiario, font=("Arial", 16))
        label.grid(row=i, column=0, pady=10, padx=100)

    button_back = ctk.CTkButton(indicador_frame, text="Voltar", width=200, height=40, font=("Arial", 16),
                                fg_color="#B22222", command=open_menu)
    button_back.grid(row=i + 1, column=0, pady=20)

# Mostrar a tela de login inicialmente
show_login_screen()

# Iniciando o loop principal
root.mainloop()
