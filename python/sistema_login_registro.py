from tkinter import *
import sqlite3
from tkinter import messagebox


class Aplicacao:
    con = sqlite3.connect("dados_usuario.db")
    cur = con.cursor()
    root = Tk()
    nome = StringVar()
    nome_usuario = StringVar()
    senha = StringVar()
    email = StringVar()
    nome_usuario_login = StringVar()
    senha_login = StringVar()
    senha_temp = StringVar()
    root.geometry("500x450")
    root.title("Sistema de Login Básico")
    root.resizable(False, False)

    def __init__(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS registros(
                                nome text,
                                nome_usuario text,
                                senha text,
                                email text
                                )''')
        self.con.commit()

    def inserir_registro(self):
        contador, aviso = 0, ''
        if self.nome.get().strip() == '':
            aviso = "Nome não pode estar vazio"
        else:
            contador += 1
        if self.nome_usuario.get().strip() == '':
            aviso = "Nome de usuário não pode estar vazio"
        else:
            contador += 1
        if self.senha.get().strip() == '':
            aviso = "Senha não pode estar vazia"
        else:
            contador += 1
        if self.senha.get().strip() == '':
            aviso = "Email não pode estar vazio"
        else:
            contador += 1
        if contador == 4:
            try:
                self.cur.execute("INSERT INTO registros VALUES (:nome, :nome_usuario, :senha, :email)",
                                 {"nome": self.nome.get(), "nome_usuario": self.nome_usuario.get(),
                                  "senha": self.senha.get(), "email": self.email.get()})
                self.con.commit()
            except Exception as ex:
                messagebox.showerror('', str(ex))
        else:
            messagebox.showerror("Erro", aviso)

    def resposta_login(self):
        username, password, aviso = '', '', ''
        try:
            for linha in self.cur.execute("SELECT * FROM registros"):
                username = linha[1]
                password = linha[2]
        except Exception as ex:
            messagebox.showerror('', str(ex))
        contador = 0
        if self.nome_usuario_login.get().strip() == '':
            aviso = "Nome de usuário não pode estar vazio"
        else:
            contador += 1
        if self.senha_login.get().strip() == '':
            aviso = "Senha não pode estar vazia"
        else:
            contador += 1
        if contador == 2:
            if username == self.nome_usuario_login.get() and password == self.senha_login.get():
                messagebox.showinfo("Status do login", "Login OK")
            else:
                messagebox.showerror("Status do login", "Nome ou senha inválidos")
        else:
            messagebox.showerror('', aviso)

    def login(self):
        f = Frame(self.root, height=450, width=500, bg="#FFBA41")
        Label(f, text="Login", font="Helvetica 30 bold", bg="#FFBA41").place(x=200, y=120)
        Label(f, text="Preencha todos os campos do formulário", font="Helvetica 12 bold", fg="#666A6C", bg="#FFBA41")\
            .place(x=100, y=170)
        Label(f, text="Nome de Usuário", font="Helvetica 12 bold", fg="#4C4A49", bg="#FFBA41").place(x=150, y=200)
        Entry(f, textvariable=self.nome_usuario_login, font="calibre 10 normal", width=30).place(x=150, y=220)
        Label(f, text="Senha", font="Helvetica 12 bold", fg="#4C4A49", bg="#FFBA41").place(x=150, y=250)
        Entry(f, textvariable=self.senha_login, font="calibre 10 normal", width=30, show='*').place(x=150, y=270)
        Button(f, text="Login", font="Helvetica 15 bold", bg="#00B6FF", command=self.resposta_login).place(x=220, y=300)
        Label(text="Não possuo uma conta", font="Helvetica 12 bold", fg="#666A6C", bg="#FFBA41").place(x=110, y=350)
        Button(text="Registre-se aqui", font="Helvetica 8 bold", bg="#FFBA41", command=self.registro)\
            .place(x=320, y=350)
        f.place(x=0, y=0)

    def registro(self):
        f = Frame(self.root, height=450, width=500, bg="#FFBA41")
        Label(f, text="Registro", font="Helvetica 30 bold", bg="#FFBA41").place(x=140, y=60)
        Label(f, text="Nome completo", font="Helvetica 12 bold", fg="#4C4A49", bg="#FFBA41").place(x=150, y=120)
        Entry(f, textvariable=self.nome, font="calibre 10 normal", width=30).place(x=150, y=140)
        Label(f, text="Nome de Usuário", font="Helvetica 12 bold", fg="#4C4A49", bg="#FFBA41").place(x=150, y=170)
        Entry(f, textvariable=self.nome_usuario, font="calibre 10 normal", width=30).place(x=150, y=190)
        Label(f, text="Email", font="Helvetica 12 bold", fg="#4C4A49", bg="#FFBA41").place(x=150, y=220)
        Entry(f, textvariable=self.email, font="calibre 10 normal", width=30).place(x=150, y=240)
        Label(f, text="Senha", font="Helvetica 12 bold", fg="#4C4A49", bg="#FFBA41").place(x=150, y=270)
        Entry(f, textvariable=self.senha, font="calibre 10 normal", width=30, show='*').place(x=150, y=290)
        Button(f, text="Registrar-se", font="Helvetica 15 bold", bg="#00B6FF", command=self.inserir_registro)\
            .place(x=200, y=330)
        Label(f, text="Já possuo uma conta", font="Helvetica 12 bold", fg="#666A6C", bg="#FFBA41").place(x=120, y=380)
        Button(f, text="Login", font="Helvetica 8 bold", bg="#FFBA41", command=self.login).place(x=300, y=380)
        f.place(x=0, y=0)


app = Aplicacao()
app.login()

mainloop()
