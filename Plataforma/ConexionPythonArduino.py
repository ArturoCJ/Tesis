import serial
import time
from datetime import datetime
import mysql.connector

db = mysql.connector.connect( #crea conexion con la base de datos
    host = 'localhost', #IP host donde se aloja de db
    user = 'root', #usuario con el que se conectará
    password = '12345678', #contraseña del usuario
    database = 'plataforma' #base de datos a acceder
)

### Zona de declaracion de variables

serialConection = serial.Serial('COM3', 9600) #abre conexión serial
data = [] #genera lista para almacear datos recibidos

####
runTime = int(1)

cursor = db.cursor()
cursor.execute('INSERT INTO lecturas(fecha_lectura) VALUES(NOW())') #ejecuta sentencia de mysql
db.commit()
cursor.execute('SELECT id_lectura FROM lecturas ORDER BY id_lectura DESC LIMIT 1')
resultado = cursor.fetchone() #guarda en resultado lo arrojado por la instruccion anterior
fk = resultado[0]

time.sleep(2)

begTime = datetime.now()

#ciclo mientras diferencia sea menor a tiempo de corrida
while (int(((datetime.now() - begTime).total_seconds())/60)) < runTime:
    sensorValue = float(serialConection.readline())    #Reconoce como decimal la medición hecha por el sensor
    cursor.execute('INSERT INTO mediciones(volts_medicion, lecturas_id) VALUES({}, {})'.format(sensorValue, fk))
    db.commit()
    #print(data)
    #print(sensorValue)
print("Lectura finalizada")

