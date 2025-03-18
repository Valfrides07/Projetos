#Projeto de interface

import customtkinter as ctk

#Configuração da aparencia

ctk.set_appearance_mode('dark')

#Funcionalidade app

def validar_login():
    usuario = Campo_usuario.get()
    senha = Campo_senha.get() 
    
    # Verificação se o usuario e senha estão corretos
    if usuario == 'Valfrides' and senha == '12345':
        mensagem_login.configure (text = 'Login realizado com sucesso!',text_color = 'White')
        
    else:
        mensagem_login.configure(text='Login incorreto.',text_color= 'White')

#Criação da janela principal

janela_principal = ctk.CTk()
janela_principal.title('Sistema de Login')
janela_principal.geometry('300x300')

# Campos 1,2,3

# Label = Informativo acima da barra onde o usuario irá interagir
Label_usuario = ctk.CTkLabel(janela_principal,text='Usuário')

# Pady(Distancia) de Usuario até o topo
Label_usuario.pack(pady = 20)
 
# Entry = barra de interação onde o usuario irá digitar login

Campo_usuario = ctk.CTkEntry(janela_principal,placeholder_text='Digite o seu usuário')
Campo_usuario.pack(pady = 5)

# Label senha
Label_senha = ctk.CTkLabel(janela_principal,text='Senha')
Label_senha.pack(pady = 5)

# Campo Senha
Campo_senha = ctk.CTkEntry(janela_principal,placeholder_text='Digite a sua senha',show='*')
Campo_senha.pack(pady=10)

#Button = Botao de login
Botao_usuario = ctk.CTkButton(janela_principal,text='Login', command=validar_login)
Botao_usuario.pack(pady=10)
# Mensagem erro login
mensagem_login = ctk.CTkLabel(janela_principal, text=' ')
mensagem_login.pack(pady = 10)

# Inicialização app

janela_principal.mainloop() 