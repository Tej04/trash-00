
import socket
import sys
import math

def p2p_client():


   
   host =socket.gethostname()
   port=6060
   s = socket.socket() 
   s.connect((host, port))

   n=int(s.recv(1024).decode('utf-8'))
   e=int(s.recv(1024).decode('utf-8'))
   print("Public key received from Alice")
   print("Public key: {"+str(n)+","+str(e)+"}")

   message=7
   cipher=int((math.pow(message,e))%n)
   print("Encrypting...")
   print("Sending encrypted message to Alice")
   s.send(str(cipher).encode('utf-8'))
   
   
   s.close()

if __name__ == "__main__":

     sys.exit(p2p_client())
