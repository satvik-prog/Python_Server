import socket
import sys
import os

s = socket.socket()
port = int(sys.argv[1])
s.bind(('',port))
s.listen()
while True:
    new_conn,addr = s.accept()
    request_data = new_conn.recv(4096)#estimated this because there is no payload
    request_data_decoded = request_data.decode("ISO-8859-1")
    request_split = request_data_decoded.split()
    file_path = request_split[1]
    file_name = os.path.split(file_path)[-1]
    extension_type = os.path.splitext(file_name)[-1]
    if extension_type == '.txt':
        content = "text/plain"
    else :
        content = "text/html"

    try:
        with open(file_name,"rb") as fp:
            file_data = fp.read()
            response_header = "HTTP/1.1 200 OK"
            final_line = file_data.decode("ISO-8859-1")
    except:
        response_header = "HTTP/1.1 404 Not Found"
        final_line = "404 not found"
        file_data = b'404 not found'
    content_length = len(file_data)
    response = response_header + "\r\n" + "Content-Type: " + content + "\r\n" + "Content-length: " + str(content_length) + "\r\n" + "Connection: close" + "\r\n\r\n" + final_line 
    new_conn.sendall(response.encode())
    new_conn.close()

