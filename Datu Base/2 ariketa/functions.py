import random
def taulak_sortu():
    instrucciones = []

    # Crear tablas
    clientes = """
    CREATE TABLE IF NOT EXISTS CLIENTES (
        CodCliente INT PRIMARY KEY AUTO_INCREMENT,
        Nombre VARCHAR(255) NOT NULL,
        Apellidos VARCHAR(255),
        Empresa VARCHAR(255),
        Puesto VARCHAR(255),
        CP INT DEFAULT 20600,
        Provincia VARCHAR(255) DEFAULT 'Guipuzkoa',
        Telefono INT,
        FechaNacimiento DATETIME
    );
    """
    instrucciones.append(clientes)

    articulos = """
    CREATE TABLE IF NOT EXISTS ARTICULOS (
        CodArticulo INT PRIMARY KEY AUTO_INCREMENT,
        Nombre VARCHAR(255) NOT NULL,
        Descripcion VARCHAR(255) NOT NULL,
        PrecioUnidad DECIMAL(10, 2) NOT NULL,
        UnidadesEnStock INT,
        StockDeSeguridad INT,
        Imagen VARCHAR(255)
    );
    """
    instrucciones.append(articulos)

    compras = """
    CREATE TABLE IF NOT EXISTS COMPRAS (
        CodCliente INT,
        CodArticulo INT,
        Fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
        Unidades INT,
        PRIMARY KEY (CodCliente, CodArticulo),
        FOREIGN KEY (CodCliente) REFERENCES CLIENTES(CodCliente),
        FOREIGN KEY (CodArticulo) REFERENCES ARTICULOS(CodArticulo)
    );
    """
    instrucciones.append(compras)

    return ";\n".join(instrucciones) + ";"
def taula_ezabatu():
    instrucciones = []
    notak = "DROP TABLE COMPRAS"
    instrucciones.append(notak)
    ikasleak = f"DROP TABLE ARTICULOS"
    instrucciones.append(ikasleak)
    ikasgaiak = f"DROP TABLE CLIENTES"
    instrucciones.append(ikasgaiak)
    return ";\n".join(instrucciones) + ";"
def count_rows():
    clientes="SELECT COUNT(*) FROM CLIENTES;"
    articulos="SELECT COUNT(*) FROM ARTICULOS;"
    return clientes, articulos
def datuak_sartu():
    # Inserciones
    clientes = """
    INSERT INTO CLIENTES (Nombre, Apellidos, Empresa, Puesto, CP, Provincia, Telefono, FechaNacimiento) VALUES
    ('José', 'Fernández Ruiz', 'Estudio Cero', 'Gerente', 41400, 'Sevilla', 65678904, '1968-06-13'),
    ('Luis', 'Fernández Chacón', 'Beep', 'Dependiente', 41400, 'Sevilla', 67589456, '1982-05-24'),
    ('Antonio', 'Ruiz Gómez', 'Comar', 'Dependiente', 41400, 'Sevilla', 65434554, '1989-08-06'),
    ('Andrea', 'Romero Vázquez', 'Estudio Cero', 'Dependiente', 41400, 'Sevilla', 64676565, '1974-11-23'),
    ('José', 'Pérez Pérez', 'Beep', 'Gerente', 41400, 'Sevilla', 64534554, '1978-04-10');
    """

    articulos = """
    INSERT INTO ARTICULOS (Nombre, Descripcion, PrecioUnidad, UnidadesEnStock, StockDeSeguridad, Imagen) VALUES
    ('NETGEAR switch prosafe', 'Switch 8 puertos GigabitEthernet', 125.00, 3, 2, 'imagen1.jpg'),
    ('Switch SRW224G4-EU de Linksys', 'CISCO switch 24 puertos 10/100', 202.43, 2, 2, 'imagen2.jpg'),
    ('Switch Dlink', 'D-Link smart switch 16 puertos', 149.90, 7, 4, 'imagen3.jpg'),
    ('Switch Dlink', 'D-Link smart switch 48 puertos', 489.00, 4, 2, 'imagen4.jpg');
    """

    compras_data = [
    (1, 1, '2010-10-13', 2),  # Cliente 1, Artículo 1
    (1, 2, '2010-10-13', 1),
    (2, 3, '2010-10-15', 1),
    (2, 4, '2010-10-15', 1),
    (3, 1, '2010-10-15', 2),
    (4, 2, '2010-10-15', 1),
    (5, 3, '2010-10-15', 3),
    (1, 4, '2010-10-16', 1),  # Cliente 1, Artículo 4
    (2, 2, '2010-10-17', 1),
    (3, 3, '2010-10-18', 4),
    (4, 4, '2010-10-19', 2),
    (5, 1, '2010-10-19', 1)
    ]


    # Insertar datos en COMPRAS usando executemany
    compras = """
        INSERT INTO COMPRAS (CodCliente, CodArticulo, Fecha, Unidades)
        VALUES (%s, %s, %s, %s)
    """

    return clientes, articulos, compras,compras_data
def kontsultak():
    kontsulta1="SELECT Nombre, Apellidos FROM CLIENTES WHERE Nombre = 'José' OR Nombre = 'LUIS' ORDER BY Nombre ASC, Apellidos ASC"
    kontsulta2= """
    SELECT Nombre, Telefono 
    FROM CLIENTES 
    WHERE (YEAR(CURDATE()) - YEAR(FechaNacimiento)) BETWEEN 45 AND 50
    ORDER BY (YEAR(CURDATE()) - YEAR(FechaNacimiento)) ASC;
    """
    kontsulta3="""
    SELECT Nombre, Apellidos 
    FROM CLIENTES 
    WHERE Telefono IS NULL;
    """
    kontsulta4="""
    SELECT Nombre, UnidadesEnStock 
    FROM ARTICULOS 
    WHERE UnidadesEnStock < 4;
    """
    kontsulta5="""
    SELECT Nombre, Descripcion, Imagen 
    FROM ARTICULOS 
    WHERE PrecioUnidad < 200;
    """
    return kontsulta1, kontsulta2, kontsulta3, kontsulta4, kontsulta5