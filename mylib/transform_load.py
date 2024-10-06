"""
Transforms and Loads data into the local SQLite3 database
"""

import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/gradstudents.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("gradstudentsDB.db")
    c = conn.cursor()
    c.execute(
        "SELECT Major, Major_category, Grad_total, Grad_employed FROM gradstudentsDB"
    )
    c.execute("DROP TABLE IF EXISTS gradstudentsDB")
    c.execute(
        """
        CREATE TABLE gradstudentsDB (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Major TEXT,
            Major_category TEXT,
            Grad_total INTEGER,
            Grad_employed INTEGER
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO gradstudentsDB (
            Major, 
            Major_category, 
            Grad_total, Grad_employed
            ) 
            VALUES (?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "gradstudentsDB.db"
