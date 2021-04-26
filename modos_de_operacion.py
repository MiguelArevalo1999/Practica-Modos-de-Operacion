from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from Crypto.Cipher import DES
from PIL import Image
import tkinter as tk
import random
import string
import os

def abrirArchivo_a_Usar():
    raiz.archivo=filedialog.askopenfilename(initialdir="C:",title = "Select an image to cipher",filetypes=(("bmp files","*.bmp"),("all files","*.*")))


raiz=Tk()
raiz.title("Cipher Operation Modes")
raiz.resizable(0,0)
# raiz.iconbitmap("huella.ico")
raiz.geometry("600x250")
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
combo.place(x=330,y=130)
text2= Label(text="Cipher mode")
text2.place(x=240,y=130)
combo['values']=('AES','DES')
combo2=ttk.Combobox(raiz)
text3= Label(text="Operation mode")
text3.place(x=240,y=160)
combo2.place(x=350,y=160)
combo2['values']=('ECB','CBC', 'CFB','OFB','CTR',)
combo3=ttk.Combobox(raiz)
text6= Label(text="Ciphered or Deciphered")
text6.place(x=240,y=200)
combo3.place(x=400,y=200)
combo3['values']=('Cipher','Decipher')
text4=Label(raiz, text = "Key:")
text4.place(x=10,y=160)
blank1 = Entry(raiz)
blank1.place(x=50,y=160)
text5=Label(raiz, text = "Vector:")
text5.place(x=10,y=140)
blank2 = Entry(raiz)
blank2.place(x=55,y=140)
abrir=Button(raiz, text="Select File",command=abrirArchivo_a_Usar)
abrir.place(x=50,y=100)

def seleccionar_funcion():
        combo_sel1 = combo.get()
        combo_sel2 = combo2.get()
        combo_sel3 = combo3.get()
        key = str(blank1.get())
        vector = str(blank2.get())
        filename = "Imagen1.bmp"
        correctKey(key)
       
        if combo_sel1 == "DES" and combo_sel2 == "ECB":
            if combo_sel3 == "Cipher":
                im = Image.open(filename)
                 #Convert image data into pixel value bytes
                value_vector = im.convert("RGB").tobytes()
                imlength = len(value_vector)
                #for i in range(original):
                    #print(data[i])
    #Map the pixel value of the filled and encrypted data
                value_encrypt = trans_format_RGB(des_ecb_encrypt(key, pad(value_vector))[:imlength])
                #for i in range(original):
                    #print(new[i])
                 #Create a new object, store the corresponding value
                im2 = Image.new(im.mode, im.size)
                im2.putdata(value_encrypt)
                file =  os.path.splitext(filename)
                
                # Save the object as an image in the corresponding format
                im2.save(file[0] + "_eECB" + "." + "bmp")


            elif combo_sel2 == "Decipher":
                pass

        elif combo_sel1 == "DES" and combo_sel2 == "CBC":
            if combo_sel3 == "Cipher":
                im = Image.open(filename)
                value_vector = im.convert("RGB").tobytes()

                # Convert image data to pixel value bytes
                imlength = len(value_vector)

                # Perform pixel value mapping on the filled and encrypted data
                value_encrypt = trans_format_RGB(des_cbc_encrypt(key, pad(value_vector))[:imlength])

                # Create a new object, store the corresponding value
                im2 = Image.new(im.mode, im.size)
                im2.putdata(value_encrypt)

                # Save the object as an image in the corresponding format
                file =  os.path.splitext(filename)
                im2.save(file[0] + "_eCBC" + "." + "bmp")

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


def pad(data):
    return data + b"\x00" * (8 - len(data) % 8)

def des_cbc_encrypt(key, data, mode=DES.MODE_CBC):
    #IV is a random value
    IV = key_generator(8)
    des = DES.new(key.encode("utf8"), mode, IV.encode("utf8"))
    new_data = des.encrypt(data)
    return new_data


# ECB encryption
def des_ecb_encrypt(key, data, mode=DES.MODE_ECB):
    #The default mode is ECB encryption
    des = DES.new(key.encode("utf8"), mode)
    new_data = des.encrypt(data)
    return new_data

def des_cfb_encrypt(key, data, mode=DES.MODE_CFB):
    
    IV = key_generator(8)
    des = DES.new(key.encode("utf8"), mode,IV.encode("utf8"))
    new_data = des.encrypt(data)
    return new_data

def key_generator(size = 8, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

 #Map the image data to RGB
def trans_format_RGB(data):
    #tuple: Immutable, ensure that data is not lost
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(red, green, blue))
    return pixels


def correctKey(key):
    if len(key) == 8:
        pass
    else:
        messagebox.showinfo("Error ","Unvalid key")

sel=Button(raiz, text="Start process",command=seleccionar_funcion)
sel.place(x=50,y=190)

raiz.mainloop()
