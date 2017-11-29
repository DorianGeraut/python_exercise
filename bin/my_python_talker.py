import os
import sys
import socket
import signal


class Talker(object):
   
   def __init__(self):
      
      print "************ Talker ************"
      self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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


if __name__ == '__main__':
   t = Talker()
