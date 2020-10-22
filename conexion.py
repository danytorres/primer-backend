import sqlite3

#conn = sqlite3.connect('datos.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE users (nombre text, correo text, distancia real)''')
#c.execute("INSERT INTO users VALUES ('Daniel Torres','dtp_daniel@hotmail.com',10)")
#conn.commit()
#conn.close()

def insert(datos):
    conn = sqlite3.connect('datos.db')
    c = conn.cursor()
    c.execute('INSERT INTO users VALUES (?, ?, ?)', datos)
    conn.commit()
    conn.close()

def traerDatos():
    conn = sqlite3.connect('datos.db')
    c = conn.cursor()
    res = [datos for datos in c.execute('SELECT * FROM users')]
    conn.close()
    return res