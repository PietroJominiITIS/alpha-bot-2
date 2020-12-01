"""
client -> server
"""

from src.protocol.proto import SEPARATOR, Status
import re


def build(origin, destination):
    return f'{origin}{SEPARATOR}{destination}'


def parse(incoming):
    payload = incoming.split(SEPARATOR)
    if len(payload) != 2:
        return (Status.WRONG_FORMAT, payload)
    pmatches = re.findall(r'((\D)(\d+))', payload[1], re.IGNORECASE)
    if len(pmatches) == 0:
        return (Status.WRONG_FORMAT, payload)
    return (Status(payload[0]), pmatches)
