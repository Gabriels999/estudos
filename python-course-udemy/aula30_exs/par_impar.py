valor = input('Digite um numero inteiro: ')
status = False
try:
    if(int(valor)%2==0):
        print('Par')
    else:
        print('Impar')
except:
    print('Digite um numero inteiro valido.')