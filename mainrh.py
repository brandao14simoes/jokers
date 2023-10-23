# Teste de RH
# Import bibliotecas
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as ttk
import database

# Crie uma interface gráfica para o usuário.
root = Tk()
root.title('Login Acess Painel') # Título da janela
root.geometry('700x400')
root.configure(background = 'Gray')
root.resizable(width=False, height=False)
#root.attributes("-alpha", 0.9)

# Crie um rótulo para o nome do funcionário.
nomeLabel = ttk.Label(root, text="Nome:")
nomeLabel.place(x=10, y=10)

# Crie uma caixa de texto para o nome do funcionário.
NomeEntry = ttk.Entry(root)
NomeEntry.place(x=10, y=40)

# Crie um rótulo para o sobrenome do funcionário.
sobrenomeLabel = ttk.Label(root, text="Sobrenome:")
sobrenomeLabel.place(x=300, y=9)

# Crie uma caixa de texto para o sobrenome do funcionário.
sobrenomeEntry = ttk.Entry(root)
sobrenomeEntry.place(x=300, y=35)

# Crie um rótulo para o e-mail do funcionário.
emailLabel= ttk.Label(root, text=" E-mail:")
emailLabel.place(x=10, y=110)

# Crie uma caixa de texto para o e-mail do funcionário.
emailEntry = ttk.Entry(root)
emailEntry.place(x=10, y=140)

# Crie um rótulo para o telefone do funcionário.
telefoneLabel = ttk.Label(root, text="Telefone:")
telefoneLabel.place(x=10, y=170)

# Crie uma caixa de texto para o telefone do funcionário.
telefoneEntry = ttk.Entry(root)
telefoneEntry.place(x=10, y=200)

# Crie um rótulo para o cargo do funcionário.
cargoLabel = ttk.Label(root, text="Cargo:")
cargoLabel.place(x=10, y=230)

# Crie uma caixa de texto para o cargo do funcionário.
cargoEntry = ttk.Entry(root)
cargoEntry.place(x=10, y=260)

# Crie um rótulo para o salário do funcionário.
salarioLabel = ttk.Label(root, text="Salário:")
salarioLabel.place(x=10, y=290)

# Crie uma caixa de texto para o salário do funcionário.
salarioEntry = ttk.Entry(root)
salarioEntry.place(x=10, y=320)

# Função para salvar os dados do funcionário.
def salvar_funcionario():
  nome = NomeEntry.get()
  sobrenome = sobrenomeEntry.get()
  email = emailEntry.get()
  telefone = telefoneEntry.get()
  cargo = cargoEntry.get()
  salario = salarioEntry.get()

  # Insira os dados do funcionário no banco de dados.
  mycursor = mydb.cursor()
  mycursor.execute("INSERT INTO funcionarios (nome, sobrenome, email, telefone, cargo, salario) VALUES (?, ?, ?, ?, ?, ?)", (nome, sobrenome, email, telefone, cargo, salario))

  mydb.commit()
  
  # Exiba uma mensagem de confirmação.
  messagebox.showinfo(title="Sucesso",message="Dados incluídos com sucesso no banco de dados.")


# Crie um botão para salvar os dados do funcionário.
button_salvar = ttk.Button(root, text="Salvar", command=salvar_funcionario)
button_salvar.place(x=10, y=360)

# Inicie o loop principal da GUI.
root.mainloop()
