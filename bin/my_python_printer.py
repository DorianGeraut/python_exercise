import os
import sys
import socket
import signal


print "************ Printer ************"
print "pid: ",os.getpid()
print "uname(): ",os.uname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 55000))
s.listen(5)
conn, addr = s.accept()

while 1:
#Wait for a message from client
   buff = conn.recv(1024)
   if len(buff) > 0:
      if buff=="CLOSE_CONNECTION":
         break
      else:
         print buff
print "deconnection of client"
