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


kurtsorea = konexioa.cursor()
while True:
    print("1-Ikasle berri bat gehitu")
    print("2-Ikasle batek ikasgai batean duen nota sartu")
    print("3-Ikasle batek ikasgai batean duen nota aldatu")
    print("4-Ikasgai berri bat sartu")
    print("5-Ikasle bat ezabatu")
    try:
        aukera=int(input("Sartu zenbaki bat (1-6)"))
    except:
         print("Zenbaki bat sartu behar duzu")
    else:
        if aukera>5 or aukera<1:
             print("Zenbakia 1etik 6ra artean egon behar da")
        else:
             if aukera==1:
                  izena=input("Sartu ikasle berriaren izena:")
                  abizena=input("Sartu ikasle berriaren abizena:")
                  ikasleak,values=hasieratzea.ikasle_berria_gehitu(izena,abizena)
                  kurtsorea.execute(ikasleak,values)
                  konexioa.commit()
                  break
             elif aukera==2:
                    ikasle_kodea = int(input("Ikasle kodea: "))
                    ikasgai_kodea = int(input("Ikasgai kodea: "))
                    nota = int(input("Nota: "))
                    oharra = input("Oharra (optional): ")
                    notak, values=hasieratzea.ikasle_nota(nota, oharra, ikasle_kodea,ikasgai_kodea)
                    kurtsorea.execute(notak,values)
                    konexioa.commit()
                    break
             elif aukera==3:
                    nota = int(input("Ikaslearen nota berria: "))
                    ikasle_kodea = int(input("Ikaslearen kodea: "))
                    ikasgai_kodea = int(input("Ikasgai kodea: "))
                    oharra = input("Oharra (optional): ")
                    notak, values=hasieratzea.ikasle_nota_aldatu(nota, oharra, ikasle_kodea,ikasgai_kodea)
                    kurtsorea.execute(notak,values)
                    konexioa.commit()
                    break
             elif aukera==4:
                    izena = input("Ikasgaiaren izena: ")
                    maila = input("Maila: ")
                    hizkuntza = input("Hizkuntza: ")
                    notak, values=hasieratzea.ikasgai_berria(izena, maila, hizkuntza)
                    kurtsorea.execute(notak,values)
                    konexioa.commit()
                    break
                  
             elif aukera==5:
                  izena=input("Sartu ezabatu nahi duzun ikaslearen izena:")
                  abizena=input("Sartu ezabatu nahi duzun ikaslearen abizena:")
                  ikasleak,values=hasieratzea.ikasle_ezabatu(izena,abizena)
                  kurtsorea.execute(ikasleak,values)
                  konexioa.commit()
                  break
                
if konexioa.is_connected():
        kurtsorea.close()
        konexioa.close()
        print("Conexión cerrada.")


    