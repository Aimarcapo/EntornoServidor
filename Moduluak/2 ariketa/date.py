from datetime import datetime, timedelta

def data():
    fecha = input("Sartu data AAAA-MM-DD: ")
    try:
       
        fecha_valida = datetime.fromisoformat(fecha)
        print(f"Data egokia da: {fecha_valida}")
    except ValueError:
        print("Ez duzu data bat idatzi.")

def urtebetetzea():
    birthday = input("Sartu zure urtebetzea AAAA-MM-DD: ")
    try:
       
        birthday_date = datetime.fromisoformat(birthday)
    except ValueError:
        print("Ez duzu data bat idatzi.")
    else:
       
        ahora = datetime.now()
        diferencia = birthday_date - ahora
        if diferencia.days < 0:
            print(f"Zure urtebetetzea {abs(diferencia.days)} egun pasa da.")
        else:
            print(f"Zure urtebetetzea {diferencia.days} egun barru izango da.")

def eguna():
    bornday = input("Sartu zure jaiotze data AAAA-MM-DD: ")
    try:
       
        birthday_date = datetime.fromisoformat(bornday)
        
        if(birthday_date.isoweekday()==1):
            print("Monday")
        elif(birthday_date.isoweekday()==2):
            print("Tuesday")
        elif(birthday_date.isoweekday()==3):
            print("Wednesday")
        elif(birthday_date.isoweekday()==4):
            print("Thursday")
        elif(birthday_date.isoweekday()==5):
            print("Friday")
        elif(birthday_date.isoweekday()==6):
            print("Saturday")
        elif(birthday_date.isoweekday()==7):
            print("Sunday")
    except ValueError:
        print("Ez duzu data bat idatzi.")
   

#data()
#urtebetetzea()
eguna()
