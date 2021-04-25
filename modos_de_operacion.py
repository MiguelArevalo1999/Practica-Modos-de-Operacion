from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from Crypto.Cipher import DES
import tkinter as tk
import math
import random

raiz=Tk()
raiz.title("Cipher Operation Modes")
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
text1 = Label(text="Escuela Superior de Computo\n Oswaldo Aguilar Martinez\n Miguel Angel Arevalo Andrade")
text1.place(x=125,y=7)
combo=ttk.Combobox(raiz)
combo.place(x=315,y=130)
text2= Label(text="Cipher mode")
text2.place(x=240,y=130)
combo['values']=('AES','DES')
combo2=ttk.Combobox(raiz)
text3= Label(text="Operation mode")
text3.place(x=240,y=160)
combo2.place(x=315,y=160)
combo2['values']=('ECB','CBC', 'CFB','OFB','CTR',)
text4=Label(raiz, text = "Key:")
text4.place(x=10,y=160)
blank1 = Entry(raiz)
blank1.place(x=50,y=160)
text5=Label(raiz, text = "Vector:")
text5.place(x=10,y=140)
blank2 = Entry(raiz)
blank2.place(x=55,y=140)

def seleccionar_funcion():
        combo_sel1=combo.get()
        combo_sel2=combo2.get()
        keyword = str(blank1.get())
        vector = str(blank2.get())
       
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

def abrirArchivo_a_Usar():
    raiz.archivo=filedialog.askopenfilename(initialdir="C:",title = "Select an image to cipher",filetypes=(("bmp files","*.bmp"),("all files","*.*")))

abrir=Button(raiz, text="Select File",command=abrirArchivo_a_Usar)
abrir.place(x=50,y=100)



sel=Button(raiz, text="Start process",command=seleccionar_funcion)
sel.place(x=50,y=190)

raiz.mainloop()
