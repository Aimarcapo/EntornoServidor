class Triangelua:
    def __init__(self, a, b, c):
        # Aldeen balioak esleitzen ditugu, eta ziurtatzen dugu balioak egokiak direla
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Aldeek 0 baino handiagoak izan behar dute.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Alde hauekin ezin da triangelu bat osatu.")
        
        self.a = a
        self.b = b
        self.c = c
    
    def handiena_imprimatu(self):
        # Alde handiena aurkitzen dugu
        handiena = max(self.a, self.b, self.c)
        print(f"Triangeluaren alde handiena: {handiena}")
    
    def triangelu_mota(self):
        if self.a == self.b == self.c:
            print("Triangelua aldeberdina da.")
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            print("Triangelua isoszelea da.")
        else:
            print("Triangelua eskalenoa da.")