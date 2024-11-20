def positiboak_ordenatu(zerrenda):
    
    if not zerrenda:
        return []

    positiboak = sorted([x for x in zerrenda if x > 0])
    
    emaitza = []
    index = 0  
    
    for zenbaki in zerrenda:
        if zenbaki > 0:
            
            emaitza.append(positiboak[index])
            index += 1
        else:
          
            emaitza.append(zenbaki)
    
    return emaitza

zerrenda = [6, 3, -2, 5, -8, 2, -2]
emaitza = positiboak_ordenatu(zerrenda)
print(emaitza)
