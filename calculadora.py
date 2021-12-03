from tkinter import *
from os import remove


class Aplicacao:
    def __init__(self):
        root = Tk()
        self.valor1 = DoubleVar(root)
        self.valor2 = DoubleVar(root)
        self.txt1 = Label(text="Valor 1: ").grid(column=1, row=1)
        self.entrada1 = Entry(textvar=self.valor1).grid(column=2, row=1)
        self.txt2 = Label(text="Valor 2: ").grid(column=1, row=2)
        self.entrada2 = Entry(textvar=self.valor2).grid(column=2, row=2)
        self.botao_soma = Button(text='+', command=self.soma).grid(column=1, row=3)
        self.botao_subtracao = Button(text='-', command=self.subtracao).grid(column=2, row=3)
        self.botao_multiplicacao = Button(text='*', command=self.multiplicacao).grid(column=3, row=3)
        self.botao_divisao = Button(text='/', command=self.divisao).grid(column=4, row=3)
        self.botao_armazenamento = Button(text='M', command=self.armazenagem).grid(column=5, row=3)
        self.resultado = Label(text="= ")
        self.resultado.grid(column=2, row=4)
        self.botao_limpar = Button(text="Limpar", command=self.limpar).grid(column=2, row=5)
        self.botao_leitura = Button(text='C', command=self.leitura).grid(column=1, row=5)

    def soma(self):
        soma = self.valor1.get() + self.valor2.get()
        self.resultado.configure(text=f"= {soma}")

    def subtracao(self):
        subtracao = self.valor1.get() - self.valor2.get()
        self.resultado.configure(text=f"= {subtracao}")

    def multiplicacao(self):
        multiplicacao = self.valor1.get() * self.valor2.get()
        self.resultado.configure(text=f"= {multiplicacao}")

    def divisao(self):
        divisao = self.valor1.get() / self.valor2.get()
        self.resultado.configure(text=f"= {divisao}")

    def armazenagem(self):
        with open("valores.txt", 'w') as file:
            file.write(f"{self.valor1.get()};{self.valor2.get()}")
            file.close()

    def limpar(self):
        self.valor1.set('')
        self.valor2.set('')
        self.resultado.configure(text="= ")

    def leitura(self):
        try:
            with open("valores.txt", 'r') as file:
                conteudo = file.read()
                lista = conteudo.split(';')
                self.valor1.set(lista[0])
                self.valor2.set(lista[1])
                file.close()
        except:
            self.resultado.configure(text="Não há valores\narmazenados")


app = Aplicacao()
mainloop()
try:
    remove("valores.txt")
except:
    pass
