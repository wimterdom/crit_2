import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image
import socket

def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'

def show_votes(root,frame1):
	root.title("Votes")
	for widget in frame1.winfo_children():
		widget.destroy()

	client_socket = establish_connection()

	result = df.show_result()
    

	Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
	Label(frame1, text="").grid(row = 1,column = 0)

	vote = StringVar(frame1,"-1")

	bjpLogo = ImageTk.PhotoImage((Image.open("img/kp.jpg")).resize((70,70),Image.ANTIALIAS))
	bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

	congLogo = ImageTk.PhotoImage((Image.open("img/dpp.jpg")).resize((70,70),Image.ANTIALIAS))
	congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

	aapLogo = ImageTk.PhotoImage((Image.open("img/kmt.jpg")).resize((70,70),Image.ANTIALIAS))
	aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)

	ssLogo = ImageTk.PhotoImage((Image.open("img/lin.jpg")).resize((70,70),Image.ANTIALIAS))
	ssImg = Label(frame1, image=ssLogo).grid(row = 5,column = 0)

	notaLogo = ImageTk.PhotoImage((Image.open("img/lisa.jpg")).resize((70,70),Image.ANTIALIAS))
	notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)


	Label(frame1, text="①柯文哲、吳欣盈              :       ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
	Label(frame1, text=result['kp'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

	Label(frame1, text="②賴清德、蕭美琴              :       ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
	Label(frame1, text=result['dpp'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

	Label(frame1, text="③侯友宜、趙少康              :       ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
	Label(frame1, text=result['kmt'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

	Label(frame1, text="④林襄、李多惠                :       ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
	Label(frame1, text=result['lin'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

	Label(frame1, text="⑤Lisa、Rose                 :       ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
	Label(frame1, text=result['lisa'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

	frame1.pack()
	root.mainloop()

# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         showVotes(root,frame1)