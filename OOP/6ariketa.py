
class Kontua:
    def __init__(self, titularra, kantitatea):
        self.titularra = titularra
        self.kantitatea = kantitatea

    def inprimatu_datuak(self):
        print(f"Titularra: {self.titularra}, Kantitatea: {self.kantitatea}€")



class AurrezkiKutxa(Kontua):
    def bistaratu_informazioa(self):
        print(f"Aurrezki kontua - Titularra: {self.titularra}, Kantitatea: {self.kantitatea}€")


class EpeFinkoa(Kontua):
    def __init__(self, titularra, kantitatea, epea, interesa):
        super().__init__(titularra, kantitatea)
        self.epea = epea
        self.interesa = interesa

    def interes_osoa(self):
       
        return self.kantitatea * self.interesa / 100

    def erakutsi_informazioa(self):
      
        interes_osoa = self.interes_osoa()
        print(f"Epe Finkoa - Titularra: {self.titularra}, Kantitatea: {self.kantitatea}€, Epea: {self.epea} hilabete, Interesa: {self.interesa}%, Interes Osoa: {interes_osoa}€")



def main():
   
    aurrezki_kutxa = AurrezkiKutxa("Ane Agirre", 1500)
    aurrezki_kutxa.bistaratu_informazioa()

   
    epe_finkoa = EpeFinkoa("Jon Etxebarria", 5000, 12, 3.5)
    epe_finkoa.erakutsi_informazioa()



if __name__ == "__main__":
    main()
