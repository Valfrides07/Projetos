#Projeto de interface

import customtkinter as ctk
import sqlite3
from pathlib import Path
DB_FILE = Path(__file__).parent / 'db.sqlite3'


DB_NAME = "db.sqlite3"
DB_FILE = DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT," "nome TEXT," "senha TEXT"")"
)
connection.commit()
cursor.close()
connection.close()


#Funcionalidade app/ integração com o banco de Dados

def validar_login():
    usuario = Campo_usuario.get().strip()
    senha = Campo_senha.get().strip()
    
    if not usuario or not senha:
        mensagem_login.configure(text="Usuário e senha não podem estar vazios!", text_color=" white") 
    
    #Conectar uusario no banco de dados
    
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    
    # Buscar usuario no banco de Dados
    cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE nome = ? AND senha = ?", (usuario,senha))
    usuario_encontrado = cursor.fetchone()
    
    if usuario_encontrado:
        # Se existir, irá verifcar a senha
        if usuario_encontrado[2] == senha:
            mensagem_login.configure(text="ogin realizado com sucesso!", text_color="white")
        
        else:
            mensagem_login.configure(text="Senha incorreta!", text_color="white")
    else:
        # Se não existir, cadastrar usuário automaticamente
        cursor.execute(f"INSERT INTO {TABLE_NAME} (nome , senha) VALUES(?,?)",(usuario, senha))
        connection.commit()
        mensagem_login.configure(text="Usuario cadastrado com sucesso!", text_color="white")
        
    
    # Fechar conexão e o cursor
    cursor.close()
    connection.close()
    
    # Verificação se o usuario foram encontrados
    # if usuario_encontrado:
        # mensagem_login.configure (text = 'Login realizado com sucesso!',text_color = 'White')
        # 
    # else:
        # mensagem_login.configure(text='Login ou senha incorretos.',text_color= 'White')
#Configuração da aparencia

ctk.set_appearance_mode('dark')

#Criação da janela principal
janela_principal = ctk.CTk()
janela_principal.title('Sistema de Login')
janela_principal.geometry('300x300')


# Label = Informativo acima da barra onde o usuario irá interagir
Label_usuario = ctk.CTkLabel(janela_principal,text='Login')

# Pady(Distancia) de Usuario até o topo
Label_usuario.pack(pady = 20)
 
# Entry = barra de interação onde o usuario irá digitar login
Campo_usuario = ctk.CTkEntry(janela_principal,placeholder_text='Seu usuário')
Campo_usuario.pack(pady = 5)

# Label senha
Label_senha = ctk.CTkLabel(janela_principal,text='Senha')
Label_senha.pack(pady = 5)

# Campo Senha
Campo_senha = ctk.CTkEntry(janela_principal,placeholder_text='Sua senha',show='*')
Campo_senha.pack(pady=10)

#Button = Botao de login
Botao_usuario = ctk.CTkButton(janela_principal,text='Login', command=validar_login)
Botao_usuario.pack(pady=10)

# Mensagem erro login
mensagem_login = ctk.CTkLabel(janela_principal, text=' ')
mensagem_login.pack(pady = 10)

# Inicialização app

janela_principal.mainloop() 