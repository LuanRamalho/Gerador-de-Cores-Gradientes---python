import tkinter as tk
from random import randint

def gerar_cor_aleatoria():
    """Gera uma cor aleatória no formato hexadecimal."""
    return f'#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}'

def criar_gradiente(canvas, cor1, cor2):
    """Cria um gradiente vertical entre duas cores."""
    largura = canvas.winfo_width()
    altura = canvas.winfo_height()
    
    # Gerar as cores intermediárias para o gradiente
    for i in range(altura):
        r = int(cor1[1:3], 16) + (int(cor2[1:3], 16) - int(cor1[1:3], 16)) * i // altura
        g = int(cor1[3:5], 16) + (int(cor2[3:5], 16) - int(cor1[3:5], 16)) * i // altura
        b = int(cor1[5:], 16) + (int(cor2[5:], 16) - int(cor1[5:], 16)) * i // altura
        cor_intermediaria = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, largura, i, fill=cor_intermediaria)

def atualizar_gradiente():
    """Atualiza o gradiente com novas cores aleatórias."""
    cor_inicial = gerar_cor_aleatoria()
    cor_final = gerar_cor_aleatoria()
    criar_gradiente(canvas, cor_inicial, cor_final)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Gradiente de Cores Aleatórias")

# Definindo o canvas para exibir o gradiente
canvas = tk.Canvas(janela, width=400, height=300)
canvas.pack()

# Botão para gerar um novo gradiente
botao = tk.Button(janela, text="Gerar Gradiente Aleatório", command=atualizar_gradiente)
botao.pack()

# Inicia com um gradiente
atualizar_gradiente()

# Executa a interface Tkinter
janela.mainloop()
