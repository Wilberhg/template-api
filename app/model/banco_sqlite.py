from contextlib import contextmanager
from typing import Union
import sqlite3
import sys

class Banco:

    def __init__(self, file: str = 'usuarios.db', table: str = 'TB_Cliente'):
        self.file = file
        self. table = table

    @contextmanager
    def _open_db_connection(self, commit: bool = False) -> sqlite3.Cursor:
        conn = sqlite3.connect(self.file)
        cursor = conn.cursor()
        try:
            yield cursor
        except sqlite3.DatabaseError as err:
            error, = err.args
            sys.stderr.write(error.message)
            cursor.execute('ROLLBACK')
            raise err
        else:
            if commit:
                cursor.execute('COMMIT')
            else:
                cursor.execute('ROLLBACK')
        finally:
            cursor.close()
            conn.close()

    def do_select(self, queries: Union[str, list]) -> list:
        try:
            with self._open_db_connection() as cursor:
                if type(queries) == list:
                    for query in queries:
                        cursor.execute(query)
                else:
                    cursor.execute(queries)
                result = cursor.fetchall()
        except:
            result = []
        return result

    def do_insert_update(self, query: str, values: Union[str, list] = None) -> bool:
        try:
            with self._open_db_connection(commit=True) as cursor:
                if values:
                    cursor.executemany(query, values)
                else:
                    cursor.execute(query)
            return True
        except:
            return False