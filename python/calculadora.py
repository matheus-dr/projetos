from tkinter import *


class Aplicacao:
    root = Tk()
    valor_geral = StringVar()
    linha1 = ['7', '8', '9', '+']
    linha2 = ['4', '5', '6', '-']
    linha3 = ['1', '2', '3', '*']
    linha4 = ['0', 'C', '=', '/']

    def __init__(self):
        self.valor_geral.set('')
        f = Frame(self.root, padx=20, pady=20)
        self.screen = Entry(f, textvariable=self.valor_geral, font="Lucida 50 bold", bg="light blue")
        self.screen.pack(fill=X, padx=20, pady=15)
        f.pack()
        f = Frame(bg="grey", padx=30, pady=10)
        for i in self.linha1:
            b = Button(f, text=i, padx=10, pady=10, font="Lucida 25 bold")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        f.pack()
        f = Frame(bg="grey", padx=30, pady=10)
        for i in self.linha2:
            b = Button(f, text=i, padx=10, pady=10, font="Lucida 25 bold")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        f.pack()
        f = Frame(bg="grey", padx=30, pady=10)
        for i in self.linha3:
            b = Button(f, text=i, padx=10, pady=10, font="Lucida 25 bold")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        f.pack()
        f = Frame(bg="grey", padx=30, pady=10)
        for i in self.linha4:
            b = Button(f, text=i, padx=10, pady=10, font="Lucida 25 bold")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        f.pack()
        self.root.geometry("600x650")
        self.root.minsize()
        self.root.maxsize()
        self.root.config(bg="grey")
        self.root.title("Calculadora")

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
