import os
import sys
import socket
import signal
from threading import Thread, current_thread
import Message
import pickle

class Connexion(Thread):
   
   def __init__(self,conn_sock):
      self.conn_sock=conn_sock
      Thread.__init__(self)

   def run(self):
      print "connection running"
      while 1:
      #Wait for a message from client
         buff = self.conn_sock.recv(1024)
         try:
            message = pickle.loads(buff)
            if len(buff) > 0:
               if message.get_f_end() == True:
                  break
               else:
                  print message.m
         except EOFError:
            continue
      print "connection ended ",self.conn_sock.fileno()
      self.conn_sock.close()

   def get_pid(self):
      return os.getpid()

class Printer(object):

   def __init__(self):   
      print "************ Printer ************"
      self.connections_ids = []
      self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.s.bind(('', 55000))
      self.s.listen(5)
      try: 
         while 1:
            conn_sock, addr = self.s.accept()
            c = Connexion(conn_sock)
            c.start()
            self.connections_ids.append(c.get_pid())
      except KeyboardInterrupt: 
         for c in self.connections_ids:
            print c
            os.kill(c,signal.SIGTERM)
            exit()

if __name__ == '__main__':
   p = Printer()
