
try:
    f = open("bisitak.txt", "x")
except FileExistsError:
    f = open("bisitak.txt", "r")
    content=f.readline()
    content=int(content)
    f.close()
    parametroa=input("Sartu G(gehitzeko) ,K(kentzeko).Parametroa ez bada ez bata ez bestea balioa erakutsiko du:")
    if parametroa=="G":
        content+=1
        
    elif parametroa=="K":
        content-=1
    print(content)
    f = open("bisitak.txt", "w")
    f.write(str(content))
    f.close()
else:
    f.write("0")
    f.close()
    

    