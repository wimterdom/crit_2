import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image
from dframe import *
import random
import pyperclip
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):
    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote1 = "kp"
    vote2 = "dpp"
    vote3 = "kmt"
    vote4 = "lin"
    vote5 = "lisa"

    vote1_env = public_key.encrypt(
                vote1.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
    vote2_env = public_key.encrypt(
                vote2.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
    vote3_env = public_key.encrypt(
                vote3.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
    vote4_env = public_key.encrypt(
                vote4.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
    vote5_env = public_key.encrypt(
                vote5.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
    #print("encoded data: ", vote2_env)
    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "民眾黨\n\n①柯文哲、吳欣盈", variable = vote, value = "kp", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,vote1_env,client_socket)).grid(row = 2,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/kp.jpg")).resize((70,70),Image.ANTIALIAS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "民進黨\n\n②賴清德、蕭美琴", variable = vote, value = "dpp", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,vote2_env,client_socket)).grid(row = 3,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/dpp.jpg")).resize((70,70),Image.ANTIALIAS))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "國民黨\n\n③侯友宜、趙少康", variable = vote, value = "kmt", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,vote3_env,client_socket) ).grid(row = 4,column = 1)
    aapLogo = ImageTk.PhotoImage((Image.open("img/kmt.jpg")).resize((70,70),Image.ANTIALIAS))
    aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "桃猿\n\n④林襄、李多惠", variable = vote, value = "lin", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,vote4_env,client_socket)).grid(row = 5,column = 1)
    ssLogo = ImageTk.PhotoImage((Image.open("img/lin.jpg")).resize((70,70),Image.ANTIALIAS))
    ssImg = Label(frame1, image=ssLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "BlackPink\n\n⑤Lisa、Rose", variable = vote, value = "lisa", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,vote5_env,client_socket)).grid(row = 6,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/lisa.jpg")).resize((70,70),Image.ANTIALIAS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
