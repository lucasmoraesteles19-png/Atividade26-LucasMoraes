
import tkinter as tk
from tkinter import messagebox

tentativas = 0

def entrar():
    global tentativas

    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == "" or senha == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos")

    elif usuario == "aluno" and senha == "1234":
        messagebox.showinfo("Login", "Bem-vindo(a), aluno!")
        tentativas = 0

    else:
        tentativas += 1
        messagebox.showerror("Erro", "Usuário ou senha incorretos")

        if tentativas == 3:
            janela.destroy()

def limpar():
    campo_usuario.delete(0, tk.END)
    campo_senha.delete(0, tk.END)

janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x200")
janela.resizable(False, False)

titulo = tk.Label(janela, text="LOGIN")
titulo.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(janela, text="Usuário:").grid(row=1, column=0, padx=5, pady=5)

campo_usuario = tk.Entry(janela)
campo_usuario.grid(row=1, column=1, padx=5, pady=5)

tk.Label(janela, text="Senha:").grid(row=2, column=0, padx=5, pady=5)

campo_senha = tk.Entry(janela, show="*")
campo_senha.grid(row=2, column=1, padx=5, pady=5)

botao_entrar = tk.Button(janela, text="Entrar", command=entrar)
botao_entrar.grid(row=3, column=0, pady=15)

botao_limpar = tk.Button(janela, text="Limpar", command=limpar)
botao_limpar.grid(row=3, column=1, pady=15)

janela.mainloop()
