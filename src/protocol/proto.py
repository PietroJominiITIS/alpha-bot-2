"""
Common proto
"""

from enum import Enum


class Status(Enum):
    OK = '0.0'
    NO_PATH = '1.1'
    NO_NODE = '1.2'
    WRONG_FORMAT = '2.1'
    CONNECTION_LOST = '3.1'
    SERVER_FAULT = '4.1'


SEPARATOR = ','
