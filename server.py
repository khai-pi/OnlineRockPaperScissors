import socket
from _thread import *
import pickle

server = "192.168.0.104"
port = 5555
currentPlayer = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])



def threaded_client(conn, player):

    while(True):
        try:
            pass

        except error:
            pass



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client,(conn, ))

    currentPlayer+=1
