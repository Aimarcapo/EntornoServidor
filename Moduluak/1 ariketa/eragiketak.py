
def batuketa(first,second):
    try:
        emaitza=int(first)+int(second)
    except ValueError:
        print("Akatsa:Datu mota baliogabea")
    except ZeroDivisionError:
        print("Akatsa: Zenbakia ezin da zeroz zatitu")
    else:
        return emaitza
def kenketa(first,second):
    try:
        emaitza=int(first)-int(second)
    except ValueError:
        print("Akatsa:Datu mota baliogabea")
    except ZeroDivisionError:
        print("Akatsa: Zenbakia ezin da zeroz zatitu")
    else:
        return emaitza
def biderketa(first,second):
    try:
        emaitza=int(first)*int(second)
    except ValueError:
        print("Akatsa:Datu mota baliogabea")
    except ZeroDivisionError:
        print("Akatsa: Zenbakia ezin da zeroz zatitu")
    else:
        return emaitza 
def zatiketa(first,second):
    try:
        emaitza=int(first)/int(second)
    except ValueError:
        print("Akatsa:Datu mota baliogabea")
    except ZeroDivisionError:
        print("Akatsa: Zenbakia ezin da zeroz zatitu")
    else:
        return emaitza