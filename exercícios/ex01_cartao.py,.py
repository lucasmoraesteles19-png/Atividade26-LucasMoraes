import tkinter as tk

#criar a Janela
janela = tk.Tk()
janela.title("Cartao de Visita")
janela.geometry("360x200")
janela.resizable(False, False)


janela.configurebg=("#93B5F0")

#faixa amarela no topo da janela
faixa = tk.Frame(janela, bg="#FFD700", height=45)
faixa.pack(fill="x")

#criar um texto do nome
nome = tk.Label(
    janela, 
    text="Lucas Moraes",
    font=("Arial", 18, "bold"),
    fg="#263B70", 
    bg= "#E8F0FE"
)
nome.place(relx=0.5, y=65, anchor="center")

#criar o texto sobre o curso
curso = tk.Label(
    janela,
    text="Curso: Informática",
    font=("Arial", 12),
    fg="#16803C",
    bg="#E8F0FE"
)
curso.place(relx=0.5, y=110, anchor="center")

#cria um texto sobre a escola
escola = tk.Label(
    janela,
    text="ETEC Alberto Santos Dumont",
    font=("Arial", 10),
    fg="#B04A30",
    bg="#E8F0FE"
)
escola.place(relx=0.5, y=140, anchor="center")

#botao fechar
botao = tk.Button(
    janela,
    text="Fechar",
    command=janela.destroy
)
botao.place(x=155, y=170)

# executar a janela
janela.mainloop()
