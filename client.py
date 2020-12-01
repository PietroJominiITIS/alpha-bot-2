import socket
import time
from src.protocol import cts as proto
from src.client.alphabot.untimed import AlphaBotUntimed
from sys import argv

directions_map = {
    'B': lambda utb, am: utb.backward(am),
    'F': lambda utb, am: utb.forward(am),
    'R': lambda utb, am: utb.rotate(am),
    'L': lambda utb, am: utb.rotate(-1 * am),
}


def handle_path(path):
    utb = AlphaBotUntimed(_d_scale=3)
    for _, direction, amount in path:
        directions_map[direction](utb, int(amount))
    print('_d_ waiting for key')
    input()


def handle_error(status, msg):
    print(f'Error {status} :: {msg}')


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.connect(('127.0.0.1', 3000))
        connection.send(proto.build(argv[1], argv[2]).encode())
        status, data = proto.parse(connection.recv(1024).decode())
        if not status == proto.Status.OK:
            handle_error(status, data)
        else:
            handle_path(data)
