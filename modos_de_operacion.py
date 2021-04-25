from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
import tkinter as tk
import math
import random

raiz=Tk()
raiz.title("Vigenére/Affine")
raiz.resizable(0,0)
# raiz.iconbitmap("huella.ico")
raiz.geometry("550x250")
raiz.config(bg="cyan")

myFrame=Frame()
myFrame.pack(side="top")
myFrame.config(bg="white")
#myFrame.config(width="350", height="350")
#Logo ESCOM
imagen=tk.PhotoImage(file="logoescom.png")
imagen_sub=imagen.subsample(12)
widget=ttk.Label(image=imagen_sub)
widget.place(x=5,y=5)

#Logo IPN
imageni=tk.PhotoImage(file="ipn.png")
imageni_sub=imageni.subsample(15)
widgeti=ttk.Label(image=imageni_sub)
widgeti.place(x=350,y=5)
text = Label(text="Escuela Superior de Computo\n Oswaldo Aguilar Martinez\n Miguel Angel Arevalo Andrade")
text.place(x=125,y=7)
combo=ttk.Combobox(raiz)
combo.place(x=315,y=130)
text= Label(text="Cipher mode")
text.place(x=240,y=130)
combo['values']=('Vigenére','Affine')
combo1=ttk.Combobox(raiz)
text1= Label(text="Alphabet")
text1.place(x=240,y=100)
combo1.place(x=315,y=100)
combo1['values']=('Spanish','English')
combo2=ttk.Combobox(raiz)
text2= Label(text="Operation")
text2.place(x=240,y=160)
combo2.place(x=315,y=160)
combo2['values']=('Ciphered','Deciphered')
text3=Label(raiz, text = "Alpha:")
text3.place(x=10,y=100)
text4=Label(raiz, text = "Beta:")
text4.place(x=10,y=120)
text5=Label(raiz, text = "n:")
text5.place(x=10,y=140)
text6=Label(raiz, text = "Key:")
text6.place(x=10,y=160)
blank = Entry(raiz)
blank.place(x=50,y=100)
blank1 = Entry(raiz)
blank1.place(x=50,y=120)
blank2 = Entry(raiz)
blank2.place(x=50,y=140)
blank3 = Entry(raiz)
blank3.place(x=50,y=160)

def seleccionar_funcion():
        combo_sel1=combo1.get()
        combo_sel=combo.get()
        combo_sel2=combo2.get()
        alpha=int(blank.get())
        beta=int(blank1.get())
        n=int(blank2.get())
        keyword = str(blank3.get())
        if combo_sel1 == "Spanish" and combo_sel == "Vigenére" and combo_sel2 == "Ciphered":
            n=27
            if combo_sel2 == "Ciphered":
                with open('elvis_paravigenere.txt', 'r') as file:
                 string = file.read().replace('\n', '')
                 key = generateKey(string, keyword)
                cipherText(string,key)
            elif combo_sel2 == "Deciphered":
                with open('elvis_paravigenere_C.vig', 'r') as file:
                 cipher_text = file.read().replace('\n', '')
                 key = generateKey(string, keyword)
                 originalText(cipher_text,key)

        elif combo_sel1 == "Spanish" and combo_sel == "Affine":
            #n=27
            if combo_sel2 == "Ciphered":
                Encrypt(n,alpha,beta)
            elif combo_sel2 == "Deciphered":
                Decrypt(n,alpha,beta)
        elif combo_sel1 == "English" and combo_sel == "Vigenére":
            n=26
            if combo_sel2 == "Ciphered":
                with open('elvis_paravigenere.txt', 'r') as file:
                 string = file.read().replace('\n', '')
                 key = generateKey(string, keyword)
                cipherText(string,key)
            elif combo_sel2 == "Deciphered":
                with open('elvis_paravigenere.txt', 'r') as file:
                 string = file.read().replace('\n', '')
                with open('elvis_paravigenere_C.vig', 'r') as file:
                 cipher_text = file.read().replace('\n', '')
                 key = generateKey(string, keyword)
                 originalText(cipher_text,key)

        elif combo_sel1 == "English" and combo_sel == "Affine":
            #n=26
            if combo_sel2 == "Ciphered":
                Encrypt(n,alpha,beta)
            elif combo_sel2 == "Deciphered":
                Decrypt(n,alpha,beta)
        else:
            messagebox.showinfo("Error ","You must select an option")
        return n

def generateKey(string, key):
    print(key)
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

# This function get the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    print(string)
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    cipher_text_s = ''.join(cipher_text)
    file = open("elvis_paravigenere_C.vig", "w")
    file.write(cipher_text_s)
    file.close()

# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    print(cipher_text)
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    orig_text_s = ''.join(orig_text)
    file = open("elvis_paravigenere_C_D.vig", "w")
    file.write(orig_text_s)
    file.close()

