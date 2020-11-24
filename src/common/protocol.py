"""
Protocol definition
"""

from enum import Enum
SEPARATOR = ','


class Codes(Enum):
    OK = '0.0'
    NO_PATH = '1.1'
    NO_NODE = '1.2'
    WRONG_FORMAT = '2.1'


def parse(incoming):
    payload = incoming.split(SEPARATOR)
    if len(payload) != 2:
        return (Codes.WRONG_FORMAT, payload)
    return (None, payload)


def build(code=Codes.OK, data=''):
    return f'{code.value}{SEPARATOR}{data}'


def ok(data):
    return build(Codes.OK, data)


def no_path():
    return build(Codes.NO_PATH, 'Path not found')


def wrong_format():
    return build(Codes.WRONG_FORMAT, 'Malformed incoming message')


def no_origin():
    return build(Codes.NO_NODE, 'Origin not found')


def no_destination():
    return build(Codes.NO_NODE, 'Destination not found')
