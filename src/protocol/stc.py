"""
server -> client
"""

from src.protocol.proto import Status, SEPARATOR


def parse(incoming):
    payload = incoming.split(SEPARATOR)
    if len(payload) != 2:
        return (Status.WRONG_FORMAT, payload)
    return (None, payload)


def build(code=Status.OK, data=''):
    return f'{code.value}{SEPARATOR}{data}'


def ok(data):
    return build(Status.OK, data)


def no_path():
    return build(Status.NO_PATH, 'Path not found')


def wrong_format():
    return build(Status.WRONG_FORMAT, 'Malformed incoming message')


def no_origin():
    return build(Status.NO_NODE, 'Origin not found')


def no_destination():
    return build(Status.NO_NODE, 'Destination not found')
