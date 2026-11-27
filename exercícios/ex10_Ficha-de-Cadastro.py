import tkinter as tk
from tkinter import ttk, messagebox

janela = tk.Tk()
janela.title("Ficha de Cadastro de Aluno")
janela.resizable(False, False)


turma = tk.StringVar()
periodo = tk.StringVar()
programacao = tk.BooleanVar()
redes = tk.BooleanVar()
design = tk.BooleanVar()
regras = tk.BooleanVar()


def validar():
    if not nome.get().strip():
        messagebox.showwarning("Aviso", "Digite o nome completo!")
        return False
    if not turma.get():
        messagebox.showwarning("Aviso", "Escolha uma turma!")
        return False
    if not periodo.get():
        messagebox.showwarning("Aviso", "Escolha um período!")
        return False
    if not regras.get():
        messagebox.showwarning("Aviso", "Aceite as regras!")
        return False
    return True


def cadastrar():
    if validar():
        interesses = [n for n, v in [
            ("Programação", programacao),
            ("Redes", redes),
            ("Design", design)
        ] if v.get()]

        resumo = ", ".join(interesses) if interesses else "Nenhum"

        messagebox.showinfo(
            "Cadastro realizado",
            f"Nome: {nome.get().strip()}\n"
            f"Turma: {turma.get()}\n"
            f"Período: {periodo.get()}\n"
            f"Interesses: {resumo}"
        )


def limpar():
    nome.delete(0, tk.END)
    turma.set("")
    periodo.set("")
    programacao.set(False)
    redes.set(False)
    design.set(False)
    regras.set(False)


def sair():
    if messagebox.askyesno("Sair", "Deseja fechar o programa?"):
        janela.destroy()


tk.Label(janela, text="Nome completo:").grid(row=0, column=0, padx=10, pady=5)
nome = tk.Entry(janela, width=30)
nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Turma:").grid(row=1, column=0, padx=10, pady=5)
ttk.Combobox(janela, textvariable=turma, values=["1MI", "1MA", "1ML"], state="readonly").grid(row=1, column=1)

tk.Label(janela, text="Período:").grid(row=2, column=0, padx=10, pady=5)
for i, p in enumerate(["Manhã", "Tarde", "Noite"]):
    tk.Radiobutton(janela, text=p, variable=periodo, value=p).grid(row=2+i, column=1, sticky="w")

tk.Label(janela, text="Interesses:").grid(row=5, column=0, padx=10, pady=5)
for i, (n, v) in enumerate([
    ("Programação", programacao),
    ("Redes", redes),
    ("Design", design)
]):
    tk.Checkbutton(janela, text=n, variable=v).grid(row=5+i, column=1, sticky="w")

tk.Checkbutton(janela, text="Li e aceito as regras", variable=regras).grid(row=8, column=1, pady=5)


tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=9, column=0, pady=10)
tk.Button(janela, text="Limpar", command=limpar).grid(row=9, column=1)
tk.Button(janela, text="Sair", command=sair).grid(row=10, column=1, pady=5)

janela.mainloop()