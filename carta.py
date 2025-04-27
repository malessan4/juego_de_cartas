class Carta:
    listaDePalos = ['Treboles', 'Diamantes', 'Corazones', 'Picas']
# Treboles = 0
# Diamentas = 1
# Corazonez = 2
# Picas = 3
    
    listaDeValores = ['nada', 'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Sota', 'Reina', 'Rey']
    
#   se usa "nada" en lista de valores para que la carta del valor 2 se pueda codificar con el 2 y no con el 1    
    
    def __init__(self, palo = 0, valor = 0):
        self.palo = palo
        self.valor = valor
        
    def __str__(self):
        return (self.listaDeValores[self.valor] + " de " + self.listaDePalos[self.palo])

    def __lt__(self, otro):
        if self.valor != otro.valor:
            return self.valor < otro.valor
        return self.palo < otro.palo

    def __eq__(self, otro):
        return self.valor == otro.valor and self.palo == otro.palo

def comparar_cartas(carta1, carta2):
    if carta1 < carta2:
        print(f'{carta1} es MENOR que {carta2}')
    elif carta1 > carta2:
        print(f'{carta1} es MAYOR que {carta2}')
    else:
        print(f'{carta1} es IGUAL a {carta2}')
        

"""  
    def __cmp__(self, otro):
        if self.palo > otro.palo: return 1
        if self.palo < otro.palo: return -1    
        if self.valor > otro.valor: return 1
        if self.valor < otro.valor: return -1
        return 0
"""        


            

carta1 = Carta(1, 11)
carta2 = Carta(2, 5)
print(carta1)
print(carta2)
comparar_cartas(carta1, carta2)