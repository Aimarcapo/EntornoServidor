class Ikaslea:
    def __init__(self,izena, kalifikazioa):
        self.izena=izena
        self.kalifikazioa=kalifikazioa
    def getNota(self):
        print (self.kalifikazioa)
    def getIzena(self):
        print (self.izena)
    def __str__(self):
        return f"{self.izena}({self.kalifikazioa})"
    def isgainditu(self):
        if self.kalifikazioa>=5:
            return f"{self.izena}gainditu du {self.kalifikazioa} batekin"
        else:
            return f"{self.izena} ez du gainditu {self.kalifikazioa} batekin"
ikaslea=Ikaslea("Aimar",9)
ikaslea.getIzena()
ikaslea.getNota()
print(ikaslea.isgainditu())