def Euclides(m, n):
	r=0
	while (n!=0):
		r=m%n
		m=n
		n=r
	return m

def Inverse(y,p):
    (b,z,x)=ExtEuclidean(y,p)
    if(z<0):
        z=z+p
    return z

def ExtEuclidean(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    numiteraciones = 0
    while a:
        (q, a), b = (b // a, b % a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
        numiteraciones += 1
    return b, x0, y0

def generar_Rdm():
    combo_sel1=combo1.get()
    n=int(blank2.get())
    if combo_sel1 == "Spanish":
        blank.delete(0, END)
        blank1.delete(0, END)
        blank2.delete(0, END)
        alpha,beta=generar(n)
        blank.insert(0,alpha)
        blank1.insert(0,beta)
        blank2.insert(0,n)
    else:
        #n=26
        blank.delete(0, END)
        blank1.delete(0, END)
        blank2.delete(0, END)
        alpha,beta=generar(n)
        blank.insert(0,alpha)
        blank1.insert(0,beta)
        blank2.insert(0,n)

def generar(n):
    probables=[]
    a=1
    b=n
    for i in range (a,b+1):
        if math.gcd(i,b)==1:
            probables.append(i)
    print("Números que se pueden usar: ",probables)
    #generar alpha
    alpha,beta=random.sample(probables,2)
    #print(alpha,beta)
    return alpha,beta
    #generar betha
def num_to_char(n):
    m = chr(n + 97)
    return m

def char_to_num(k):
    z = (ord(k.lower()) - 97)
    return z

def Encrypt(n, alpha, beta):
    file = open("simon_paraAffine.txt", "r")
    f=open("file_.aff","wb")
    while 1:
        # read by character
        char = file.read(1)
        if not char:
            break
        print(char)
        P_n = char_to_num(char)
        C_n = ((alpha * P_n) + beta) % n
        #print(C_n)
        cipher_text=(num_to_char(C_n))
        # print(cipher_text)
        f.write(cipher_text.encode('UTF-8'))
        #print(char)
    file.close()
    f.close

def InversoAditivo(beta,n):
    if beta > 0:
        addInv=n - beta
    else:
        addInv = n + beta
    return addInv

def Decrypt(n, alpha, beta):
    file1 = open("file_.aff","r",encoding='UTF-8')
    f1=open("file.aff","wb")
    print("Mensaje Decifrado")
    while 1:
        # read by character
        char = file1.read(1)
        if not char:
            break
        C_n = char_to_num(char)
        alpha_inverso_multiplicativo = Inverse(alpha,n)
        beta_inverso_aditivo = InversoAditivo(beta, n)
        P_n = ( alpha_inverso_multiplicativo * ( C_n + beta_inverso_aditivo ) ) % n
        decipher_text=(num_to_char(P_n))
        f1.write(decipher_text.encode('UTF-8'))
        #print(decipher_text)
            #print(char)
    file1.close()
    f1.close

def validar_alpha():
    a=int(blank.get())
    n=int(blank2.get())
    if(Euclides(a,n)==1):
        messagebox.showinfo("Alpha","Alpha es valida")
    else:
        messagebox.showinfo("Alpha","Alpha es invalida")
def validar_beta():
    b=int(blank1.get())
    n=int(blank2.get())
    if(Euclides(b,n)==1):
        messagebox.showinfo("Beta","Beta es valida")
    else:
        messagebox.showinfo("Beta","Beta es invalida")
     #/*
     #*  Aplicando la formula de des cifrado: P_n = alpha^-1 * [ C_n + (-beta) ] mod longitud_del_alfabeto, donde:
     #*  C_n, es el carácter del texto en claro descifrado
     #*  P_n, es la letra de la posicion n del texto cifrado
     #*  alpha, es el valor multiplicativo de la llave en inverso multiplicativo
     #*  beta, es el valor aditivo de la llave en inverso aditivo
     #* */
sel=Button(raiz, text="Start process",command=seleccionar_funcion)
sel.place(x=50,y=190)
sel1=Button(raiz, text="Random",command=generar_Rdm)
sel1.place(x=50,y=220)
sel2=Button(raiz, text="Alpha Validation",command=validar_alpha)
sel2.place(x=150,y=190)
sel3=Button(raiz, text="Beta Validation",command=validar_beta)
sel3.place(x=150,y=220)
t=int(input("Ingresa el valor de alpha: "))
u=int(input("Ingresa el valor de n: "))
print("GCD: ",Euclides(t,u))
if(Euclides(t,u)==1):
        print("Inverso Multiplicativo: ",Inverse(t,u))
        print("Llave valida\n")
else:
   print("Llave invalida\n")
raiz.mainloop()
