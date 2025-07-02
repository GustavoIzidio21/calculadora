numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Kevin', 'Gustavo', 'Andrade', 'Caramelo']
ano = [2001, 2025]

for nome in nomes:
    print(f'.{nome}')

soma = 0
for numero in range(1, 11):
    if numero % 2 != 0:
        soma = soma + numero  
print(f'\n{soma}\n')

for numero in range(1, 11, +1):
    print(numero)
print()

numero_escolhido = int(input('Insira um número: '))
for i in range(1, 11):
    print(f'{numero_escolhido} x {i} = {numero_escolhido * i}')
