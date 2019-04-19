
import socket
import sys
import math

HOST = socket.gethostname()              # Symbolic name meaning all available interfaces
BUFFER = 4096
PORT = 6060


def p2p_server():
    
    
    
    server_socket = socket.socket()
    server_socket.bind((HOST,PORT))
    server_socket.listen(1)

    client, addr =  server_socket.accept()
    
    P=input("Enter P: ")
    G=input("Enter G: ")
    client.send(P.encode('utf-8'))
    client.send(G.encode('utf-8'))

    P=int(P)
    G=int(G)
    a=4
    x=str(int((math.pow(G,a))%P))
    y=int(client.recv(1024).decode('utf-8'))
    print("Bob's public key: ",y)

    client.send(x.encode("utf-8"))

    ka=str(int((math.pow(y,a))%P))
    client.send(ka.encode('utf-8'))
    
    #kb=int(client.recv(1024).decode('utf-8'))

    client.close()

if __name__ == "__main__":

    sys.exit(p2p_server())
