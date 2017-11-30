import sys
import socket
import time
from threading import Thread, Event

class Message(object):

   def __init__(self,*args):
      if len(args) >= 1:
         self.m = args[0]
      else:
         self.m = None
      if len (args) >= 2:
         self.f_end = args[1]
      else:
         self.f_end = False
      self.t = time.time()

   def __getitem__(self):
      return (self.m, self.t, self.f_end)

   def set_f_end(self):
      self.f_end = True
   
   def get_f_end(self):
      return self.f_end
