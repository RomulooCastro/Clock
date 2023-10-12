#MagicClock

# Mostra e oculta a hora atual na sua tela
# de acordo com o time que você decidir

import tkinter as tk
import time

def mostrar_hora():
    hora_atual = time.strftime("%H:%M:%S")
    label_hora.config(text=hora_atual)
    janela.after(5000, ocultar_janela) # Time para ocultar a janela em milésimos

def ocultar_janela():
    janela.withdraw()
    janela.after(5000, mostrar_janela) # Time para mostrar a janela em milésimos

def mostrar_janela():
    janela.deiconify()
    mostrar_hora()

janela = tk.Tk()
janela.geometry("400x100")  # Tamanho da janela

label_hora = tk.Label(janela, text="", font=("Arial", 24))
label_hora.pack(expand=True)

mostrar_janela()

janela.mainloop()
