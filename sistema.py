import customtkinter as ctk
from tkinter import messagebox, PhotoImage
import mysql.connector

# Configuração inicial
ctk.set_appearance_mode("dark")  # Modos: "dark" (padrão), "light", "system"
ctk.set_default_color_theme("dark-blue")  # Temas: "blue" (padrão), "green", "dark-blue")

# Criando a janela principal
root = ctk.CTk()
root.title("Verbo Amar")
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

def consultar_voluntario(documento2_entry):
    try:
        # Extrair o valor de texto do campo de entrada
        documento = documento2_entry.get()

        connection = connect_to_db()
        if connection is None:
            return None

        cursor = connection.cursor()

        query = "SELECT * FROM voluntarios WHERE documento = %s"
        cursor.execute(query, (documento,))
        voluntarios = cursor.fetchone()

        cursor.close()
        connection.close()

        if voluntarios:
            # Formatar as informações do beneficiário para exibição
            voluntario_info = (
                f"Nome: {voluntarios[0]}\n"
                f"Telefone: {voluntarios[1]}\n"
                f"Endereço: {voluntarios[2]}\n"
                f"E-mail: {voluntarios[3]}\n"
                f"Data de Nascimento: {voluntarios[4]}\n"
                f"Documento: {voluntarios[5]}\n"
                f"Profissão: {voluntarios[6]}\n"
                f"Valor: {voluntarios[7]}\n"
                f"Forma de Pagamento: {voluntarios[8]}\n"
                f"Apadrinhamento: {voluntarios[9]}\n"
                f"Data de Entrada: {voluntarios[10]}\n"
                f"Data de Saída: {voluntarios[11]}\n"
                f"OBS: {voluntarios[12]}"
            )
            messagebox.showinfo("Informações do Voluntário", voluntario_info)
        else:
            messagebox.showinfo("Não encontrado", "Voluntário não encontrado.")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao consultar Voluntário: {err}")

def excluir_voluntario(documento2_entry):
    try:
        # Extrair o valor de texto do campo de entrada
        documento = documento2_entry.get()

        connection = connect_to_db()
        if connection is None:
            return

        cursor = connection.cursor()

        query = "DELETE FROM voluntarios WHERE documento = %s"
        cursor.execute(query, (documento,))
        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Exclusão", "Voluntário excluído com sucesso!")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao excluir Voluntário: {err}")



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

