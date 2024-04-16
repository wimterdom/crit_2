import socket
import threading
import dframe as df
from threading import Thread
from dframe import *
import random
import pyperclip
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import time

lock = threading.Lock()

def generate_rsa_keys():
    # 生成 RSA 金鑰
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    # 序列化私鑰
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    # 序列化公鑰
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # 儲存金鑰到本地文件
    with open("private_key.pem", "wb") as private_key_file:
        private_key_file.write(private_pem)

    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(public_pem)

    return public_pem, private_key

def send_public_key(public_key):
    # 建立 socket 連線
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Server is running...")

    while True:
        # 等待客戶端連線
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # 傳送公鑰給客戶端
        client_socket.send(public_key)
        client_socket.close()

        break

def client_thread(connection):

    data = connection.recv(1024)     #receiving voter details            #2

    #verify voter details
    log = (data.decode()).split(' ')
    log[0] = int(log[0])
    if(df.verify(log[0],log[1])):                                #3 Authenticate
        if(df.isEligible(log[0])):
            print('Voter Logged in... ID:'+str(log[0]))
            connection.send("Authenticate".encode())
        else:
            print('Vote Already Cast by ID:'+str(log[0]))
            connection.send("VoteCasted".encode())
            time.sleep(2)
            with open("./database/cand_list.csv", "rb") as cand:
                cand_data = cand.read()
                connection.send(cand_data)
            #

    else:
        print('Invalid Voter')
        connection.send("InvalidVoter".encode())


    data = connection.recv(1024)                                    #4 Get Vote
    print("Vote Received from ID: "+str(log[0])+"  Processing...")
    lock.acquire()
    #update Database
    decrypted_value = private_key.decrypt(
                    data,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
    print(str(decrypted_value))
    if(df.vote_update(decrypted_value.decode(),log[0])):
        print("Vote Casted Sucessfully by voter ID = "+str(log[0]))
        connection.send("Successful".encode())
    else:
        print("Vote Update Failed by voter ID = "+str(log[0]))
        connection.send("Vote Update Failed".encode())
                                                                        #5

    lock.release()
    connection.close()


def voting_Server():

    serversocket = socket.socket()
    host = socket.gethostname()
    port = 4001

    ThreadCount = 0

    try :
        serversocket.bind((host, port))
    except socket.error as e :
        print(str(e))
    print("Waiting for the connection")

    serversocket.listen(10)

    print( "Listening on " + str(host) + ":" + str(port))

    while True :
        client, address = serversocket.accept()

        print('Connected to :', address)

        client.send("Connection Established".encode())   ### 1
        
        t = Thread(target = client_thread,args = (client,))
        t.start()
        ThreadCount+=1
        # break

    serversocket.close()
    
if __name__ == '__main__':
    public_key, private_key = generate_rsa_keys()
    send_public_key(public_key)
    voting_Server()
