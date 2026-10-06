import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter


# ============================================================
# JANELA PRINCIPAL
# ============================================================

janela = tk.Tk()

janela.title("Calculadora de chapas")
janela.geometry("700x500")
janela.minsize(450, 350)

# A janela fica 100% visível.
# A transparência será aplicada somente visualmente à imagem.
janela.attributes("-alpha", 1.0)

janela.configure(bg="#E9EEF5")


# ============================================================
# IMAGEM DE FUNDO
# ============================================================

# A imagem precisa estar na mesma pasta do arquivo .py
imagem_original = Image.open("grunge-wall-texture.jpg").convert("RGB")


def criar_imagem_fundo(largura, altura):

    # Evita erro caso a janela fique muito pequena
    if largura < 1 or altura < 1:
        return None

    # Redimensiona a imagem conforme o tamanho atual da janela
    imagem = imagem_original.resize(
        (largura, altura),
        Image.Resampling.LANCZOS
    )

    # Aplica desfoque
    imagem = imagem.filter(
        ImageFilter.GaussianBlur(7)
    )

    # Cria uma camada clara
    camada = Image.new(
        "RGB",
        imagem.size,
        "#F1F5F9"
    )

    # Mistura a foto com a camada clara
    # Quanto maior, mais suave/apagada fica a foto
    imagem = Image.blend(
        imagem,
        camada,
        0.68
    )

    return ImageTk.PhotoImage(imagem)


# Cria fundo inicial
imagem_fundo = criar_imagem_fundo(700, 500)

fundo = tk.Label(
    janela,
    image=imagem_fundo,
    borderwidth=0
)

fundo.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)


# ============================================================
# CONFIGURAÇÃO DO GRID
# ============================================================

# Colunas
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=2)
janela.columnconfigure(2, weight=1)

# Linhas
janela.rowconfigure(0, weight=1)
janela.rowconfigure(9, weight=1)


# ============================================================
# TÍTULO
# ============================================================

titulo = tk.Label(
    janela,
    text="Calculadora de Peso de Chapa",
    font=("Segoe UI", 20, "bold"),
    bg="#F1F5F9",
    fg="#1E293B"
)

titulo.grid(
    row=1,
    column=1,
    pady=(0, 20)
)


# ============================================================
# CAMPO LARGURA
# ============================================================

label_largura = tk.Label(
    janela,
    text="Digite a largura:",
    font=("Segoe UI", 10),
    bg="#F1F5F9",
    fg="#334155"
)

label_largura.grid(
    row=2,
    column=1,
    sticky="w",
    padx=30,
    pady=(0, 5)
)


entrada_largura = tk.Entry(
    janela,
    font=("Segoe UI", 12),
    bg="#F8FAFC",
    fg="#1E293B",
    justify="center",
    bd=0,
    highlightthickness=1,
    highlightbackground="#CBD5E1",
    highlightcolor="#2563EB"
)

entrada_largura.grid(
    row=3,
    column=1,
    sticky="ew",
    padx=30,
    pady=(0, 12),
    ipady=7
)


# ============================================================
# CAMPO COMPRIMENTO
# ============================================================

label_comprimento = tk.Label(
    janela,
    text="Digite o comprimento:",
    font=("Segoe UI", 10),
    bg="#F1F5F9",
    fg="#334155"
)

label_comprimento.grid(
    row=4,
    column=1,
    sticky="w",
    padx=30,
    pady=(0, 5)
)


entrada_comprimento = tk.Entry(
    janela,
    font=("Segoe UI", 12),
    bg="#F8FAFC",
    fg="#1E293B",
    justify="center",
    bd=0,
    highlightthickness=1,
    highlightbackground="#CBD5E1",
    highlightcolor="#2563EB"
)

entrada_comprimento.grid(
    row=5,
    column=1,
    sticky="ew",
    padx=30,
    pady=(0, 12),
    ipady=7
)


# ============================================================
# CAMPO ESPESSURA
# ============================================================

label_espessura = tk.Label(
    janela,
    text="Digite a espessura:",
    font=("Segoe UI", 10),
    bg="#F1F5F9",
    fg="#334155"
)

label_espessura.grid(
    row=6,
    column=1,
    sticky="w",
    padx=30,
    pady=(0, 5)
)


entrada_espessura = tk.Entry(
    janela,
    font=("Segoe UI", 12),
    bg="#F8FAFC",
    fg="#1E293B",
    justify="center",
    bd=0,
    highlightthickness=1,
    highlightbackground="#CBD5E1",
    highlightcolor="#2563EB"
)

entrada_espessura.grid(
    row=7,
    column=1,
    sticky="ew",
    padx=30,
    pady=(0, 15),
    ipady=7
)


# ============================================================
# RESULTADO
# ============================================================

label_resultado = tk.Label(
    janela,
    text="Peso da chapa: -- kg",
    font=("Segoe UI", 16, "bold"),
    bg="#F1F5F9",
    fg="#1E293B"
)


# ============================================================
# FUNÇÃO CALCULAR
# ============================================================

def calcular():

    try:

        # .replace permite digitar 6,30 ou 6.30
        largura = float(
            entrada_largura.get().replace(",", ".")
        )

        comprimento = float(
            entrada_comprimento.get().replace(",", ".")
        )

        espessura = float(
            entrada_espessura.get().replace(",", ".")
        )

        # Cálculo do peso da chapa
        peso = (
            largura
            * comprimento
            * espessura
            * 0.00000785
        )

        label_resultado.config(
            text=f"Peso da chapa: {peso:.2f} kg"
        )

    except ValueError:

        messagebox.showerror(
            "Valor inválido",
            "Digite somente valores numéricos."
        )


# ============================================================
# BOTÃO CALCULAR
# ============================================================

botao_calcular = tk.Button(
    janela,
    text="Calcular",
    command=calcular,
    font=("Segoe UI", 11, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    bd=0,
    cursor="hand2"
)

botao_calcular.grid(
    row=8,
    column=1,
    pady=(5, 10),
    ipadx=30,
    ipady=7
)


# Resultado fica abaixo do botão
label_resultado.grid(
    row=9,
    column=1,
    pady=(5, 20)
)


# ============================================================
# ENTER PARA TROCAR DE CAMPO
# ============================================================

entrada_largura.bind(
    "<Return>",
    lambda event: entrada_comprimento.focus_set()
)

entrada_comprimento.bind(
    "<Return>",
    lambda event: entrada_espessura.focus_set()
)

entrada_espessura.bind(
    "<Return>",
    lambda event: calcular()
)


# ============================================================
# RESPONSIVIDADE DA IMAGEM
# ============================================================

def redimensionar_fundo(event):

    # Só queremos responder ao redimensionamento da janela
    if event.widget != janela:
        return

    nova_imagem = criar_imagem_fundo(
        event.width,
        event.height
    )

    if nova_imagem is not None:

        fundo.config(
            image=nova_imagem
        )

        # Importante:
        # mantém referência da imagem na memória
        fundo.image = nova_imagem


janela.bind(
    "<Configure>",
    redimensionar_fundo
)


# ============================================================
# COLOCA FUNDO ATRÁS DOS COMPONENTES
# ============================================================

fundo.lower()


# ============================================================
# CURSOR COMEÇA NA LARGURA
# ============================================================

entrada_largura.focus_set()


# ============================================================
# INICIAR PROGRAMA
# ============================================================

janela.mainloop()