import socket as sket
HOST = "127.0.0.1"
PORT = 65432

with sket.socket(sket.AF_INET,sket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept()
    with conn:
        print("Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
