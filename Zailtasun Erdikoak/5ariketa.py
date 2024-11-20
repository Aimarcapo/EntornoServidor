def amaiera_amankomuna(str1, str2):
    
    amaiera_amankomuna = ""
    
    luzera_minimoa = min(len(str1), len(str2))

    for i in range(1, luzera_minimoa + 1):
        if str1[-i] == str2[-i]: 
            amaiera_amankomuna = str1[-i] + amaiera_amankomuna
        else:
            break

    return amaiera_amankomuna

print(amaiera_amankomuna("programazio", "funtzio"))
print(amaiera_amankomuna("auto", "moto"))
print(amaiera_amankomuna("bilbo", "donostia"))
