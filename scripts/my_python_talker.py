import sys
import socket
import time
import Message
import pickle
from threading import Thread, Event



class Talker(Thread):
   
   def __init__(self):      
      print "************ Talker ************"
      self.event = Event()
      self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      Thread.__init__(self)

   def run(self):
      while not self.event.is_set():
         try:
            self.s.connect(('localhost', 55000))
            while 1:
               m = Message.Message(raw_input("message:"))
               self.s.send(pickle.dumps(m))              
         except socket.error:
            time.sleep(1)

   def stop(self):
      m = Message.Message()
      m.set_f_end()
      self.s.send(pickle.dumps(m))
      self.s.close()
      self.event.set()

if __name__ == '__main__':
   t = Talker()
   t.start()
   try:
      while 1:
         time.sleep(1)
   except KeyboardInterrupt:
      t.stop()
      sys.exit()
