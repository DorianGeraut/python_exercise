import sys
import socket
import signal
from threading import Thread

class Connexion(Thread):
   
   def __init__(self,conn_sock):
      print "connection established"
      self.conn_sock=conn_sock
      Thread.__init__(self)


   def run(self):
      print "connection running"
      try:
         while 1:
         #Wait for a message from client
            buff = self.conn_sock.recv(1024)
            if len(buff) > 0:
               if buff=="CLOSE_CONNECTION":
                  break
               else:
                  print buff
   
      except KeyboardInterrupt:
         print "connection recieved Keyboard Interrupt!"
      
      print "connection ended ",self.conn_sock.fileno()
      self.conn_sock.close()

class Printer(object):

   def __init__(self):
   
      print "************ Printer ************"
      self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.s.bind(('', 55000))
      self.s.listen(5)
      
      while 1:
         conn_sock, addr = self.s.accept()
         try:
            c = Connexion(conn_sock)
            c.start()
         except KeyboardInterrupt:
            sys.exit()
if __name__ == '__main__':
   p = Printer()
