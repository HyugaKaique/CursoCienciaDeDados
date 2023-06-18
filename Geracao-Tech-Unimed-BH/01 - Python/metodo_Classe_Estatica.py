class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome=nome
        self.idade=idade
        
    @classmethod
    def cria_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
#p = Pessoa("Guilherme, 28")
#print(p.nome, p.idade)
p = Pessoa.cria_data_nascimento(1994,3,21, "Kaique")
print(p.nome, p.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(17))