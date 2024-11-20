import random
def irakurri_zenbakiak(min,max):
    if min>=max:
         raise ValueError("Minimoa maximoa baino handiagoa edo berdina da!")
    return random.uniform(min,max)
def zenbakia_asmatu(min,max):
    emaitza=irakurri_zenbakiak(min,max)
    for x in range(7):
        try:
            zenbakia=int(input("Esan zenbakia"))
        except:
             print("Balioa gaizki idatzi duzu")
             continue

        if zenbakia==emaitza:
            print ("Zenbakia asmatu duzu")
            break

        elif zenbakia>emaitza:
            print ("Idatzi duzun zenbakia ausasko zenbakia baino handiagoa da")

        elif emaitza>zenbakia:
            print ("Idatzi duzun zenbakia ausasko zenbakia baino txikiagoa da")
            