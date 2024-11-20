def gehiengo_absolutua(lista):
 duplicates={}
 lista.sort()
 
 for x in range (0,len(lista)):
      
      if lista[x] not in duplicates:
        contador=lista.count(lista[x])
        duplicates[lista[x]]=contador

 for key,value in duplicates.items():
   
   if int(value)*2>=len(lista):
     return (key+" alderdiak gehiengo absolutua lortu du")
   else:
     return ("Inork ez dauka gehiengo absoluturik")
lista=["a","b","a","b","a"]
print(gehiengo_absolutua(lista))
