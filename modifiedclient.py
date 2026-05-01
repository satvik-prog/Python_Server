import socket as sck
HOST = "127.0.0.1"
PORT = 65432

with sck.socket(sck.AF_INET,sck.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    var = 0
    while var<5:
        s.sendall(b"{var}")
        var+=1
        data = s.recv(1024)
        print(f"Recieved {data!r}")
