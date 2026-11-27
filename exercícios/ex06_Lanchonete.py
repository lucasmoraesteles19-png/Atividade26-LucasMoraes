
import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Pedido de Lanchonete")
janela.geometry("300x350")

hambuguer = tk.BooleanVar()
Batata = tk.BooleanVar()
refrigerante = tk.BooleanVar()
suco = tk.BooleanVar()
gorjeta = tk.BooleanVar()

tk.Label(janela, text="Escolha seu pedido").pack(pady=10)

itens = [
    ("Hambúrguer - R$ 18,00", hambuguer),
    ("Batata Frita - R$ 10,00", Batata),
    ("Refrigerante - R$ 6,00", refrigerante),
    ("Suco - R$ 7,00", suco),
    ("Gorjeta de 10%", gorjeta)
]

for texto, variavel in itens:
    tk.Checkbutton(janela, text=texto, variable=variavel).pack()

resultado = tk.Label(janela, text="Total: R$ 0,00")
resultado.pack(pady=10)

def calcular():
    total = sum([
        hambuguer.get() * 18,
        Batata.get() * 10,
        refrigerante.get() * 6,
        suco.get() * 7
    ])

    if total == 0:
        messagebox.showwarning("Atenção", "Selecione um item!")
        return

    if gorjeta.get():
        total *= 1.10

    resultado.config(text=f"Total: R$ {total:.2f}")

def novo_pedido():
    for texto, variavel in itens:
        variavel.set(False)

    resultado.config(text="Total: R$ 0,00")

tk.Button(janela, text="Calcular total", command=calcular).pack(pady=5)
tk.Button(janela, text="Novo pedido", command=novo_pedido).pack()

janela.mainloop()
