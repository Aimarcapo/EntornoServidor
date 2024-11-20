class Pertsona:
    def __init__(self,izena, adina):
        self.izena=izena
        self.adina=adina
    def getAdina(self):
        print (self.adina)
    def getIzena(self):
        print (self.izena)
    def __str__(self):
        return f"{self.izena}({self.adina})"
    def isNagusi(self):
        if self.adina>=18:
            return f"{self.izena}nagusia da {self.adina} urterekin"
        else:
            return f"{self.izena} ez da nagusia {self.adina} urterekin"
pertsona=Pertsona("Aimar",9)
pertsona.getIzena()
pertsona.getAdina()
print(pertsona.isNagusi())