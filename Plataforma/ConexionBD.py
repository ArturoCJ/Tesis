import mysql.connector

db = mysql.connector.connect( #crea conexion con la base de datos
    host = 'localhost', #IP host donde se aloja de db
    user = 'root', #usuario con el que se conectará
    password = '12345678', #contraseña del usuario
    database = 'plataforma' #base de datos a acceder
)

cursor = db.cursor()
"""cursor.execute('INSERT INTO lecturas(fecha_lectura) VALUES(NOW())') #ejecuta sentencia de mysql
db.commit()
cursor.execute('SELECT * FROM lecturas')
resultado = cursor.fetchall() #guarda en resultado lo arrojado por la instruccion anterior
print(resultado) #imprime resultado"""
cursor.execute('SELECT id_lectura FROM lecturas ORDER BY id_lectura DESC LIMIT 1')
resultado = cursor.fetchone() #guarda en resultado lo arrojado por la instruccion anterior
print(resultado[0])
