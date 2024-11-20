import re
try:
    print("Sartu ezazu zenbaki bat:")
    zenbakia  = float(input())
except:
    print("Zenbaki bat sartu behar duzu")
else:
    kenduta =zenbakia*0.85
    print("Zenbaki 15% kenduta:",kenduta)
