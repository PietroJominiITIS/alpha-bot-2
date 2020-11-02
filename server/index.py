"""
do
  . listen incoming -> medium
  . parse incoming  -> medium > brain
  . query results   -> medium > brain > db
  . format result   -> medium > brain
  . send result     -> medium
"""

from medium import TCP
from brain import execute
from protocol import parse

if __name__ == "__main__":
    with TCP('127.0.0.1', 3000) as connection:
        @connection.listen
        def handler(incoming):
            cmd = parse(incoming)
            return execute(cmd)
