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
    sql = 'INSERT INTO users VALUES (?, ?, ?)'
    c.execute(sql, datos)
    conn.commit()
    conn.close()

def traerDatos():
    conn = sqlite3.connect('datos.db')
    c = conn.cursor()
    sql = 'SELECT * FROM users'
    res = [datos for datos in c.execute(sql)]
    conn.close()
    return res