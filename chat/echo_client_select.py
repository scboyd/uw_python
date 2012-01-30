"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""

import socket 
import sys
import select
import time

host = 'localhost' 
port = 50000 
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 

s.connect((host,port)) 

timeout = 10
input = [s, sys.stdin]

running = True

while running:
    inputready,outputready,exceptready = select.select(input, [], [], timeout)
    
    # 'Client timeout'
    if not inputready:
        pass

    for sock in inputready:
     
        # If the sever is sending us something
        if sock == s:
            data = s.recv(size)
            if data:
                print '[Data Received] from (%s, %s) %s' % (host, port, data) 
            else:
                inputready.remove(sock)

        # handle standard input --> send to server
        elif sock == sys.stdin:
            data = sys.stdin.readline().strip('\n')
            if not data:
                print "Closing connection"
                running = False
            else:
                s.send(data)
                inputready.remove(sock)


s.close()
