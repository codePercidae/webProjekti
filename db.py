import sqlite3
from flask import g #why tho?

def get_connection():
    db = sqlite3.connect("boulder.db")
    db.execute("PRAGMA foreign_keys = ON")
    db.row_factory = sqlite3.Row
    return db

def exec(sql, params=[]):
    db = get_connection()
    res = db.execute(sql, params)
    db.commit()
    g.last_insert_id = res.lastrowid
    db.close()