def cadastrar_projeto(EntryNomeProjeto, EntryDataInicio, EntryDataTermino, EntryParticipantes):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # Obtendo os valores dos campos de entrada
        nome_projeto = EntryNomeProjeto.get()
        data_inicio = EntryDataInicio.get()
        data_termino = EntryDataTermino.get()
        participantes = EntryParticipantes.get()

        # Comando SQL para inserir dados na tabela de projetos
        query = """
            INSERT INTO projetos (nome_projeto, data_inicio, data_termino, participantes)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (nome_projeto, data_inicio, data_termino, participantes))


        connection.commit()
        cursor.close()
        connection.close()

        messagebox.showinfo("Cadastro de Projeto", "Projeto cadastrado com sucesso!")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao cadastrar projeto: {err}")

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
        ("Projetos", show_projetos),
        ("Financeiro", show_financeiro),
        ("Logout", logout),
    ]

    row, col = 1, 0
    for btn_text, btn_command in buttons:
        button = ctk.CTkButton(menu_frame, text=btn_text, width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=btn_command)
        button.grid(row=row, column=col, padx=20, pady=20)
        col += 1
        if col == 2:
            col = 0
            row += 1

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

    row = 1
    for label_text in labels:
        label = ctk.CTkLabel(projeto_frame, text=f"{label_text}:", font=("Arial", 16))
        label.grid(row=row, column=0, pady=10, padx=10, sticky="e")

        row += 1

    entryNomeProjeto = ctk.CTkEntry(projeto_frame, width=400, font=("Arial", 16))
    entryNomeProjeto.grid(row=1, column=1, pady=10, padx=10, sticky="w")

    entryProjetoDataInicio = ctk.CTkEntry(projeto_frame, width=400, font=("Arial", 16))
    entryProjetoDataInicio.grid(row=2, column=1, pady=10, padx=10, sticky="w")

    entryProjetoDataFim = ctk.CTkEntry(projeto_frame, width=400, font=("Arial", 16))
    entryProjetoDataFim.grid(row=3, column=1, pady=10, padx=10, sticky="w")

    entryParticipantes = ctk.CTkEntry(projeto_frame, width=400, font=("Arial", 16))
    entryParticipantes.grid(row=4, column=1, pady=10, padx=10, sticky="w")

    button_save = ctk.CTkButton(projeto_frame, text="Salvar", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=lambda: save_projeto(entryNomeProjeto, entryProjetoDataInicio, entryProjetoDataFim, entryParticipantes))
    button_save.grid(row=row, column=0, columnspan=2, pady=20)

    button_list = ctk.CTkButton(projeto_frame, text="Listar Projetos", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=listar_projetos)
    button_list.grid(row=row+1, column=0, columnspan=2, pady=20)

    button_delete = ctk.CTkButton(projeto_frame, text="Excluir Projeto", width=200, height=40, font=("Arial", 16),
                                  command=lambda: excluir_projeto(entryNomeProjeto), fg_color="#B22222",)
    button_delete.grid(row=row+2, column=0, columnspan=2, pady=20)

    button_back = ctk.CTkButton(projeto_frame, text="Voltar", width=200, height=40, font=("Arial", 16), fg_color="#B22222", command=open_menu)
    button_back.grid(row=row+3, column=0, columnspan=2, pady=20)

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
        ("Cadastrar Voluntários", lambda: show_cadastro_financeiro("voluntário"))
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

        row += 1
    entryNome2 = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryNome2.grid(row=1, column=1, pady=10, padx=10, sticky="w")

    entryTelefone2 = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryTelefone2.grid(row=2, column=1, pady=10, padx=10, sticky="w")

    entryEndereco2 = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryEndereco2.grid(row=3, column=1, pady=10, padx=10, sticky="w")

    entryEmail2 = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryEmail2.grid(row=4, column=1, pady=10, padx=10, sticky="w")

    entryDataNasc2 = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryDataNasc2.grid(row=5, column=1, pady=10, padx=10, sticky="w")

    entryDocumento2 = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryDocumento2.grid(row=6, column=1, pady=10, padx=10, sticky="w")

    entryProfissao = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryProfissao.grid(row=7, column=1, pady=10, padx=10, sticky="w")

    entryValor = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryValor.grid(row=8, column=1, pady=10, padx=10, sticky="w")

    entryFormaPagamento = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryFormaPagamento.grid(row=9, column=1, pady=10, padx=10, sticky="w")

    entryApadrinhamento = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryApadrinhamento.grid(row=10, column=1, pady=10, padx=10, sticky="w")

    entryDataEntrada = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryDataEntrada.grid(row=11, column=1, pady=10, padx=10, sticky="w")

    entryDataSaida = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryDataSaida.grid(row=12, column=1, pady=10, padx=10, sticky="w")

    entryobs2 = ctk.CTkEntry(financeiro_frame, width=400, font=("Arial", 16))
    entryobs2.grid(row=13, column=1, pady=10, padx=10, sticky="w")

    button_save = ctk.CTkButton(financeiro_frame, text="Salvar", width=150, height=40, font=("Arial", 16), fg_color="#B22222", command=lambda: save_financeiro(entryNome2, entryTelefone2, entryEndereco2, entryEmail2, entryDataNasc2, entryDocumento2, entryProfissao, entryValor, entryFormaPagamento, entryApadrinhamento, entryDataEntrada, entryDataSaida, entryobs2))
    button_save.grid(row=row, column=0, columnspan=2, pady=20)

    button_back = ctk.CTkButton(financeiro_frame, text="Voltar", width=150, height=40, font=("Arial", 16), fg_color="#B22222", command=show_financeiro)
    button_back.grid(row=row+1, column=0, columnspan=2, pady=20)

    button_excluir = ctk.CTkButton(financeiro_frame, text='Excluir', width=150, height=40, font=("Arial", 16),
                                     fg_color="#B22222", command=lambda: excluir_voluntario(entryDocumento2))
    button_excluir.grid(row=row+2, column=0, columnspan=2, pady=20)

    button_consultar = ctk.CTkButton(financeiro_frame, text='Consultar', width=150, height=40, font=("Arial", 16),
                                     fg_color="#B22222", command=lambda: consultar_voluntario(entryDocumento2))
    button_consultar.place(x=420, y=712)



# Função para excluir um projeto da lista e do banco de dados
def excluir_projeto(entryNomeProjeto):
    try:
        # Extrair o valor de texto do campo de entrada
        nomeProjeto = entryNomeProjeto.get()

        connection = connect_to_db()
        if connection is None:
            return

        cursor = connection.cursor()

        query = "DELETE FROM projetos WHERE nome_projeto = %s"
        cursor.execute(query, (nomeProjeto,))
        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Exclusão", "Projeto excluído com sucesso!")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao excluir Projeto: {err}")


def listar_projetos(entryNomeProjeto):
    try:
        # Extrair o valor de texto do campo de entrada
        nomeProjeto = entryNomeProjeto.get()

        connection = connect_to_db()
        if connection is None:
            return None

        cursor = connection.cursor()

        query = "SELECT * FROM projetos WHERE nome_projeto = %s"
        cursor.execute(query, (nomeProjeto,))
        voluntarios = cursor.fetchone()

        cursor.close()
        connection.close()

        if nomeProjeto:
            # Formatar as informações do beneficiário para exibição
            projetos_info = (
                f"Nome: {nomeProjeto[0]}\n"
                f"Data Início: {nomeProjeto[1]}\n"
                f"Data Fim: {nomeProjeto[2]}\n"
                f"Participantes: {nomeProjeto[3]}\n"
            )
            messagebox.showinfo("Informações do Projeto", projetos_info)
        else:
            messagebox.showinfo("Não encontrado", "Projeto não encontrado.")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao consultar Projeto: {err}")


def save_projeto(entryNomeProjeto, entryProjetoDataInicio, entryProjetoDataFim, entryParticipantes):
    nomeProjeto = entryNomeProjeto.get()
    dataInicio = entryProjetoDataInicio.get()
    dataFim = entryProjetoDataFim.get()
    participantes = entryParticipantes.get()

    try:
        connection = connect_to_db()
        cursor = connection.cursor()

    # Comando SQL para inserir dados na tabela de beneficiários
        query =    """
                INSERT INTO projetos (nome_projeto, data_inicio, data_termino, participantes)
                VALUES (%s, %s, %s, %s)
             """
        cursor.execute(query, (nomeProjeto, dataInicio, dataFim, participantes))

        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Cadastro", "Beneficiário cadastrado com sucesso!")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao cadastrar beneficiário: {err}")

def save_relatorio(text_widget):
    data = text_widget.get("1.0", "end-1c")
    print(data)  # Aqui você pode adicionar a lógica para salvar o relatório
    messagebox.showinfo("Sucesso", "Relatório salvo com sucesso!")

def save_financeiro(entryNome2, entryTelefone2, entryEndereco2, entryEmail2, entryDataNasc2, entryDocumento2, entryProfissao, entryValor, entryFormaPagamento, entryApadrinhamento, entryDataEntrada, entryDataSaida, entryobs2):

    # Obtendo os valores dos campos de entrada
    nome2 = entryNome2.get()
    telefone2 = entryTelefone2.get()
    endereco2 = entryEndereco2.get()
    email2 = entryEmail2.get()
    data_nascimento2 = entryDataNasc2.get()
    documento2 = entryDocumento2.get()
    profissao = entryProfissao.get()
    valor = entryValor.get()
    formaPagamento = entryFormaPagamento.get()
    apadrinhamento = entryApadrinhamento.get()
    dataEntrada2 = entryDataEntrada.get()
    dataSaida2 = entryDataSaida.get()
    obs2 = entryobs2.get()


    try:
        connection = connect_to_db()
        cursor = connection.cursor()

    # Comando SQL para inserir dados na tabela de beneficiários
        query =    """
                INSERT INTO voluntarios (nome, telefone, endereco, email, data_nascimento, documento, profissao,
                                       valor, formaPagamento, apadrinhamento, dataEntrada, dataSaida, obs)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
             """
        cursor.execute(query, (nome2, telefone2, endereco2, email2, data_nascimento2, documento2, profissao,
                            valor, formaPagamento, apadrinhamento, dataEntrada2, dataSaida2, obs2))

        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Cadastro", "Beneficiário cadastrado com sucesso!")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao cadastrar beneficiário: {err}")

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
