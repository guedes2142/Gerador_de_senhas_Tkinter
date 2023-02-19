#Gerador de Senha
from tkinter import  messagebox
import string
from tkinter import ttk
from tkinter.ttk import * #importar nessa ordem 1
from tkinter import * #importar nessa ordem 2
from PIL import ImageTk, Image
import random

#----------------------------------------------
janela = Tk()
janela.geometry('320x400')
janela.title('MaxPass By.Rafael Guedes')
janela.resizable(width=False, height=False)
janela.iconphoto(False, PhotoImage(file='icon2.png'))

#--------------------------Logica de combinação-------------------------------------------
def genpass():
    
    l_upper = string.ascii_uppercase
    l_lower = string.ascii_lowercase
    numBers = '123456789'
    symBols = '@#%$&*!'

    combine = l_upper + l_lower + numBers + symBols
    
    if estado_1.get() == l_upper:
        combine = combine + l_upper
    else:
        pass
    
    if estado_2.get() == l_lower:
        combine = combine + l_lower
    else:
        pass
    
    if estado_3.get() == numBers:
        combine = combine + numBers
    else:
        pass

    if estado_4.get() == symBols:
        combined = combine + symBols
    else:
        pass  
    
    comprimento = int(heightPass.get())
    passWord = "".join(random.sample(combine, comprimento))
    
    displayPass['text'] = passWord   
    
    def passcoy():
            
        info = passWord
        frametwo.clipboard_clear()
        frametwo.clipboard_append(info)
                
<<<<<<< HEAD
        messagebox.showinfo('Sucesso', 'Senha copiada e salva')
=======
        messagebox.showinfo('Sucesso', 'Senha copiada e salva na mesma pasta que esta o programa')
>>>>>>> 35cf901 (commit 2)
        
        with open('senha.txt', 'a') as file:
            file.write(f'{info}\n')
        
#------------------------Botão salva e copia-------------------------------
    copyBtn = Button(frametwo, width=7 , height=1, text='Copiar',font=('Verdana 10'), relief='flat', bg='green', fg='white', command=passcoy)
    copyBtn.grid(row=0, column=0, padx=90, pady=5, sticky=E)     
            
#------------------------Frame de cima----------------------------------------
frameOne = Frame(janela, width=320, height=90, bg='black', pady=0 , padx=0, relief='flat')
frameOne.grid(row=0, column=0, sticky=NSEW)

#------------------------Frame de baixo----------------------------------------
frametwo = Frame(janela, width=500, height=500, bg='black', pady=0 , padx=0, relief='flat')
frametwo.grid(row=1, column=0, sticky=NSEW)

#------------------------Logotipo----------------------------------------
logotipo = Image.open('PassWord.png')
logotipo = logotipo.resize((325,90), Image.ANTIALIAS)
logotipo = ImageTk.PhotoImage(logotipo)
app_logo = Label(frameOne, width=320, image=logotipo, compound=LEFT,padx=5, relief='flat', anchor=NW ,bg='black')
app_logo.grid(row=0, column=0)

#------------------------Display senha----------------------------------------
displayPass = Label(frametwo, text='------------------', width=28, height=2, font=('Verdana 10'), )
displayPass.grid(row=0 , column=0, sticky=W, padx=5)

#------------------------SpinBox-------------------------------
var = IntVar()#Definindo o número inicial da SpinoBox para 8
var.set(8) 
heightPass = Spinbox(frametwo, from_='0' , to='20' , width=10, textvariable=var) 
print(type(heightPass))#<-----
heightPass.grid(row=1, column=0, padx=5, pady=5, sticky=NW)

#--------------------------Logica Inicial------------------------------------------------
l_upper = string.ascii_uppercase
l_lower = string.ascii_lowercase
numBers = '123456789'
symBols = '@#%$&*!.'

#------------------------Label tamanha senha-------------------------------
textOne = Label(frametwo, height=1, text='Número e caracteres da sua senha',font=('Verdana 8'), bg='black', fg='white'  )
textOne.grid(row=1, column=0, sticky=NW, padx=100, pady=5)
textTwo = Label(frametwo, height=1, text='Recomendado 8 ou 12 caracteres ',font=('Verdana 8'), bg='black', fg='white' )
textTwo.grid(row=2, column=0 ,sticky=NS)

#-------------------frameTree----------------
frameTree = Frame(janela, width=300, height=300, bg='black', )
frameTree.grid(row=2, column=0, pady=0, sticky=NSEW )


#------------------------CheckButton-------------------------------
estado_1 = StringVar()
estado_1.set(False)
boxOne = Checkbutton(frameTree, width=5, bg='black', variable=estado_1, onvalue=l_upper, offvalue='off')
boxOne.grid(row=3, column=0, sticky=NW, padx=5, pady=2)

estado_2 = StringVar()
estado_2.set(False)
boxTwo = Checkbutton(frameTree, width=5, bg='black', variable=estado_2, onvalue=l_lower, offvalue='off')
boxTwo.grid(row=4, column=0, sticky=NW, padx=5, pady=2)

estado_3 = StringVar()
estado_3.set(False)
boxtree = Checkbutton(frameTree, width=5, bg='black', variable=estado_3,onvalue=numBers, offvalue='off')
boxtree.grid(row=5, column=0, sticky=NW, padx=5, pady=2)

estado_4 = StringVar()
estado_4.set(False)
boxFour = Checkbutton(frameTree, width=5, bg='black', variable=estado_4, onvalue=symBols, offvalue='off')
boxFour.grid(row=6, column=0, sticky=NW, padx=5, pady=2)

#------------------------CheckBox Info-------------------------------
ma_letter = Label(frameTree, text='Maiúsculas', bg='black', fg='white', font=('Verdana 8 bold'))
ma_letter.grid(row=3, column=0, sticky=NW, padx=50, pady=2)

mi_letter = Label(frameTree, text='Minúsculas', bg='black', fg='white', font=('Verdana 8 bold'))
mi_letter.grid(row=4, column=0, sticky=NW, padx=50, pady=2)

numBers = Label(frameTree, text='Números', bg='black', fg='white', font=('Verdana 8 bold'))
numBers.grid(row=5, column=0, sticky=NW, padx=50, pady=2)

symBols = Label(frameTree, text='Simbolos', bg='black', fg='white', font=('Verdana 8 bold'))
symBols.grid(row=6, column=0, sticky=NW, padx=50, pady=2)

#------------------------Botão gerar senhha-------------------------------
genBtn = Button(frameTree, width=33, height=2, text='Gerar Senha', font=('Verdana 10 bold'), relief='flat', bg='dark green', fg='white', command=genpass)
genBtn.grid(row=7, column=0, sticky=W, pady=52, padx=7)

estilo = ttk.Style(janela)
estilo.theme_use('clam')
janela.mainloop()
<<<<<<< HEAD
=======

#dar opção do usuario criar a senha para poder criar um pdf protegido com senha com as senhas geradas pelo
#programa

#criar input para salvar senha
#criar logica para salvar em pdf protegido
>>>>>>> 35cf901 (commit 2)
