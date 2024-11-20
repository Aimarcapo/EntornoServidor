def telefonoa_existitu():
     try:
         f = open("listin.txt", "x")
         f.close()
     except:
        print("Existitzen da")
        
def telefonoa_kontsultatu(zenbakia):
    f = open("listin.txt", "r")
    lines=f.readlines()
    aurkituta=0
    for line in lines:
       
        line=line.strip()
        line=line.split(",")
        
        if int(line[0])==zenbakia:
           aurkituta=1
           print(line)
    if aurkituta==0:
        print("Ez da aurkitu")
    f.close()

def telefono_berria(zenbakia, izena):
    with open("listin.txt", "a") as f:
        f.write(f"{zenbakia},{izena}\n")
def telefonoa_ezabatu(zenbakia, izena):
    datu_zerrenda = []
    
    # Abrimos el archivo en modo lectura para obtener las líneas
    with open("listin.txt", "r") as f:
        lines = f.readlines()
    
    # Procesamos cada línea
    for line in lines:
        emaitza = line.strip()  # Elimina espacios en blanco
        line_data = emaitza.split(",")  # Divide la línea en número y nombre
        
        # Si el número y el nombre coinciden, no añadimos la línea (la eliminamos)
        if not (line_data[0] == str(zenbakia) and line_data[1] == izena):
            datu_zerrenda.append(emaitza)
    
    with open("listin.txt", "w") as f:
        for datu in datu_zerrenda:
            f.write(datu + "\n")



def main():
    
    while True:
        print("1-Telefono lista sortu")
        print("2-Telefonoa kontsultatu")
        print("3-Telefono berria sortu")
        print("4-Telefonoa ezabatu")
        print("5-Amaitzeko")
        aukera=int(input("Aukeratu zenbakia idatziz"))
        if aukera==1:
            telefonoa_existitu()
        elif aukera==2:
            zenbakia = int(input("Esan zenbakia:"))
            telefonoa_kontsultatu(zenbakia)
        elif aukera==3:
            zenbakia = int(input("Esan zenbakia:"))
            izena=input("Esan izena:")
            telefono_berria(zenbakia,izena)
        elif aukera==4:
            zenbakia = int(input("Esan zenbakia:"))
            izena=input("Esan izena:")
            telefonoa_ezabatu(zenbakia,izena)
        else:
            break
    
    #zenbakia = int(input("Esan zenbakia:"))
   # izena=input("Esan izena:")
    #telefono_berria(zenbakia,izena)
main()