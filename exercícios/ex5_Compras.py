import tkinter as tk
from tkinter import messagebox

def atualizar_total():
    total.config(text=f"Itens: {lista.size()}")

def adicionar():
    item = entrada.get().strip()

    if item == "":
        messagebox.showwarning("Atenção", "Digite um item!")
    elif item in lista.get(0, tk.END):
        messagebox.showwarning("Atenção", "Esse item já está na lista!")
    else:
        lista.insert(tk.END, item)
        entrada.delete(0, tk.END)

    atualizar_total()

def remover():
    selecionado = lista.curselection()

    if not selecionado:
        messagebox.showinfo("Aviso", "Selecione um item para remover!")
    else:
        lista.delete(selecionado[0])

    atualizar_total()

def limpar():
    resposta = messagebox.askyesno(
        "Confirmar",
        "Deseja apagar todos os itens?"
    )

    if resposta:
        lista.delete(0, tk.END)

    atualizar_total()


janela = tk.Tk()
janela.title("Lista de Compras")
janela.geometry("350x400")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="Minha Lista de Compras",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

entrada = tk.Entry(janela, width=30)
entrada.pack(pady=5)

botao_adicionar = tk.Button(
    janela,
    text="Adicionar",
    command=adicionar
)
botao_adicionar.pack(pady=5)

lista = tk.Listbox(janela, width=35, height=10)
lista.pack(pady=10)

botao_remover = tk.Button(
    janela,
    text="Remover selecionado",
    command=remover
)
botao_remover.pack(pady=5)

botao_limpar = tk.Button(
    janela,
    text="Limpar lista",
    command=limpar
)
botao_limpar.pack(pady=5)

total = tk.Label(
    janela,
    text="Itens: 0",
    font=("Arial", 11)
)
total.pack(pady=10)

janela.mainloop()