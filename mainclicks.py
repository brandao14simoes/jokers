import tkinter as tk

root = tk.Tk()  # Corrigido: 'tk.TK()' para 'tk.Tk()'
root.geometry('500x500')
root.title('Contador de Clicks')
root.configure(background='#1d1d1d')

numero = 0

def acrescentar():
    global numero
    numero = numero + 1
    contagem_click.configure(text=numero)  # Corrigido: 'contagem_clicks' para 'contagem_click'

def diminuir():
    global numero
    numero = numero - 1
    contagem_click.configure(text=numero)

margem = tk.Canvas(root, height=200, background='#1d1d1d',
                   bd=0, highlightthickness=0, relief='flat')  # Corrigidos os erros de atribuição

margem.pack()

botao_acrescentar = tk.Button(root, bg='#FFFFFF', text='+', font=('Montserrat', 16, 'bold'), padx=10, command=acrescentar)  # Corrigidos os erros de formatação e atribuição
botao_acrescentar.pack()

contagem_click = tk.Label(root, text=numero, fg='#FFFFFF', bg='#1d1d1d', font=('Montserrat', 16))
contagem_click.pack()

botao_diminuir = tk.Button(root, bg='#FFFFFF', text='-', font=('Montserrat', 16, 'bold'), padx=10, command=diminuir) # Corrigidos os erros de formatação e atribuição
botao_diminuir.pack()

root.mainloop()
