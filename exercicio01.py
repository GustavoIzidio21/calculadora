# Par ou Ímpar
numero = int(input('Insira um número: '))
if numero % 2 == 0:
    print('Esse número é par')
else:
    print('Esse número é ímpar')

# Cri, Ado or Adu
pergunta_idade = int(input('Digite sua idade: '))
if 0 <= pergunta_idade <= 12:
    print('Criança')
elif 13 <= pergunta_idade < 18:
    print('Adolescente')
elif pergunta_idade >= 18:
    print("Adulto")
else: 
    print("Valor inválido!")

# Usuario and senha
admin = '@1234'
senha = 1234
admin_inserido = input('Insira seu usuário:')
senha_inserido = int(input('Insira sua senha:'))
if admin == admin_inserido and senha == senha_inserido:
    print('Acesso liberado')
else:
    print('Acesso negado')

# Valor dos quadrantes
x = int(input('Insira o valor de X: '))
y = int(input('Insira o valor de Y: '))

if x > 0 and y > 0:
    print('Esse é o primeiro quadrante')
elif x < 0 and y > 0:
    print('Esse é o segundo quadrante')
elif x < 0 and y < 0:
    print('Esse é o terceiro quadrante')
elif x > 0 and y < 0:
    print('Esse é o quarto quadrante')
else:
    print('O ponto está localizado no eixo ou origem')