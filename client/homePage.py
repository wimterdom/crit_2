import subprocess as sb_p
import tkinter as tk
from tkinter import *
from Admin import AdmLogin
from voter import voterLogin
import socket
from ShowVotes import *

def receive_public_key():
    # 建立 socket 連線
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    # 接收公鑰
    public_key = client_socket.recv(4096)

    # 關閉連線
    client_socket.close()

    return public_key

def save_public_key(public_key):
    # 將公鑰儲存至本地文件
    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(public_key)

def Home(root, frame1, frame2):

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    Button(frame2, text="Home", command = lambda: Home(root, frame1, frame2)).grid(row=0,column=0)
    Label(frame2, text="                                                                         ").grid(row = 0,column = 1)
    Label(frame2, text="                                                                         ").grid(row = 0,column = 2)
    Label(frame2, text="         ").grid(row = 1,column = 1)
    frame2.pack(side=TOP)

    root.title("Presidential election")

    Label(frame1, text="Presidential election", font=('Helvetica', 25, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    #Admin Login
    #admin = Button(frame1, text="Show Votes", width=15, command = lambda: show_votes(root, frame1))

    #Voter Login
    voter = Button(frame1, text="Voter Login", width=15, command = lambda: voterLogin(root, frame1))

    #New Tab
    newTab = Button(frame1, text="New Window", width=15, command = lambda: sb_p.call('start python homePage.py', shell=True))

    Label(frame1, text="").grid(row = 2,column = 0)
    Label(frame1, text="").grid(row = 4,column = 0)
    Label(frame1, text="").grid(row = 6,column = 0)
    #admin.grid(row = 3, column = 1, columnspan = 2)
    voter.grid(row = 5, column = 1, columnspan = 2)
    newTab.grid(row = 7, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()


def new_home():
    root = Tk()
    root.geometry('500x500')
    frame1 = Frame(root)
    frame2 = Frame(root)
    Home(root, frame1, frame2)


if __name__ == "__main__":
    received_public_key = receive_public_key()
    save_public_key(received_public_key)
    new_home()
