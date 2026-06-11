import socket
import sys

s = socket.socket()
host = sys.argv[1]
port = int(sys.argv[2])

s.connect((host,port))
request = "GET /foo/dummy/file2.html HTTP/1.1\r\nHost: " + host + "localhost\r\nConnection: close\r\n\r\n"
s.sendall((request.encode()))
data = b""
while True:
    tempdata = s.recv(4096)
    if len(tempdata) == 0:
        break
    data = data + tempdata
    print(data.decode("ISO-8859-1"))
#later write the code for parsing the file contents from data