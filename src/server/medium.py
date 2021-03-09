"""
Connection medium abstraction layer
"""

import socket
from threading import Thread
from flask import Flask


class Medium:
    """"""

    def __init__(self):
        self.workers = []

    def listen(self, handler):
        self.listening = True
        try:
            self.listener(handler)
        except KeyboardInterrupt:
            return
        except Exception as e:
            self.on_error(e)

    def worker(self, target):
        worker = Thread(target=target)
        self.workers.append(worker)
        worker.start()

    def open(self):
        """Dummy"""
        pass

    def close(self):
        self.listening = False
        for worker in self.workers:
            worker.join()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def listener(self, handler):
        """ Dummy """
        pass

    def on_error(self, error):
        """ Dummy """
        pass


class TCP(Medium):
    """"""

    def __init__(self, address, port):
        super().__init__()
        self.address = address
        self.port = port

    def open(self):
        super().open()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.address, self.port))
        self.sock.listen()

    def close(self):
        super().close()
        self.sock.close()

    def listener(self, handler):
        while self.listening:
            conn, client = self.sock.accept()

            @self.worker
            def handle_connection():
                data = conn.recv(1024)
                result = handler(data.decode())
                conn.send(result.encode())
                conn.close()

    def on_error(self, e):
        self.close()
        raise e


class HTTP(Medium):
    """"""

    def __init__(self, address, port):
        super().__init__()
        self.address = address
        self.port = port
        self.url = "/"

    def open(self):
        self.app = Flask(__name__)

    def listener(self, handler):
        self.app.route(self.url)(handler)
        self.app.run(self.address, self.port)
