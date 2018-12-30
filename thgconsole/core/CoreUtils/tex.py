import sqlite3
import os

conexoes = sqlite3.connect("../../thg.db")
cursor = conexoes.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
total = len(cursor.fetchall())
for i in  cursor.fetchall():
    print(i)