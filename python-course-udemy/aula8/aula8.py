nome = 'Gabriel'
idade = 25
altura = 1.85
peso = 88.0
ano_atual = 2022

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.',
    f'O IMC de {nome} eh {peso/altura**2:.2f}.',
    f'{nome} nasceu em {ano_atual-idade}.', sep='\n')