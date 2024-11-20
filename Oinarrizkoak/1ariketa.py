import re
try:
    print("Eginiko kilometroak:")
    kilometro  = float(input())
    print("Gastatutako gasolina litroak:")
    litro =float(input())
except:
    print("Zenbakiak sartu behar dituzu")
else:
    total=float(litro)/float(kilometro)
    print("Kilometro bakoitzeko litroak:",total)