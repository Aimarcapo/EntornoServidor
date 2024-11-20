def taulak_sortu():
    
    instrucciones = []

    ikasleak = f"CREATE TABLE Ikasleak (Ikasle_kodea INTEGER PRIMARY KEY AUTO_INCREMENT, Izena TEXT, Abizena TEXT)"
    instrucciones.append(ikasleak)
    ikasgaiak = f"CREATE TABLE Ikasgaiak (Ikasgai_kodea INTEGER PRIMARY KEY AUTO_INCREMENT, Izena TEXT, Maila TEXT, Hizkuntza TEXT)"
    instrucciones.append(ikasgaiak)
    notak = """
        CREATE TABLE Notak (
            Nota INTEGER,
            Oharra TEXT,
            Ikasgai_kodea INTEGER,
            Ikasle_kodea INTEGER,
            FOREIGN KEY (Ikasgai_kodea) REFERENCES Ikasgaiak (Ikasgai_kodea),
            FOREIGN KEY (Ikasle_kodea) REFERENCES Ikasleak (Ikasle_kodea)
        )
        """
    instrucciones.append(notak)
    return ";\n".join(instrucciones) + ";"
def datuak_hasieratu():
    instrucciones = []
    instrucciones_val = []
    ikasleak = f"INSERT INTO Ikasleak (Izena, Abizena) VALUES(%s, %s)"
    ikasleak_val=["Aimar", "Alonso"]
    instrucciones.append(ikasleak)
    instrucciones_val.append(ikasleak_val)
    ikasgaiak = f"INSERT INTO Ikasgaiak (Izena, Maila, Hizkuntza) VALUES(%s, %s, %s)"
    ikasgaiak_val=["Matematika", "Bigarren maila","Euskera"]
    instrucciones.append(ikasgaiak)
    instrucciones_val.append(ikasgaiak_val)
    notak = f"INSERT INTO Notak (Nota, Oharra) VALUES(%s, %s)"
    notak_val=[8,"Oso ongi"]
    instrucciones.append(notak)
    instrucciones_val.append(notak_val)
   
    return instrucciones,instrucciones_val
def taula_ezabatu():
    instrucciones = []
    notak = "DROP TABLE Notak"
    instrucciones.append(notak)
    ikasleak = f"DROP TABLE Ikasleak"
    instrucciones.append(ikasleak)
    ikasgaiak = f"DROP TABLE Ikasgaiak"
    instrucciones.append(ikasgaiak)
    return ";\n".join(instrucciones) + ";"
def ikasle_berria_gehitu(izena,abizena):
     ikasleak = f"INSERT INTO Ikasleak (Izena, Abizena) VALUES(%s, %s)"
     values=(izena,abizena)
     return ikasleak, values
def ikasle_nota(nota,oharra, ikasle_kodea, ikasgai_kodea):
     notak = f"INSERT INTO Notak (Nota, Oharra, Ikasle_kodea, Ikasgai_kodea) VALUES(%s, %s, %s, %s)"
     values=(nota,oharra, ikasle_kodea, ikasgai_kodea)
     return notak, values
def ikasle_nota_aldatu(nota,oharra, ikasle_kodea, ikasgai_kodea):
    notak="UPDATE Notak SET Nota = %s WHERE Oharra = %s AND Ikasle_kodea = %s AND Ikasgai_kodea = %s"
    values = (nota,oharra, ikasle_kodea, ikasgai_kodea)
    return notak, values
def ikasgai_berria(izena, maila,hizkuntza):
     notak = f"INSERT INTO Ikasgaiak (Izena, Maila, Hizkuntza) VALUES(%s, %s, %s)"
     values=(izena, maila,hizkuntza)
     return notak, values
def ikasle_ezabatu(izena,abizena):
    notak="DELETE FROM Ikasleak WHERE Izena = %s AND Abizena = %s"
    values = (izena,abizena)
    return notak, values