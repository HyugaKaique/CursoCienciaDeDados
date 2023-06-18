class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw) 
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw) 
        self.cor_bico = cor_bico
        
class FalarMixin:
    def falar(self):
        return "oi estou falando"

class Gato(Mamifero):
    pass


class Ornintorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_pelo, cor_bico, numero_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas = numero_patas)

gato = Gato(numero_patas=4,cor_pelo="preto")
print(gato)

ornintorrinco = Ornintorrinco(numero_patas=4,cor_pelo="verde", cor_bico="preto")
print(ornintorrinco)