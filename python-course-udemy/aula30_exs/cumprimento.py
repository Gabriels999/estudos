class Cumprimento:
    
    def __init__(self, nome, hora):
        self.nome = nome
        self.hora = hora

    def cumprimentar(self):
        if self.hora < 12:
            print(f'Bom dia, {self.nome}.')
        elif self.hora < 18:
            print(f'Boa tarde, {self.nome}.')
        else:
            print(f'Boa noite, {self.nome}.')

valor = input("Digite um horario (0-23): ")

try:
    gabriel = Cumprimento(nome='Gabriel', hora=int(valor))
    gabriel.cumprimentar()
except:
    print("Por favor, digite um horario entre 0 e 23.")