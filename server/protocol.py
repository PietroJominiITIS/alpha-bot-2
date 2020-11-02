"""
Protocol definition
"""

"""
INCOMING

------------------------
| origin | destination |    ==>    origin;destination
------------------------

EXAMPLE:
rome;milan
3.0;SMART_LAB
"""

"""
OUTGOING

-----------------
| status | data |   ==>    status;data
-----------------

Status:
--------------
| OK? | DESC |   ==>    OK?.DESC
--------------          0.0 -> OK
                        0.1 -> OK :: No path
                        1.0 -> FAILED :: Wrong incoming format
                        1.1 -> FAIELD :: Origin not registered
                        1.2 -> FAILED :: Destination not registered
                        1.3 -> FAILED :: Server fault

Data:
0.1, 1.* -> None

       ----------------
0.0 -> | DIR | AMOUNT | (repeated)  ==>    DIR
       ----------------                      N -> Nord
                                             E -> Est
                                             S -> Sud
                                             W -> West 
                                           AMOUNT :: integer

EXAMPLE:
0.0;N10W200S15
1.2;
"""


from enum import Enum
SEPARATOR = ";"


class Codes(Enum):
    OK = '0.0'
    NO_PATH = '0.1'
    WRONG_FORMAT = '1.0'
    NO_ORIGIN = '1.1'
    NO_DESTINATION = '1.2'
    SERVER_FAULT = '1.3'


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
    return build(Codes.NO_PATH)


def wrong_format():
    return build(Codes.WRONG_FORMAT)


def no_origin():
    return build(Codes.NO_ORIGIN)


def no_destination():
    return build(Codes.NO_DESTINATION)


def server_fault():
    return build(Codes.SERVER_FAULT)
