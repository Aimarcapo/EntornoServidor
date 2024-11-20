from typing import Dict
f = open("jendea.txt", "r")
lines=f.readlines()

datu_zerrenda=[]
for line in lines:
    line=line.strip()
    if line:
        separado=line.split(";")
        hiztegia = dict(id=separado[0],izena=separado[1], abizena=separado[2],jaiotze_data=separado[3])
        #hiztegia.update({"id":separado[0],"izena":separado[1],"abizena":separado[2], "jaiotze-data":separado[3]})
        datu_zerrenda.append(hiztegia)
print(datu_zerrenda)
    