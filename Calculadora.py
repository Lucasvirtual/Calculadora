#importando tkinter
from re import A
from tkinter import *
from tkinter import ttk
from turtle import width

#cores

cor1 = "#000000"   #preta
cor2 = "#050df7"   #azul
cor3 = "#ffffff"   #branco
cor4 = "#1aff00"   #verde
cor5 = "#ff0000"   #vermelho


janela = Tk()
janela.title("Calculadora")
janela.geometry("238x318")
janela.config(bg=cor1)




# criando frames
frame_tela = Frame(janela, width=238, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=238, height=268, bg=cor3)
frame_corpo.grid(row=1, column=0)

# variavel todos valores
todos_valores = ''

#criando label
valor_texto = StringVar()


#criando funcao

def entrar_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)
    
    

    
    
    #passando valor para tela
    valor_texto.set(todos_valores)

# funcao para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

    # funcao limpar tela

def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Courier 18 bold'))
app_label.place(x=0,y=0)


#criando botoes

b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=22, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_2.place(x=150, y=0)
b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'),text="/", width=5, height=3, bg=cor5, relief=RAISED, overrelief=RIDGE)
b_3.place(x=194, y=0)

b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=8, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=50)
b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'),text="8", width=8, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_5.place(x=66, y=50)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'),text="9", width=8, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_6.place(x=132, y=50)
b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'),text="*", width=5, height=3, bg=cor5, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_7.place(x=194, y=50)

b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'),text="4", width=8, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=106)
b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'),text="5", width=8, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_9.place(x=66, y=106)
b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'),text="6", width=8, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_10.place(x=132, y=106)
b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'),text="-", width=5, height=3, bg=cor5, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_11.place(x=194, y=106)

b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'),text="1", width=8, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=162)
b_13 = Button(frame_corpo, command = lambda: entrar_valores('2'),text="2", width=8, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_13.place(x=66, y=162)
b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'),text="3", width=8, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_14.place(x=132, y=162)
b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'),text="+", width=5, height=3, bg=cor5, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_15.place(x=194, y=162)

b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'),text="0", width=22, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=212)
b_17 = Button(frame_corpo, command = lambda: entrar_valores('.'),text=".", width=5, height=3, bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
b_17.place(x=150, y=212)
b_18 = Button(frame_corpo, command = calcular ,text="=", width=5, height=3, bg=cor5, relief=RAISED, overrelief=RIDGE)
b_18.place(x=194, y=212)




janela.mainloop()