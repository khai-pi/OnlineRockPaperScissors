import socket
from _thread import *
from player import  Player
import pickle

server = "192.168.0.104"
port = 5555
currentPlayer = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,255,0))]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while(True):
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break

            if player == 0:
                reply = players[1]
            elif player == 1:
                reply = players[0]

            #print("Received: ", data)
            #print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))

        except error:
            print("Except at threadloop", error)
            break

    print("Player", player, "Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client,(conn, currentPlayer))

    currentPlayer+=1


