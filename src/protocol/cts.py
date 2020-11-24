"""
client -> server
"""

from src.protocol.proto import SEPARATOR


def build(origin, destination):
    return f'{origin}{SEPARATOR}{destination}'
