import sqlite3
import tkinter
from tkinter import Frame
from tkinter import Button
from tkinter import Entry

root = tkinter.Tk()
class aplicacao():
    def __init__(self):
        self.root = root
        self.base()
        self.botoes()
        self.root.mainloop()
    def base(self):
        self.root.title("Cadastro")
        self.root.geometry("800x700")
        self.root.minsize(width=500, height=400)
        self.frame1 = Frame(self.root, bg="#998d8d", bd=1)
        self.frame1.place(relx=0, rely=0, relheight=1, relwidth=1)
    def botoes(self):
        botaoenviar = Button(self.frame1, text="Enviar!", command=self.enviar, bg="#ffffff")
        botaoenviar.place(relx=0.05, rely=0.03, height=0.1, width=0.2)
    def enviar(self):
        print("enviado")
aplicacao()