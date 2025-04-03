from carta import Carta

class Mazo:
    def __init__(self):
        self.cartas = []
        for palo in range(4):
            for valor in range (1, 14):
                self.cartas.append(Carta(palo, valor))
    
    def __str__(self):
        s = ""
        for i in range(len(self.cartas)):
            s = s + " "*i + str(self.cartas[i]) + "\n"
        return s
    
mazo = Mazo()
print(mazo)

