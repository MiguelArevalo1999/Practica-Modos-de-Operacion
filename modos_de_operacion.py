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
combo3=ttk.Combobox(raiz)
text6= Label(text="Ciphered or Deciphered")
text6.place(x=240,y=200)
combo3.place(x=315,y=200)
combo3['values']=('Cipher','Decipher')
text4=Label(raiz, text = "Key:")
text4.place(x=10,y=160)
blank1 = Entry(raiz)
blank1.place(x=50,y=160)
text5=Label(raiz, text = "Vector:")
text5.place(x=10,y=140)
blank2 = Entry(raiz)
blank2.place(x=55,y=140)

def seleccionar_funcion():
        combo_sel1 = combo.get()
        combo_sel2 = combo2.get()
        combo_sel3 = combo3.get()
        keyword = str(blank1.get())
        vector = str(blank2.get())
       
        if combo_sel1 == "DES" and combo_sel2 == "ECB":
            if combo_sel3 == "Cipher":
                pass
            elif combo_sel2 == "Decipher":
                pass

        elif combo_sel1 == "DES" and combo_sel2 == "CBC":
            if combo_sel3 == "Cipher":
                pass
            elif combo_sel2 == "Decipher":
                pass

        elif combo_sel1 == "DES" and combo_sel2 == "CFB":
            
            if combo_sel3 == "Cipher":
                pass
            elif combo_sel2 == "Decipher":
                pass

        elif combo_sel1 == "DES" and combo_sel2 == "OFB":
            if combo_sel3 == "Cipher":
                pass
            elif combo_sel2 == "Decipher":
                pass

        elif combo_sel1 == "DES" and combo_sel2 == "CTR":
            if combo_sel3 == "Cipher":
                pass
            elif combo_sel2 == "Decipher":
                pass
        
        else:
            messagebox.showinfo("Error ","You must select an option")
        

def abrirArchivo_a_Usar():
    raiz.archivo=filedialog.askopenfilename(initialdir="C:",title = "Select an image to cipher",filetypes=(("bmp files","*.bmp"),("all files","*.*")))

abrir=Button(raiz, text="Select File",command=abrirArchivo_a_Usar)
abrir.place(x=50,y=100)



sel=Button(raiz, text="Start process",command=seleccionar_funcion)
sel.place(x=50,y=190)

raiz.mainloop()
