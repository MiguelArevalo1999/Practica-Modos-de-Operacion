from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from Crypto.Cipher import DES
from PIL import Image
import tkinter as tk
import random
import string
import os

filename = None

def abrirArchivo_a_Usar():
    global filename
    filename = filedialog.askopenfilename(initialdir="C:",title = "Select an image to cipher",filetypes=(("bmp files","*.bmp"),("all files","*.*")))
    head, tail = os.path.split(filename)
    filename = tail
    print(filename)


# ruta= r'C:\Users\helbo\OneDrive\Documentos\GitHub\Practica-Modos-de-Operacion\Imagen1.bmp'
# ruta1= r'C:\Users\helbo\OneDrive\Documentos\GitHub\Practica-Modos-de-Operacion\Imagen1_eECB.bmp'
# ruta2= r'C:\Users\helbo\OneDrive\Documentos\GitHub\Practica-Modos-de-Operacion\Imagen1_eCBC.bmp'
# ruta3= r'C:\Users\helbo\OneDrive\Documentos\GitHub\Practica-Modos-de-Operacion\Imagen1_eCFB.bmp'
# ruta4= r'C:\Users\helbo\OneDrive\Documentos\GitHub\Practica-Modos-de-Operacion\Imagen1_eOFB.bmp'
# ruta5= r'C:\Users\helbo\OneDrive\Documentos\GitHub\Practica-Modos-de-Operacion\Imagen1_eCTR.bmp'
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
IV=" "
def seleccionar_funcion():
        global IV
        combo_sel1 = combo.get()
        combo_sel2 = combo2.get()
        combo_sel3 = combo3.get()
        key = str(blank1.get())
        vector = str(blank2.get())
        global filename
        # filename=os.path.basename(ruta)
        # filename1=os.path.basename(ruta1)
        # filename2=os.path.basename(ruta2)
        # filename3=os.path.basename(ruta3)
        # filename4=os.path.basename(ruta4)
        # filename5=os.path.basename(ruta5)
        #print(filename)
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
            elif combo_sel3 == "Decipher":
                if "ECB" not in filename:
                    messagebox.showinfo("Error ","Decipher mode not allowed")
                im = Image.open(filename1)
                 #Convert image data into pixel value bytes
                value_vector = im.convert("RGB").tobytes()
                imlength = len(value_vector)
                value_desencrypt = trans_format_RGB(des_ecb_desencrypt(key, pad(value_vector))[:imlength])
                #for i in range(original):
                    #print(new[i])
                 #Create a new object, store the corresponding value
                im2 = Image.new(im.mode, im.size)
                im2.putdata(value_desencrypt)
                file =  os.path.splitext(filename1)

                # Save the object as an image in the corresponding format
                im2.save(file[0] + "_dECB" + "." + "bmp")
                print("Hola")

        elif combo_sel1 == "DES" and combo_sel2 == "CBC":
            if combo_sel3 == "Cipher":
                im = Image.open(filename)
                value_vector = im.convert("RGB").tobytes()

                # Convert image data to pixel value bytes
                imlength = len(value_vector)

                # Perform pixel value mapping on the filled and encrypted data
                val, IV=des_cbc_encrypt(key, pad(value_vector))
                value_encrypt = trans_format_RGB(val[:imlength])

                # Create a new object, store the corresponding value
                im2 = Image.new(im.mode, im.size)
                im2.putdata(value_encrypt)

                # Save the object as an image in the corresponding format
                file =  os.path.splitext(filename)
                im2.save(file[0] + "_eCBC" + "." + "bmp")

            elif combo_sel3 == "Decipher":
                if "CBC" not in filename:
                    messagebox.showinfo("Error ","Decipher mode not allowed")
                im = Image.open(filename2)
                value_vector = im.convert("RGB").tobytes()

                # Convert image data to pixel value bytes
                imlength = len(value_vector)

                # Perform pixel value mapping on the filled and encrypted data
                val=des_cbc_desencrypt(key, pad(value_vector),IV)
                value_desencrypt = trans_format_RGB(val[:imlength])

                # Create a new object, store the corresponding value
                im2 = Image.new(im.mode, im.size)
                im2.putdata(value_desencrypt)

                # Save the object as an image in the corresponding format
                file =  os.path.splitext(filename2)
                im2.save(file[0] + "_dCBC" + "." + "bmp")
        elif combo_sel1 == "DES" and combo_sel2 == "CFB":
            if combo_sel3 == "Cipher":
                im = Image.open(filename)
                value_vector = im.convert("RGB").tobytes()

                # Convert image data to pixel value bytes
                imlength = len(value_vector)

                # Perform pixel value mapping on the filled and encrypted data
                val, IV=des_cfb_encrypt(key, pad(value_vector))
                value_encrypt = trans_format_RGB(val[:imlength])
                # Create a new object, store the corresponding value
                im2 = Image.new(im.mode, im.size)
                im2.putdata(value_encrypt)

                # Save the object as an image in the corresponding format
                file =  os.path.splitext(filename)
                im2.save(file[0] + "_eCFB" + "." + "bmp")

            elif combo_sel3 == "Decipher":
                    if "CFB" not in filename:
                        messagebox.showinfo("Error ","Decipher mode not allowed")
                    im = Image.open(filename3)
                    value_vector = im.convert("RGB").tobytes()

                    # Convert image data to pixel value bytes
                    imlength = len(value_vector)
                    # Perform pixel value mapping on the filled and encrypted data
                    val=des_cfb_desencrypt(key, pad(value_vector),IV)
                    value_desencrypt = trans_format_RGB(val[:imlength])

                    # Create a new object, store the corresponding value
                    im2 = Image.new(im.mode, im.size)
                    im2.putdata(value_desencrypt)

                    # Save the object as an image in the corresponding format
                    file =  os.path.splitext(filename3)
                    im2.save(file[0] + "_dCFB" + "." + "bmp")
        elif combo_sel1 == "DES" and combo_sel2 == "OFB":
            if combo_sel3 == "Cipher":
                im = Image.open(filename)
                value_vector = im.convert("RGB").tobytes()
                # Convert image data to pixel value bytes
                imlength = len(value_vector)
                # Perform pixel value mapping on the filled and encrypted data
                val, IV=des_ofb_encrypt(key, pad(value_vector))
                value_encrypt = trans_format_RGB(val[:imlength])
                # Create a new object, store the corresponding value
                im2 = Image.new(im.mode, im.size)
                im2.putdata(value_encrypt)
                # Save the object as an image in the corresponding format
                file =  os.path.splitext(filename)
                im2.save(file[0] + "_eOFB" + "." + "bmp")

            elif combo_sel3 == "Decipher":
                if "OFB" not in filename:
                        messagebox.showinfo("Error ","Decipher mode not allowed")
                im = Image.open(filename4)
                value_vector = im.convert("RGB").tobytes()
                # Convert image data to pixel value bytes
                imlength = len(value_vector)
                # Perform pixel value mapping on the filled and encrypted data
                val=des_ofb_desencrypt(key, pad(value_vector),IV)
                value_desencrypt = trans_format_RGB(val[:imlength])

                # Create a new object, store the corresponding value
                im2 = Image.new(im.mode, im.size)
                im2.putdata(value_desencrypt)

                # Save the object as an image in the corresponding format
                file =  os.path.splitext(filename4)
                im2.save(file[0] + "_dOFB" + "." + "bmp")
        elif combo_sel1 == "DES" and combo_sel2 == "CTR":
            if combo_sel3 == "Cipher":
                im = Image.open(filename)
                value_vector = im.convert("RGB").tobytes()

                # Convert image data to pixel value bytes
                imlength = len(value_vector)

                # Perform pixel value mapping on the filled and encrypted data
                value_encrypt = trans_format_RGB(des_ctr_encrypt(key, pad(value_vector))[:imlength])
                #val, IV=des_ofb_encrypt(key, pad(value_vector))
                #value_encrypt = trans_format_RGB(val[:imlength])
                # Create a new object, store the corresponding value
                im2 = Image.new(im.mode, im.size)
                im2.putdata(value_encrypt)

                # Save the object as an image in the corresponding format
                file =  os.path.splitext(filename)
                im2.save(file[0] + "_eCTR" + "." + "bmp")
            elif combo_sel3 == "Decipher":
                im = Image.open(filename)
                value_vector = im.convert("RGB").tobytes()

                # Convert image data to pixel value bytes
                imlength = len(value_vector)

                # Perform pixel value mapping on the filled and encrypted data
                value_encrypt = trans_format_RGB(des_ctr_desencrypt(key, pad(value_vector))[:imlength])
                #val, IV=des_ofb_encrypt(key, pad(value_vector))
                #value_encrypt = trans_format_RGB(val[:imlength])
                # Create a new object, store the corresponding value
                im2 = Image.new(im.mode, im.size)
                im2.putdata(value_encrypt)

                # Save the object as an image in the corresponding format
                file =  os.path.splitext(filename)
                im2.save(file[0] + "_dCTR" + "." + "bmp")
                if "CTR" not in filename:
                        messagebox.showinfo("Error ","Decipher mode not allowed")
        else:
            messagebox.showinfo("Error ","You must select an option")


