import socket
import os
import sys
 
network = 'chat.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK piratecd\r\n' )
irc.send ( 'USER jjt jjt jjt :just a fskin decoy\r\n' )
irc.send ( 'JOIN #batibot\r\n' )
irc.send ( 'PRIVMSG #batibot :Hello World.\r\n' )
while True:
   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( '!quit' ) != -1:
      irc.send ( 'PRIVMSG #batibot :Fine, if you do not want me\r\n' )
      irc.send ( 'QUIT\r\n' )
   if data.find ( 'lol' ) != -1:
      irc.send ( 'PRIVMSG #batibot :Gay\r\n' )
   if data.find ('!uname') != -1:
      os.system("uname -a > /tmp/tempt.txt")
      a = open("/tmp/tempt.txt")
      uname = a.read()
      uname.replace("\r \n", "_")
      a.close()
      irc.send ('PRIVMSG #batibot :' +uname+ '\r\n')  
   print data 
