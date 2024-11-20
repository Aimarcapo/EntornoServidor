class Bezero:
    def __init__(self, izena, abizena, dirua):
        self.izena = izena
        self.abizena = abizena
        self.dirua = dirua

    def __str__(self):
        return f"Izena: {self.izena}, Abizena: {self.abizena}, Dirua: {self.dirua}"


class Bankua:
    def __init__(self):
        self.bezeroak = []

    def gehitu_bezeroa(self, izena, abizena, dirua):
        bezero_berria = Bezero(izena, abizena, dirua)
        self.bezeroak.append(bezero_berria)
        print(f"{izena} bezeroa gehitu da.")

    def inprimatu_zerrenda(self):
        if not self.bezeroak:
            print("Ez dago bezerorik bankuan.")
        else:
            print("Bankuaren bezeroak:")
            for bezero in self.bezeroak:
                print(bezero)

    def bilatu_bezeroa(self, izena):
        for bezero in self.bezeroak:
            if bezero.izena.lower() == izena.lower():
                return bezero
        return None

    def gehitu_dirua(self, izena, dirua):
        bezero = self.bilatu_bezeroa(izena)
        if bezero:
            bezero.dirua += dirua
            print(f"{izena} bezeroari {dirua}€ gehitu zaizkio.")
        else:
            print(f"{izena} bezeroa ez da aurkitu.")

    def dirua_kendu(self, izena, dirua):
        bezero = self.bilatu_bezeroa(izena)
        if bezero:
            if bezero.dirua >= dirua:
                bezero.dirua -= dirua
                print(f"{izena} bezeroari {dirua}€ kendu zaizkio.")
            else:
                print(f"{izena} bezeroak ez du diru nahikorik ({bezero.dirua}€ baino ez dauka).")
        else:
            print(f"{izena} bezeroa ez da aurkitu.")

    def get_dirua(self, izena):
        bezero = self.bilatu_bezeroa(izena)
        if bezero:
            return bezero.dirua
        else:
            print(f"{izena} bezeroa ez da aurkitu.")
            return None


def menu():
    bankua = Bankua()

    while True:
        print("\nAukerak:")
        print("1. Gehitu bezeroa")
        print("2. Inprimatu bezeroak")
        print("3. Gehitu dirua bezeroari")
        print("4. Dirua kendu bezeroari")
        print("5. Bezeroaren dirua kontsultatu")
        print("6. Irten")

        aukera = input("Aukera bat aukeratu: ")

        if aukera == "1":
            izena = input("Sartu bezeroaren izena: ")
            abizena = input("Sartu bezeroaren abizena: ")
            dirua = float(input("Sartu hasierako dirua: "))
            bankua.gehitu_bezeroa(izena, abizena, dirua)

        elif aukera == "2":
            bankua.inprimatu_zerrenda()

        elif aukera == "3":
            izena = input("Sartu bezeroaren izena: ")
            dirua = float(input("Zenbat diru gehitu nahi duzu?: "))
            bankua.gehitu_dirua(izena, dirua)

        elif aukera == "4":
            izena = input("Sartu bezeroaren izena: ")
            dirua = float(input("Zenbat diru kendu nahi duzu?: "))
            bankua.dirua_kendu(izena, dirua)

        elif aukera == "5":
            izena = input("Sartu bezeroaren izena: ")
            dirua = bankua.get_dirua(izena)
            if dirua is not None:
                print(f"{izena} bezeroak {dirua}€ dauka kontuan.")

        elif aukera == "6":
            print("Agur!")
            break

        else:
            print("Aukera okerra, saiatu berriz.")


menu()

