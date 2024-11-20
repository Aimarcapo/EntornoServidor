import sqlite3
import mysql.connector
import functions

dbConnect = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Admin123',
    'database': 'tienda'
}
konexioa = mysql.connector.connect(**dbConnect)
try:
    kurtsorea = konexioa.cursor()
    
    # Crear tablas
    sql = functions.taula_ezabatu()
    for statement in sql.split(';'):
        if statement.strip():  # Verifica que la sentencia no esté vacía
            kurtsorea.execute(statement)
    
    konexioa.commit()
   

except mysql.connector.Error as err:
    print(f"Ocurrió un error: {err}")
   
if konexioa.is_connected():
        kurtsorea.close()
        konexioa.close()
        print("Conexión cerrada.")

