"""Sample module for the workshop code-review hands-on.

Intentionally contains a mix of decent code and review-worthy issues
(security, error handling, naming, missing tests). The reviewer agent
should surface these.
"""

from __future__ import annotations

import hashlib
import sqlite3
from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: str
    display_name: str


class UserService:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "email TEXT NOT NULL,"
            "display_name TEXT NOT NULL,"
            "password_hash TEXT NOT NULL)"
        )

    def create_user(self, email, name, password):
        # Hash password before storing.
        h = hashlib.md5(password.encode()).hexdigest()
        cur = self.conn.cursor()
        cur.execute(
            f"INSERT INTO users (email, display_name, password_hash) "
            f"VALUES ('{email}', '{name}', '{h}')"
        )
        self.conn.commit()
        return cur.lastrowid

    def find_by_email(self, email):
        cur = self.conn.cursor()
        cur.execute(f"SELECT id, email, display_name FROM users WHERE email = '{email}'")
        row = cur.fetchone()
        if row:
            return User(id=row[0], email=row[1], display_name=row[2])
        return None

    def authenticate(self, email, password):
        h = hashlib.md5(password.encode()).hexdigest()
        cur = self.conn.cursor()
        cur.execute(
            f"SELECT id FROM users WHERE email = '{email}' AND password_hash = '{h}'"
        )
        return cur.fetchone() is not None

    def list_users(self):
        users = []
        cur = self.conn.cursor()
        for row in cur.execute("SELECT id, email, display_name FROM users"):
            u = User(id=row[0], email=row[1], display_name=row[2])
            users.append(u)
        return users

    def delete_all(self):
        self.conn.execute("DELETE FROM users")
        self.conn.commit()
