
import tkinter as tk

# Função para atualizar a aparência
def atualizar():
    cor = cor_var.get()
    tamanho = tamanho_var.get()

    # Altera o fundo da janela
    janela.config(bg=cor)

    # Altera o fundo e a fonte do texto
    estilo = "bold" if negrito_var.get() else "normal"

    texto.config(
        bg=cor,
        font=("Arial", tamanho, estilo)
    )

    # Atualiza o Label com as escolhas
    escolha.config(
        text=f"Cor: {cor} · Letra: {tamanho}"
    )


# Função para restaurar os valores iniciais
def restaurar():
    cor_var.set("lightblue")
    tamanho_var.set(16)
    negrito_var.set(False)
    atualizar()


# Criação da janela
janela = tk.Tk()
janela.title("Mudando o visual da janela")
janela.geometry("400x450")
janela.config(bg="lightblue")

# Variáveis de controle
cor_var = tk.StringVar(value="lightblue")
tamanho_var = tk.IntVar(value=16)
negrito_var = tk.BooleanVar(value=False)

# Label de exemplo
texto = tk.Label(
    janela,
    text="Este é o meu texto",
    bg="lightblue",
    font=("Arial", 16)
)
texto.pack(pady=15)

# Grupo de cores
tk.Label(
    janela,
    text="Escolha a cor de fundo:",
    bg="lightblue"
).pack()

cores = [
    ("Azul claro", "lightblue"),
    ("Verde claro", "lightgreen"),
    ("Amarelo", "lightyellow"),
    ("Rosa", "pink")
]

for nome, valor in cores:
    tk.Radiobutton(
        janela,
        text=nome,
        variable=cor_var,
        value=valor,
        command=atualizar,
        bg="lightblue"
    ).pack()

# Grupo de tamanhos
tk.Label(
    janela,
    text="Escolha o tamanho da letra:",
    bg="lightblue"
).pack(pady=5)

tamanhos = [
    ("Pequena (12)", 12),
    ("Média (16)", 16),
    ("Grande (22)", 22)
]

for nome, valor in tamanhos:
    tk.Radiobutton(
        janela,
        text=nome,
        variable=tamanho_var,
        value=valor,
        command=atualizar,
        bg="lightblue"
    ).pack()

# Checkbutton Negrito
tk.Checkbutton(
    janela,
    text="Negrito",
    variable=negrito_var,
    command=atualizar,
    bg="lightblue"
).pack(pady=8)

# Label que mostra as escolhas atuais
escolha = tk.Label(
    janela,
    text="Cor: lightblue · Letra: 16",
    bg="lightblue"
)
escolha.pack(pady=10)

# Botão Restaurar
tk.Button(
    janela,
    text="Restaurar",
    command=restaurar
).pack(pady=10)

# Mantém a janela aberta
janela.mainloop()
