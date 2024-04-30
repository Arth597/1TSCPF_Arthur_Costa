# Receba uma palavra do usuário e verifique se ela é um palíndromo (igual quando
# lida de trás para frente).
palavra = str(input('Digite uma palavra:'))

invertida =  palavra[::-1]

if palavra == invertida:
    print(f'{palavra} É um palindromo')
else:
    print('Não é um palindromo')
EDITADO