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
    sql = functions.taulak_sortu()
    for statement in sql.split(';'):
        if statement.strip():  # Verifica que la sentencia no esté vacía
            kurtsorea.execute(statement)
    
    konexioa.commit()
    print("Tablas creadas con éxito.")
    num_clientes, num_articulos=functions.count_rows()
   
    clientes, articulos, compras, compras_data = functions.datuak_sartu()
    kurtsorea.execute(clientes)
    konexioa.commit()
    kurtsorea.execute(articulos)
    konexioa.commit()
    kurtsorea.executemany(compras, compras_data)
    konexioa.commit()

    
    print("Datos insertados con éxito.")

except mysql.connector.Error as err:
    print(f"Ocurrió un error: {err}")
   
if konexioa.is_connected():
        kurtsorea.close()
        konexioa.close()
        print("Conexión cerrada.")

