"""
"""

from src.server.medium import HTTP
from src.server.brain import execute
from src.protocol.stc import parse
from src.protocol.cts import build, parse as c_parse

if __name__ == "__main__":
    with HTTP("127.0.0.1", 3000) as connection:
        connection.url = "/<f>/<t>"

        @connection.listen
        def handler(f, t):
            cmd = parse(build(f, t))
            code, data = c_parse(execute(cmd))
            return dict(code=code.value, data=data)
