"""
hello_www.py - minimal web server + web application
"""

import socket 
import sys
import re

page = """
HTTP/1.0 200 OK
Content-Type text/html

<html>
<body>
Hello Brittany!!
%s
</body>
</html>
"""

host = '' 
port = 8082 # different default port than thirty_minute_webserver

# optional command line argument: port 
if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5 
size = 1024 

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'hello_www listening on port', port
s.listen(backlog) 

path = ""
while True: # just keep serving page to any client that connects
    client, address = s.accept() # create client socket
    data = client.recv(size) # HTTP request - not too big!  Just ignore contents
    print data 
    if data:
        # split data into a list
        data_list = data.split('\n')
        for line in data_list:
            # Looking for 

            if "GET" in line and "favicon.ico" not in line:
                print line
                # FIXME: This isn't working
                m = re.search('\s+?GET\s+.*', line)
                path = m.group(0)
                print "group: " + path 
                sys.exit(1)
                path = line
                path = path.lstrip("GET /")
                path = path.replace('HTTP/1.1', "")
                print "This is the only thing", path 

    client.send(page % ("scboyd: " + path)) # HTTP response - same for any request
    client.close()
