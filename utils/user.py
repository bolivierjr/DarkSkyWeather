import os
import logging
import sqlite3
from typing import Tuple, Union


log = logging.getLogger(__name__)


class UserInfo:
    """
    A users info stored in the db.
    """

    fullpath: str = os.path.dir(os.path.abspath(__file__))
    db: str = f"{fullpath}/../data/{os.getenv('DB_NAME')}"
    table: str = os.getenv("DB_TABLE")

    def __init__(self, irc, **kwargs):
        self.conn = self._connect()
        self.irc = irc
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def get(self) -> Tuple:
        log.info("Getting user info from database.")
        sql: str = """ """
        cursor = self.conn.cursor()
        cursor.execute(sql())

    def set(self) -> None:
        pass

    def _connect(self) -> Union[sqlite3.Connection, None]:
        try:
            if not os.path.isfile(self.db):
                self._create_database()
                return None

            log.info("Connecting to the SQLite3 database.")
            conn = sqlite3.connect(self.db)

            return conn

        except sqlite3.Error as err:
            log.error(err)
            self.irc.reply("There seems to be an error. Contact the admin.")

    def _create_database(self) -> None:
        self.irc.reply("No database found. Creating a new database...")

        conn = None

        try:
            log.info("Connecting to SQLite3 database.")
            conn: sqlite3.Connection = sqlite3.connect(self.db)
            cursor: sqlite3.Cursor = conn.cursor()

            sql: str = f"""CREATE TABLE IF NOT EXISTS {self.table} (
                        id INTEGER PRIMARY KEY,
                        nick TEXT NOT NULL,
                        host TEXT NOT NULL,
                        units INTEGER NOT NULL,
                        location TEXT NOT NULL,
                        channel TEXT NOT NULL,
                        timestamp INT DEFAULT NULL);"""

            cursor.execute(sql)
            conn.commit()
            cursor.close()
            log.info("Database created.")

        except sqlite3.Error as err:
            log.error(err)

        finally:
            if conn is not None:
                conn.close()
                log.info("Database connection closed.")

    def __del__(self):
        if self.conn is not None:
            log.info("Database connection closed.")
            self.conn.close()
