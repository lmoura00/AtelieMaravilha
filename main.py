from tkinter.ttk import *
from tkinter import *
import datetime
import tkinter.messagebox
import os


cinza = "#2f2f2f"
gold = "#ffbc43"
preto = "#222"
hoje = str(datetime.date.today())
print(hoje)
dia = hoje[8:10]
mes = hoje[5:7]
global year
year = hoje[:4:]
tudo = f"{dia}/{mes}/{year}"
print(tudo)
janela = Tk()
janela.title("ATELIER MARAVILHA")
janela.geometry("800x400")
janela.configure(background=cinza)
janela.resizable(False, False)
titulo = Label(janela, text="ATELIER MARAVILHA", font="arial 20 underline bold", bg=cinza, fg=gold)
titulo.place(x=250, y=30)
diaHj = Label(janela, text=tudo, font="arial 10 bold", bg=cinza, fg=gold)
diaHj.place(x=350, y=70)

image1 = PhotoImage(file="bg.png")
localImage1 = Label(janela, image=image1, height=100, width=100, bg=cinza, fg=gold)
localImage1.place(x=90, y=5, width=100, height=100)

image2 = PhotoImage(file="bg2.png")
localImage1 = Label(janela, image=image2, height=100, width=100, bg=cinza)
localImage1.place(x=600, y=5, width=100, height=100)

def cadastrar():
    janelaCad = Toplevel(janela)
    janelaCad.title("CADASTRAR CLIENTE")
    janelaCad.geometry("400x400")
    janelaCad.resizable(False, False)
    janelaCad.configure(background=cinza)
    tituloCad = Label(janelaCad, text="CADASTRAR CLIENTE", font="arial 15 underline bold", bg=cinza, fg=gold)
    tituloCad.place(x=100, y=1)

    nomeCliente = Label(janelaCad, text="NOME: ", font="arial 14 bold", bg=cinza, fg=gold)
    nomeCliente.place(x=1, y=30)
    nomeClienteInput = Entry(janelaCad, font="arial 14", bg="#b9b9b9", fg=preto)
    nomeClienteInput.place(x=150, y=30)

    nascimentoCliente = Label(janelaCad, text="NASCIMENTO: ", font="arial 14 bold", bg=cinza, fg=gold)
    nascimentoCliente.place(x=1, y=60)
    nascimentoClienteInput = Entry(janelaCad, font="arial 14", bg="#b9b9b9", fg=preto)
    nascimentoClienteInput.place(x=150, y=60)

    def salvar():
        dadosCliente = []
        arquivo = open("CadClientes", "a")
        arquivo.write("------------------------")
        arquivo.write("\n")
        arquivo.write("NOME: ")
        dadosCliente.append(nomeClienteInput.get())
        arquivo.writelines(dadosCliente)
        arquivo.write("\n")
        dadosCliente.clear()
        arquivo.write("NASCIMENTO: ")
        dadosCliente.append(nascimentoClienteInput.get())
        arquivo.writelines(dadosCliente)
        arquivo.write("\n")
        dadosCliente.clear()
        nascimentoClienteTodo = str(nascimentoClienteInput.get())
        anoNascimento = nascimentoClienteTodo[6:10:1]
        idade = int(year) - int(anoNascimento)
        arquivo.write("IDADE: ")
        arquivo.write(str(idade))
        arquivo.write(" anos")
        arquivo.write("\n")
        arquivo.close()
        tkinter.messagebox.showinfo(title="AVISO", message="Cliente cadastrado com sucesso.")
        janelaCad.destroy()
    def teste():
        if (nomeClienteInput.get() == "") or (nascimentoClienteInput.get() == ""):
            tkinter.messagebox.showinfo(title="AVISO", message="Preencha com as informações requeridas.")
        else:
            salvar()
    botaoSalvar = Button(janelaCad, text="SALVAR", font="arial 14 bold", bg="green", fg="white", command=teste)
    botaoSalvar.place(x=300, y=350)

    janelaCad.mainloop()

def lerArq():
    if os.path.exists("CadClientes"):
        janela3 = Toplevel(janela)
        janela3.title("CADASTRADOS")
        janela3.geometry("200x400")
        janela3.configure(background=preto)
        janela3.resizable(False, False)

        list = Listbox(janela3, bg=cinza, fg=gold)
        list.place(x=1, y=1, height=400, width=200)
        with open("CadClientes", "r") as arquivo:
            for dado in arquivo:
                list.insert(END, dado)
        arquivo.close()
    else:
        tkinter.messagebox.showinfo(title="AVISO", message="O arquivo não existe.")
def cadServicos():
    dados = []
    arquivo = open("CadClientes", "r")
    for dado in arquivo:
        dados.append(dado)
    arquivo.close()
    print(dados)
    janela4 =Toplevel(janela)
    janela4.title("CADASTRAR SERVIÇOS")
    janela4.resizable(False, False)
    titulo = Label(janela4,text="CADASTRAR SERVIÇOS")
    janela4.mainloop()
def apagarCad():
    if os.path.exists("CadClientes"):
        janela5 = Toplevel(janela)
        janela5.title("Tem certeza?")
        janela5.geometry("200x50")
        janela5.configure(background=preto)
        janela5.resizable(False, False)
        def apagar():
            os.remove("CadClientes")
            tkinter.messagebox.showinfo(title="AVISO", message="O arquivo foi apagado.")
            janela5.destroy()
        buttonConfirma = Button(janela5, text="APAGAR", bg="green", fg="white", command=apagar)
        buttonConfirma.place(x=20, y=20)
        buttonSair = Button(janela5, text="CANCELAR", bg="red", fg="white", command=janela5.destroy)
        buttonSair.place(x=110, y=20)
        janela5.mainloop()
    else:
        tkinter.messagebox.showinfo(title="AVISO", message="O arquivo não existe.")
linha = Label(janela, text="----------------------------------------------------------------------------------------", font="arial 20", bg="#2f2f2f", fg="#ffbc43")
linha.place(x=2, y=90)

botao1 = Button(janela, text="CADASTRAR", font="arial 15 underline", bg=gold, fg=preto, width=20, command=cadastrar)
botao1.place(x=120, y=150)

botao2 = Button(janela, text="CADASTRAR SERVIÇOS", font="arial 15 underline", bg=gold, fg=preto, width=20, command=cadServicos)
botao2.place(x=120, y=200)

botao3 = Button(janela, text="FECHAR COMPRA", font="arial 15 underline", bg=gold, fg=preto, width=20)
botao3.place(x=120, y=250)

botao4 = Button(janela, text="LISTAR DADOS", font="arial 15 underline", bg=gold, fg=preto, width=20, command=lerArq)
botao4.place(x=400, y=150)

botao5 = Button(janela, text="APAGAR CADASTROS", font="arial 15 underline", bg=gold, fg=preto, width=20, command=apagarCad)
botao5.place(x=400, y=200)

botaoSair = Button(janela, text="SAIR", font="arial 15 underline", bg="red", fg="#fff", width=10, command=janela.destroy)
botaoSair.place(x=650, y=350)
janela.mainloop()
