import socket

import src.protocol.cts as proto

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.connect(('127.0.0.1', 3000))
        connection.send(proto.build("info3", "smartlab").encode())
        res = connection.recv(1024)
        print(res.decode())