def pad(data):
    return data + b"\x00" * (8 - len(data) % 8)

def des_cbc_encrypt(key, data, mode=DES.MODE_CBC):
    #IV is a random value
    global IV
    IV = key_generator(8)
    des = DES.new(key.encode("utf8"), mode, IV.encode("utf8"))
    new_data = des.encrypt(data)
    return new_data, IV

def des_cbc_desencrypt(key, data, IV, mode=DES.MODE_CBC):
    #IV is a random value
    des = DES.new(key.encode("utf8"), mode, IV.encode("utf8"))
    new_data = des.decrypt(data)
    return new_data

# ECB encryption
def des_ecb_encrypt(key, data, mode=DES.MODE_ECB):
    #The default mode is ECB encryption
    des = DES.new(key.encode("utf8"), mode)
    new_data = des.encrypt(data)
    return new_data

def des_ecb_desencrypt(key, data, mode=DES.MODE_ECB):
    #The default mode is ECB encryption
    des = DES.new(key.encode("utf8"), mode)
    new_data = des.decrypt(data)
    return new_data

def des_cfb_encrypt(key, data, mode=DES.MODE_CFB):
    global IV
    IV = key_generator(8)
    des = DES.new(key.encode("utf8"), mode,IV.encode("utf8"))
    new_data = des.encrypt(data)
    return new_data, IV

def des_cfb_desencrypt(key, data, IV, mode=DES.MODE_CFB):
    des = DES.new(key.encode("utf8"), mode,IV.encode("utf8"))
    new_data = des.decrypt(data)
    return new_data

def des_ofb_encrypt(key, data, mode=DES.MODE_OFB):
    global IV
    IV = key_generator(8)
    des = DES.new(key.encode("utf8"), mode,IV.encode("utf8"))
    new_data = des.encrypt(data)
    return new_data, IV

def des_ofb_desencrypt(key, data, IV, mode=DES.MODE_OFB):
    des = DES.new(key.encode("utf8"), mode,IV.encode("utf8"))
    new_data = des.decrypt(data)
    return new_data

def des_ctr_encrypt(key, data, mode=DES.MODE_CTR):
    des = DES.new(key.encode("utf8"), mode,nonce=b'')
    new_data = des.encrypt(data)
    return new_data

def des_ctr_desencrypt(key, data, mode=DES.MODE_CTR):
    des = DES.new(key.encode("utf8"), mode,nonce=b'')
    new_data = des.decrypt(data)
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
