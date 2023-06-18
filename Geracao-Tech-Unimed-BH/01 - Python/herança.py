class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Ligando motor")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"
        
class Motocicleta(Veiculo):
    def __init__(self, cor, placa, numero_rodas, status):
        super().__init__(cor, placa, numero_rodas)
        self.status = status
    
    def qual_status(self):
        print(f"{'Sim' if self.status else 'Não'} estou rodando")

moto = Motocicleta("preta", "aaa-1111", 2, True)
moto.ligar_motor()
moto.qual_status()
print(moto)