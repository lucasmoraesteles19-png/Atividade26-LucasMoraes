
import tkinter as tk
from tkinter import messagebox

# Lê os números
def ler_numeros():
    try:
        n1 = float(entrada_peso.get().replace(",", "."))
        n2 = float(entrada_numero2.get().replace(",", "."))
        return n1, n2
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos!")
        return None

# Mostra o resultado
def calcular(operacao):
    numeros = ler_numeros()
    if numeros is None:
        return

    n1, n2 = numeros

    if operacao == "+":
        valor = n1 + n2
    elif operacao == "-":
        valor = n1 - n2
    elif operacao == "×":
        valor = n1 * n2
    elif operacao == "÷":
        if n2 == 0:
            messagebox.showwarning("Atenção", "Não é possível dividir por zero!")
            return
        valor = n1 / n2
    else:
        valor = n1 ** n2

    resultado.config(text=f"Resultado: {valor}")
    historico.config(text=f"Última conta: {n1} {operacao} {n2} = {valor}")

# Limpa os campos
def limpar():
    entrada_peso.delete(0, tk.END)
    entrada_numero2.delete(0, tk.END)
    resultado.config(text="Resultado:")
    historico.config(text="Última conta:")

# Janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x350")

tk.Label(janela, text="Número 1").pack()
entrada_peso = tk.Entry(janela)
entrada_peso.pack()

tk.Label(janela, text="Número 2").pack()
entrada_numero2 = tk.Entry(janela)
entrada_numero2.pack()

# Botões das operações
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

for simbolo in ["+", "-", "×", "÷", "**"]:
    tk.Button(
        frame_botoes,
        text=simbolo,
        command=lambda op=simbolo: calcular(op)
    ).pack(side="left", padx=3)

# Resultado e histórico
resultado = tk.Label(janela, text="Resultado:")
resultado.pack(pady=5)

historico = tk.Label(janela, text="Última conta:")
historico.pack()

tk.Button(janela, text="Limpar", command=limpar).pack(pady=10)

janela.mainloop()
