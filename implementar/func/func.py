import sqlite3
import os.path
def createdb():
    con = sqlite3.connect("thg_test.db")
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE agenda(
        "nome" text, 
        "numero" text
    )''')
    cursor.execute('''insert into agenda (nome,numero)
        values(?,?)''',("dsa","1111111"))
    con.commit()
    cursor.close()
    con.close()
def listdb():
    con = sqlite3.connect("thg_test.db")
    cursor = con.cursor()
    cursor.execute("select * from agenda")
    resul = cursor.fetchone()
    print("nome:%s\ntelefone:%s "% (resul))
createdb()
listdb()