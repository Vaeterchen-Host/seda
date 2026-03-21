"""This is a test file for the database module."""

from model.database import Database


def test_database_connection():
    """This test checks if the database connection can be established."""
    db = Database(":memory:")  # Use an in-memory database for testing
    assert db is not None, "Connection should work"
