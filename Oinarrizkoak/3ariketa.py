import re
try:
    print("Sartu ezazu testu bat:")
    testua  = input()
except:
    print("Testu bat sortu behar duzu")
else:
    lehenengo=testua[0]
    print("Testuaren lehenengo karakterea",lehenengo)
    testua=testua.replace(" ", "")
    while True:
        try:
            print("Sartu 53 baino zenbaki positibo txikiago bat:")
            zenbakia=int(input())
        except:
            print("Sartu behar duzuna zenbaki bat izan behar da")
        else:
            if 53> zenbakia &zenbakia<=len(testua):
                print("Posizio horretan dagoen karakterea:", testua[zenbakia-1])
            elif zenbakia>len(testua):
                print("Sartu behar duzun zenbakia testuaren letra kantitatearen berdina edo txikiagoa izan behar da")
            else:
                print("Sartu behar duzun zenbaki 53 baino txikiagoa izan behar da:")

        

