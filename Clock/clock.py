# Mostra a hora atual atualizada a cada segundo

import tkinter as tk
import time

def mostrar_hora():
    hora_atual = time.strftime("%H:%M:%S")
    label_hora.config(text=hora_atual)
    janela.after(1000, mostrar_hora)  # Atualiza a cada segundo

janela = tk.Tk()
janela.geometry("300x100")  # Tamanho da janela

label_hora = tk.Label(janela, text="", font=("Arial", 24))
label_hora.pack(expand=True)

mostrar_hora()

janela.mainloop()
