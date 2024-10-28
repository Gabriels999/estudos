class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def analisa_nome(self):
        if len(self.nome) < 5:
            print(f"{self.nome}, seu nome eh curto.")
        elif len(self.nome) < 7:
            print(f"{self.nome}, seu nome tem tamanho medio.")
        else:
            print(f"{self.nome}, seu nome eh muito grande.")

gabriel = Pessoa(nome='Gabriel')
laura = Pessoa('Laura')
joao = Pessoa('Joao')

gabriel.analisa_nome()
laura.analisa_nome()
joao.analisa_nome()