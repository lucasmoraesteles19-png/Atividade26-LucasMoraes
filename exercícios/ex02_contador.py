import tkinter as tk
from tkinter import messagebox

contador = 0

def atualizar_tela():
    label_numero.config(text=str(contador))
    if contador >= 10:
        label_numero.config(fg="red")
    else:
        label_numero.config(fg="black")

def somar():
    global contador
    contador += 1
    atualizar_tela()
    if contador == 10:
        messagebox.showinfo("Parabéns!", "Você chegou a 10!")

def subtrair():
    global contador
    if contador > 0:
        contador -= 1
        atualizar_tela()

def zerar():
    global contador
    contador = 0
    atualizar_tela()

janela = tk.Tk()
janela.title("Contador")
janela.geometry("300x250")

label_numero = tk.Label(janela, text="0", font=("Arial", 60, "bold"), fg="black")
label_numero.pack(pady=20)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_menos = tk.Button(frame_botoes, text="-1", font=("Arial", 14), width=6, command=subtrair)
btn_menos.pack(side="left", padx=5)

btn_zerar = tk.Button(frame_botoes, text="Zerar", font=("Arial", 14), width=6, command=zerar)
btn_zerar.pack(side="left", padx=5)

btn_mais = tk.Button(frame_botoes, text="+1", font=("Arial", 14), width=6, command=somar)
btn_mais.pack(side="left", padx=5)

janela.mainloop()