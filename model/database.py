"""This module defines everything that is needed for the database."""

import sqlite3
from config import DB_PATH


class Database:
    """This class defines the Database."""

    def __init__(self, db=DB_PATH):
        """This is the constructor of the Database."""
        self._db = db
        self.create_tables()

    def connect(self):
        """This method connects to the database."""
        conn = sqlite3.connect(self._db)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def create_tables(self):
        """This method creates the tables in the database. Further tables can be added here."""
        self.create_user_table()
        self.create_water_log_table()

    # Here are the user related methods.
    def create_user_table(self):
        """This method creates a users table"""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                       user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_name TEXT NOT NULL,
                       date_of_birth TEXT NOT NULL,
                       height INTEGER NOT NULL CHECK(height > 0 AND height <= 250),
                       gender TEXT NOT NULL CHECK(gender IN ('m', 'f', 'd')),
                       fitness_lvl TEXT NOT NULL CHECK(fitness_lvl IN ('beginner', 'intermediate', 'advanced'))
            )"""
        )
        conn.commit()
        conn.close()

    def add_user(self, name, birthdate, height_in_cm, gender, fitness_lvl):
        """This method adds a user to the db."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (user_name, date_of_birth, height,  gender, fitness_lvl) VALUES (?, ?, ?, ?, ?)",
            (name, birthdate, height_in_cm, gender, fitness_lvl),
        )
        conn.commit()
        conn.close()

    def get_user(self, name) -> list:
        """This method retrieves a user from database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return row

    def delete_user(self, name) -> list:
        """This method deletes a user from database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE user_name = ?", (name,))
        row = cursor.fetchone()
        conn.commit()
        conn.close()
        return row

    # Here are the waterlog related methods.

    def create_water_log_table(self):
        """This method creates the water logs table in the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS water_logs (
                       water_log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id INTEGER NOT NULL,
                       amount_in_ml INTEGER NOT NULL,
                       timestamp TEXT NOT NULL,
                       FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            )"""
        )
        conn.commit()
        conn.close()

    def add_water_log(self, user_id, amount_in_ml, timestamp):
        """This method adds a water logs to the database. Code partly AI-generated."""
        conn = self.connect()
        cursor = conn.cursor()
        # The '?' is a placeholder.
        cursor.execute(
            "INSERT INTO water_logs (user_id, amount_in_ml, timestamp) VALUES (?, ?, ?)",
            (user_id, amount_in_ml, timestamp),
        )
        conn.commit()
        conn.close()

    def get_all_water_logs(self) -> list:
        """This method retrieves all water logs from the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM water_logs")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_water_log(self, water_log_id) -> list:
        """This method deletes a water log from the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM water_logs WHERE water_log_id = ?", (water_log_id,))
        row = cursor.fetchone()
        conn.commit()
        conn.close()
        return row
