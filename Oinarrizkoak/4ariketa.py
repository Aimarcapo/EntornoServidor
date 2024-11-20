try:
    print("Sartu ezazu zenbaki oso bat:")
    zenbakia  = int(input())
except:
    print("Zenbaki bat izan behar da")
else:
    if zenbakia%2==0:
        print("Bikotia da")
    else:
        print("Ez da bikotia")