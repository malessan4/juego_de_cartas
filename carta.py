class Carta:
    listaDePalos = ['Treboles', 'Diamantes', 'Corazones', 'Picas']
    
    listaDeValores = ['nada', 'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Sota', 'Reina', 'Rey']
    
    def __init__(self, palo = 0, valor = 0):
        self.palo = palo
        self.valor = valor
        
    def __str__(self):
        return (self.listaDeValores[self.valor] + " de " + self.listaDePalos[self.palo])