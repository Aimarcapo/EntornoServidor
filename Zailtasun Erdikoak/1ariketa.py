import re
testua=input("Sartu ezazu testu bat:")
testua=testua.upper()
ordenado=sorted((testua.split()))
sin_duplicado=sorted(set(ordenado))
emaitza=' '.join(sin_duplicado)
print(emaitza)
