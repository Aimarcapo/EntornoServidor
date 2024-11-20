import sqlite3
import mysql.connector
import hasieratzea

dbConnect = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Admin123',
    'database': 'proba'
}

konexioa = mysql.connector.connect(**dbConnect)

try:
    kurtsorea = konexioa.cursor()
    
    # Crear tablas
    sql = hasieratzea.taulak_sortu()
    for statement in sql.split(';'):
        if statement.strip():  # Verifica que la sentencia no esté vacía
            kurtsorea.execute(statement)
    
    konexioa.commit()
    print("Tablas creadas con éxito.")
    
    # Insertar datos
    instrucciones, valores = hasieratzea.datuak_hasieratu()
    for instruccion, valor in zip(instrucciones, valores):
        kurtsorea.execute(instruccion, valor)
    
    konexioa.commit()
    print("Datos insertados con éxito.")

except mysql.connector.Error as err:
    print(f"Ocurrió un error: {err}")
instrucciones, valores = hasieratzea.datuak_hasieratu()
for instruccion, valor in zip(instrucciones, valores):
        kurtsorea.execute(instruccion, valor)
    
        konexioa.commit()
print("Datos insertados con éxito.")
while True:
    ezabatu=input("Ezabatu nahi dituzu taula eta datu guztiak?")
    if ezabatu=="Bai":
        sql = hasieratzea.taula_ezabatu()
        for statement in sql.split(';'):

            if statement.strip(): 

                kurtsorea.execute(statement)

        konexioa.commit()

        print("Tablas creadas con éxito.")
        
        break

    elif ezabatu=="Ez":
         break
    
    else:
         print("Zenbaki bat sartu behar duzu")

         
if konexioa.is_connected():
        kurtsorea.close()
        konexioa.close()
        print("Conexión cerrada.")


    