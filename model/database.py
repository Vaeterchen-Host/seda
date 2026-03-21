"""This module defines everything that is needed for the database."""

import sqlite3
from config import DB_PATH


class Database:
    """This class defines the Database."""

    def __init__(self, db=DB_PATH(initialize=True)):
        """This is the constructor of the Database."""
        self._db = db

    def connect(self):
        """This method connects to the database."""
        conn = sqlite3.connect(self._db)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def create_tables(self):
        """This method creates the tables in the database. Further tables can be added here."""

    # Here are the waterlog related methods.

    def add_water_log(self, id, amount_in_ml, timestamp):
        """This method adds a water log to the database. Code partly AI-generated."""
        conn = self.connect()
        cursor = conn.cursor()
        # The '?' is a placeholder.
        cursor.execute(
            "INSERT INTO water_log (id, amount_in_ml, timestamp) VALUES (?, ?, ?)",
            (id, amount_in_ml, timestamp),
        )
        conn.commit()
        conn.close()

    def get_all_water_logs(self) -> list:
        """This method retrieves all water logs from the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM water_log")
        rows = cursor.fetchall()
        conn.close()
        return rows
