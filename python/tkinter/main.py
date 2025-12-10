import tkinter
from tkinter import Frame
from tkinter import Button

root = tkinter.Tk()

class app():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.botoes()
        self.root.mainloop()
    def tela(self):
        self.root.title("Nosso Software")
        self.root.geometry("800x600") 
        self.root.minsize(width=500, height=250)
    def frames(self):
        self.frame1 = Frame(self.root, bg="#000000", bd=4)
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
    def botoes(self):
        self.botao1 = Button(self.frame1, text="Botão", command=None, bg="#ffffff")
        self.botao1.place(relx=0.03, rely=0.05, relheight=0.01, relwidth=0.01)
app()