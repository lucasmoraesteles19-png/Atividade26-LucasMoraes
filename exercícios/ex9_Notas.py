import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Bloco de Notas")


texto = tk.Text(janela, width=50, height=12)
texto.pack(pady=10)

def contar_palavras():
    conteudo = texto.get("1.0", "end-1c")

    if not conteudo.strip():
        messagebox.showwarning("Aviso", "Não há nada escrito!")
    else:
        palavras = len(conteudo.split())
        caracteres = len(conteudo)
        messagebox.showinfo("Contagem", f"Palavras: {palavras}\nCaracteres: {caracteres}")

def maiusculas():
    conteudo = texto.get("1.0", "end-1c")

    if not conteudo.strip():
        messagebox.showwarning("Aviso", "Não há nada escrito!")
    else:
        texto.delete("1.0", "end")
        texto.insert("1.0", conteudo.upper())

def limpar():
    if messagebox.askyesno("Limpar", "Deseja apagar todo o texto?"):
        texto.delete("1.0", "end")

def sair():
    if messagebox.askyesno("Sair", "Deseja fechar o programa?"):
        janela.destroy()

tk.Button(janela, text="Contar palavras", command=contar_palavras).pack()
tk.Button(janela, text="Maiúsculas", command=maiusculas).pack()
tk.Button(janela, text="Limpar", command=limpar).pack()
tk.Button(janela, text="Sair", command=sair).pack()

janela.mainloop()
