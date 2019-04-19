
import socket
import sys
import math

def p2p_client():


   
   host =socket.gethostname()
   port=6060
   s = socket.socket() 
   s.connect((host, port))

   P=int(s.recv(1024).decode('utf-8'))
   G=int(s.recv(1024).decode('utf-8'))
   print("P,G: ",P,G)
   b=3
   y=str(int((math.pow(G,b))%P))
   s.send(y.encode('utf-8'))

   x=int(s.recv(1024).decode('utf-8')) 
   print("Alice's public key: ",x)

   kb=str(int((math.pow(x,b))%P))
   #s.send(kb.encode('utf-8'))

   ka=s.recv(1024).decode('utf-8')
   
   if ka==kb:
      print("Key excahnge successful")
      print("Key: ",kb)

   s.close()

if __name__ == "__main__":

     sys.exit(p2p_client())
