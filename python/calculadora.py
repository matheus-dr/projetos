from tkinter import *


class Aplicacao:
    def __init__(self):
        self.janela = Tk()
        self.valor_geral = StringVar()
        self.valor_geral.set('')
        self.f = Frame(self.janela, padx=20, pady=20)
        self.screen = Entry(self.f, textvar=self.valor_geral, font="Lucida 50 bold", bg="light blue")
        self.screen.pack(fill=X, padx=20, pady=15)
        self.f.pack()
        self.linha1 = ['7', '8', '9', '+']
        self.linha2 = ['4', '5', '6', '-']
        self.linha3 = ['1', '2', '3', '*']
        self.linha4 = ['0', 'C', '=', '/']
        self.f = Frame(bg="grey", padx=30, pady=10)
        for i in self.linha1:
            b = Button(self.f, text=i, padx=10, pady=10, font="Lucida 25 bold")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        self.f.pack()
        self.f = Frame(bg="grey", padx=30, pady=10)
        for i in self.linha2:
            b = Button(self.f, text=i, padx=10, pady=10, font="Lucida 25 bold")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        self.f.pack()
        self.f = Frame(bg="grey", padx=30, pady=10)
        for i in self.linha3:
            b = Button(self.f, text=i, padx=10, pady=10, font="Lucida 25 bold")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        self.f.pack()
        self.f = Frame(bg="grey", padx=30, pady=10)
        for i in self.linha4:
            b = Button(self.f, text=i, padx=10, pady=10, font="Lucida 25 bold")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        self.f.pack()
        self.janela.geometry("600x650")
        self.janela.minsize()
        self.janela.maxsize()
        self.janela.config(bg="grey")
        self.janela.title("Calculadora")

    def click(self, event):
        entrada = event.widget.cget("text")
        try:
            if entrada == '=':
                valor = eval(self.screen.get())
                self.valor_geral.set(valor)
                self.screen.update()
            elif entrada == 'C':
                self.valor_geral.set('')
                self.screen.update()
            else:
                self.valor_geral.set(self.valor_geral.get() + entrada)
                self.screen.update()
        except ZeroDivisionError:
            self.valor_geral.set("Erro: n/0")
            self.screen.update()
        except SyntaxError:
            self.valor_geral.set("Erro: Sintaxe")
            self.screen.update()


app = Aplicacao()
mainloop()
