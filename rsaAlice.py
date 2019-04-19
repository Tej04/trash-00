
import socket
import sys
import math

HOST = socket.gethostname()              # Symbolic name meaning all available interfaces
BUFFER = 4096
PORT = 6060

def gcd(a,h):
    while 1:
        temp=a%h
        if temp==0:
            return h
        a=h
        h=temp

def p2p_server():
    
    
    
    server_socket = socket.socket()
    server_socket.bind((HOST,PORT))
    server_socket.listen(1)

    client, addr =  server_socket.accept()
    p=11
    q=3
    n=p*q
    phi=(p-1)*(q-1)

    e=2
    while e<phi:
        if gcd(e,phi)==1:
            break
        else:
            e=e+1

            
    d=0
    for i in range(0,20):
        x=(phi*i)+1
        if x%e==0:
            d=x/e
            break
    
    print("Public key: {"+str(n)+","+str(e)+"}")
    print("Sending public key to Bob")
    client.send(str(n).encode('utf-8'))
    client.send(str(e).encode('utf-8'))

    cipher=int(client.recv(1024).decode('utf-8'))

    print("Encrypted message received from Bob")
    print("Decrypting...")
    message=int((math.pow(cipher,d))%n)
    print("Message: ",message)

    client.close()

if __name__ == "__main__":

    sys.exit(p2p_server())
