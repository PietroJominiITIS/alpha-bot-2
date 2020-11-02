"""
Decision-making entity
"""

import protocol as proto
from db import Db


def execute(cmd):
    status, payload = cmd
    if status == proto.Codes.WRONG_FORMAT:
        return proto.wrong_format()

    origin, destination = payload
    with Db() as db:
        paths = db.paths(origin, destination)
        if len(paths) > 0:
            return proto.ok(paths[0])

        places = db.places()
        if not origin in places:
            return proto.no_origin()
        if not destination in places:
            return proto.no_destination()

        return proto.no_path()
