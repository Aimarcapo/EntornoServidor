import zenbakiaAsmatu
try:
    minimoa=int(input("Sartu nahi duzun minimoa"))
    maximoa=int(input("Sartu nahi duzun maximoa"))
except ValueError:
    print("Balioa gaizki idatzi duzu")
else:
    zenbakiaAsmatu.zenbakia_asmatu(minimoa,maximoa)
  