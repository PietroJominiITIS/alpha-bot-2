"""
sqlite abstraction layer
"""

import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "percorsi.db")


class Db():

    def __init__(self, path=DB_PATH):
        self.connection = sqlite3.connect(path)

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def places(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT nome
            FROM luoghi
        """)
        return [p[0] for p in cursor.fetchall()]

    def paths(self, start, end):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT 
                start.nome as start,
                end.nome as end,
                percorsi.percorso as percorso
            FROM inizio_fine
            INNER JOIN percorsi ON inizio_fine.id_percorso = percorsi.id
            INNER JOIN luoghi AS start ON inizio_fine.id_start = start.id
            INNER JOIN luoghi AS end ON inizio_fine.id_end = end.id
            WHERE start=? and end=?
        """, (start, end))
        return [p for _, _, p in cursor.fetchall()]

    def all(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT 
                start.nome as start,
                end.nome as end,
                percorsi.percorso as percorso
            FROM inizio_fine
            INNER JOIN percorsi ON inizio_fine.id_percorso = percorsi.id
            INNER JOIN luoghi AS start ON inizio_fine.id_start = start.id
            INNER JOIN luoghi AS end ON inizio_fine.id_end = end.id
        """)
        return {
            (orig, dest): path
            for orig, dest, path
            in cursor.fetchall()
        }
