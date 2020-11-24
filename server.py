"""
"""

from src.server.medium import TCP
from src.server.brain import execute
from src.common.protocol import parse

if __name__ == "__main__":
    with TCP('127.0.0.1', 3000) as connection:
        @connection.listen
        def handler(incoming):
            cmd = parse(incoming)
            return execute(cmd)
