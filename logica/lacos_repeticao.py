'''Exercícios de Laços (while e for) resolvidos!'''

#Ex 1
contador = 0
while(contador < 3):
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        print(f'Usuário maior de idade({idade} anos)')
    else:
        print(f'Usuário menor de idade ({idade} anos)')
    
    contador += 1

#Ex 2
tabuada = int(input("Qual tabuada você quer aprender?"))
for index in range(1, 11):
    print(f'{tabuada} x {index} = {tabuada * index}')

#Ex3
soma = 0
contador = 0

while contador < 5:
    numero = int(input('Digite o número a ser somado: '))
    soma += numero  
    print(soma)
    contador += 1

media = soma / 5
print(f'A média do total foi {media}')


# Ex 4
for i in range(1,6):
    numero = int(input("insira um número: "))
    if numero % 2 == 0:
        print(f'{numero} é par!')
    else:
        print(f'{numero} é ímpar!')
        