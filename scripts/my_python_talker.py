import sys
import socket
import time
from threading import Thread

class Talker(Thread):
   
   def __init__(self):
      
      print "************ Talker ************"
      self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      Thread.__init__(self)

   def run(self):
      print "running"
      while 1:
         try:
            self.s.connect(('localhost', 55000))
            while 1:
               try:
                  m = raw_input("message:")
               except:
                  self.s.send("CLOSE_CONNECTION")
                  self.s.close()
                  break
               else:
                  self.s.send(str(m))              
         except socket.error:
            time.sleep(5)
            print "sleeping"

if __name__ == '__main__':
   t = Talker()
   t.start()
