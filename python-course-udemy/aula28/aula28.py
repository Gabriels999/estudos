from curses.ascii import isdigit


num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

if num1.isdigit() and num2.isdigit():
    print(int(num1) + int(num2))
else:
    print('Insira apenas numeros, sem caracteres especiais.')

try:
    print(int(num1) + int(num2))
except:
    print('ERROR')
