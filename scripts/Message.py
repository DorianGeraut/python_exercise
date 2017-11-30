import sys
import socket
import time
from threading import Thread, Event

class Message(object):

   def __init__(self,m):
      self.m = m
      self.t = time.time()
      self.f_end = False

   def __getitem__(self):
      return (self.m, self.t, self.f_end)

   def set_f_end(self):
      self.f_end = True
   
   def get_f_end(self):
      return self.f_end
