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
    
    def mezclar(self):
        import random
        nCartas = len(self.cartas)
        for i in range(nCartas):
            j = random.randrange(i, nCartas)
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]
        
    
mazo = Mazo()
mazo.mezclar()
print(mazo)


