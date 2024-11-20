class Kontaktu:
    def __init__(self, izena, telefonoa, emaila):
        self.izena = izena
        self.telefonoa = telefonoa
        self.emaila = emaila

    def __str__(self):
        return f"Izena: {self.izena}, Telefonoa: {self.telefonoa}, Emaila: {self.emaila}"


class Agenda:
    def __init__(self):
        self.kontaktuak = []

    def gehitu_kontaktua(self, izena, telefonoa, emaila):
        kontaktu_berria = Kontaktu(izena, telefonoa, emaila)
        self.kontaktuak.append(kontaktu_berria)
        print(f"{izena} kontaktua gehitu da.")

    def inprimatu_zerrenda(self):
        if not self.kontaktuak:
            print("Ez dago kontakturik agendan.")
        else:
            print("Kontaktuen zerrenda:")
            for kontaktu in self.kontaktuak:
                print(kontaktu)

    def bilatu_kontaktua(self, izena):
        for kontaktu in self.kontaktuak:
            if kontaktu.izena.lower() == izena.lower():
                return kontaktu
        return None

    def editatu_kontaktua(self, izena):
        kontaktua = self.bilatu_kontaktua(izena)
        if kontaktua:
            print(f"{izena} kontaktua aurkitu da.")
            print("Zer aldatu nahi duzu? (1) Izena (2) Telefonoa (3) Emaila")
            aukera = input("Aukera sartu (1, 2 edo 3): ")
            
            if aukera == "1":
                izen_berria = input("Izen berria sartu: ")
                kontaktua.izena = izen_berria
                print(f"Izena aldatu da: {izen_berria}")
            elif aukera == "2":
                telefono_berria = input("Telefono berria sartu: ")
                kontaktua.telefonoa = telefono_berria
                print(f"Telefonoa aldatu da: {telefono_berria}")
            elif aukera == "3":
                email_berria = input("Email berria sartu: ")
                kontaktua.emaila = email_berria
                print(f"Emaila aldatu da: {email_berria}")
            else:
                print("Aukera okerra.")
        else:
            print(f"{izena} kontaktua ez da aurkitu.")


def menu():
    agenda = Agenda()

    while True:
        print("\nMenua:")
        print("1. Gehitu kontaktua")
        print("2. Inprimatu kontaktu zerrenda")
        print("3. Bilatu kontaktua")
        print("4. Editatu kontaktua")
        print("5. Irten")

        aukera = input("Aukera bat hautatu: ")

        if aukera == "1":
            izena = input("Sartu izena: ")
            telefonoa = input("Sartu telefonoa: ")
            emaila = input("Sartu emaila: ")
            agenda.gehitu_kontaktua(izena, telefonoa, emaila)

        elif aukera == "2":
            agenda.inprimatu_zerrenda()

        elif aukera == "3":
            izena = input("Sartu bilatzeko izena: ")
            kontaktua = agenda.bilatu_kontaktua(izena)
            if kontaktua:
                print(kontaktua)
            else:
                print(f"{izena} kontaktua ez da aurkitu.")

        elif aukera == "4":
            izena = input("Sartu editatzeko izena: ")
            agenda.editatu_kontaktua(izena)

        elif aukera == "5":
            print("Programatik irten.")
            break

        else:
            print("Aukera okerra. Saiatu berriro.")


# Programa exekutatu
menu()
