import mysql.connector
import functions

dbConnect = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Admin123',
    'database': 'tienda'
}

# Conexión a la base de datos
konexioa = mysql.connector.connect(**dbConnect)

try:
    # Crear cursor
    kurtsorea = konexioa.cursor()
    
    # Obtener la consulta SQL de la función 'kontsultak'
    kontsulta1, kontsulta2, kontsulta3, kontsulta4, kontsulta5 = functions.kontsultak()
    
    # Ejecutar la consulta
    kurtsorea.execute(kontsulta1)
    
    # Obtener los resultados
    resultados = kurtsorea.fetchall()
    
    # Imprimir los resultados
    for fila in resultados:
        print(f"Nombre: {fila[0]}, Apellidos: {fila[1]}")
    kurtsorea.execute(kontsulta2)
    
    # Obtener los resultados
    resultados = kurtsorea.fetchall()
    
    # Imprimir los resultados
    for fila in resultados:
        print(f"Nombre: {fila[0]}, Telefono: {fila[1]}")
    kurtsorea.execute(kontsulta3)

    resultados = kurtsorea.fetchall()

    for fila in resultados:
        print(f"Nombre: {fila[0]}, Apellidos: {fila[1]}")
    
    kurtsorea.execute(kontsulta4)

    resultados = kurtsorea.fetchall()

    for fila in resultados:
        print(f"Producto: {fila[0]}, Unidades en stock: {fila[1]}")
    kurtsorea.execute(kontsulta5)

    resultados = kurtsorea.fetchall()

    for fila in resultados:
        print(f"Producto: {fila[0]}, Descripción: {fila[1]}, Imagen: {fila[2]}")

except mysql.connector.Error as err:
    print(f"Ocurrió un error: {err}")
   
finally:
    # Cerrar la conexión
    if konexioa.is_connected():
        kurtsorea.close()
        konexioa.close()
        print("Conexión cerrada.")
