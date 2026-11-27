
import tkinter as tk
from tkinter import messagebox

# Função para converter Celsius em Fahrenheit
def converter():
    try:
        celsius = float(entrada.get().replace(",", "."))
        fahrenheit = celsius * 9 / 5 + 32

        resultado.config(
            text=f"{celsius:.1f} °C = {fahrenheit:.1f} °F"
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite uma temperatura válida!")

# Função para converter Fahrenheit em Celsius
def converter_inverso():
    try:
        fahrenheit = float(entrada.get().replace(",", "."))
        celsius = (fahrenheit - 32) * 5 / 9

        resultado.config(
            text=f"{fahrenheit:.1f} °F = {celsius:.1f} °C"
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite uma temperatura válida!")

# Função para limpar
def limpar():
    entrada.delete(0, tk.END)
    resultado.config(text="")

# Criar janela
janela = tk.Tk()
janela.title("Conversor de Temperatura")
janela.geometry("380x220")
janela.resizable(False, False)

# Label Celsius
tk.Label(
    janela,
    text="Temperatura:"
).grid(row=0, column=0, padx=10, pady=15)

# Campo de entrada
entrada = tk.Entry(janela)
entrada.grid(row=0, column=1, padx=10)

# Botão converter
tk.Button(
    janela,
    text="Converter",
    command=converter
).grid(row=1, column=0, pady=10)

# Botão Fahrenheit para Celsius
tk.Button(
    janela,
    text="Fahrenheit para Celsius",
    command=converter_inverso
).grid(row=1, column=1)

# Botão limpar
tk.Button(
    janela,
    text="Limpar",
    command=limpar
).grid(row=2, column=0, columnspan=2, pady=5)

# Label do resultado
resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 12)
)
resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Executar janela
janela.mainloop()
