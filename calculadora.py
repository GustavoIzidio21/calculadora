import os

def frase_inicial():
    print ('''
\033[0;33m
█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█
\033[0m''')

def main():
    os.system('cls')
    frase_inicial()
    exibir_opcoes()
    escolher_opcao()

def opcao_valida():
   print('\033[1;31mErro!\033[0m Digite uma opção válida. \n')

def exibir_opcoes ():
    print ('''
    \033[1;37m
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
    5. Tabuada \033[0m
    \033[1;31m6. Sair\033[0m
    
    ''')

def exibir_texto(texto):
    os.system('cls')
    print(texto)

def voltar_ao_menu():
    input('\nDigite Enter para voltar ao menu principal... ')
    main()

def soma(): # essa função serve para o usuário inserir dois valores e realizar a soma dos mesmos.
        try:
            os.system('cls')
            exibir_texto('A opção escolhida foi a de \033[1;33mSOMA\033[0m\n')
            x = float(input('Digite o primeiro número: '))
            y = float(input('Digite o segundo número: '))            
            soma = x + y
            print(f'\nO resultado de {x} + {y} é = \033[1;32m{soma}\033[0m\n')
        except ValueError:
            print('\033[1;31mErro!\033[0m Digite um número válido.\n')    
        realizar_nova_conta()
                    

def subtracao(): # essa função serve para o usuário inserir dois valores e realizar a subtração dos mesmos.
        try:
            os.system('cls')
            exibir_texto('A opção escolhida foi a de \033[1;33mSUBTRAÇÃO\033[0m\n')
            x = float(input('Digite o primeiro número: '))
            y = float(input('Digite o segundo número: '))
            subtracao = x - y
            print(f'\nO resultado de {x} - {y} é = \033[1;32m{subtracao}\033[0m\n')
        except ValueError:
            print('\033[1;31mErro!\033[0m Digite um número válido.\n')
        realizar_nova_conta()



def multiplicacao(): # essa função serve para o usuário inserir dois valores e realizar a multiplicação dos mesmos.
        try:
            os.system('cls')
            exibir_texto('A opção escolhida foi a de \033[1;33mMULTIPLICAÇÃO\033[0m\n')
            x = float(input('Digite o primeiro número: '))
            y = float(input('Digite o segundo número: '))
            multiplicacao = x * y
            print(f'\nO resultado de {x} x {y} é = \033[1;32m{multiplicacao}\033[0m\n') 
        except ValueError:
            print('\033[1;31mErro!\033[0m Digite um número válido.\n')
        realizar_nova_conta()


def divisao(): # essa função serve para o usuário inserir dois valores e realizar a divisão dos mesmos.
        try:
            os.system('cls')
            exibir_texto(f'A opção escolhida foi a de \033[1;33mDIVISÃO\033[0m\n')
            x = float(input('Digite o primeiro número: '))
            y = float(input('Digite o segundo número: '))
            if x == 0:
                raise ZeroDivisionError
            if y == 0:
                raise ZeroDivisionError ('\033[1;31mErro!\033[0m Não é possível divisão por 0. Tente com um número válido.\n')
            divisao = x / y
            print(f'\nO resultado de {x} / {y} é = \033[1;32m{divisao}\033[0m\n')
        except ValueError:
            print('\033[1;31mErro!\033[0m Digite um número válido.\n')
        except ZeroDivisionError:
            print('\n\033[1;31mErro!\033[0m Não é possível divisão por 0. Tente com um número válido.\n')
        realizar_nova_conta()


def tabuada():
        try:    
            os.system('cls')
            exibir_texto (f'A opção escolhida foi a \033[1;33mTABUADA\033[0m\n')
            tabuada = int(input('Insira um número desejado: '))
            print(f'\nSegue abaixo o resultado da tabuada do \033[1;32m{tabuada}:\033[0m\n')
            for i in range(1, 11):
                print(f'{tabuada} x {i} = \033[1;32m{tabuada * i}\033[0m')
            print()
        except ValueError:
            print('\033[1;31mErro!\033[0m Digite um número válido.\n')
        realizar_nova_conta()


def finalizando_app(texto):
    print(texto)


def escolher_opcao():
    while True:
        try:
            escolher_opcao = int(input('\033[1;37mDigite uma opção válida:\033[0m '))

            if escolher_opcao == 1:
                soma()
            elif escolher_opcao == 2:
                subtracao()
            elif escolher_opcao == 3:
                multiplicacao()
            elif escolher_opcao == 4:
                divisao()
            elif escolher_opcao == 5:
                tabuada()
            elif escolher_opcao == 6:
                sair_do_programa()
                exit()
            else:
                opcao_valida()
                os.system('cls')
                exibir_opcoes()
                print(f'\033[1;31mErro!\033[0m O número {escolher_opcao} é invalido. \n')
        except ValueError:
            os.system('cls')
            exibir_opcoes()
            print(f'\033[1;31mErro!\033[0m O caractere digitado é invalido. \n')

def realizar_nova_conta():
    while True: 
        nova_conta = input('\nDeseja continuar o programa?\n\033[1;32m(Sim\033[0m/\033[1;31mNão)\033[0m: ').lower()
        if nova_conta == 'sim':
            voltar_ao_menu()
            break
        elif nova_conta == 'não':
            os.system('cls')
            finalizando_app('\n\033[0;37mFinalizando app\033[0m')
            print('Até a próxima... \n')
            exit()
        else:
           opcao_valida()

def sair_do_programa():
    while True:
        try:
            os.system('cls')
            exibir_texto ('A opção escolhida foi a \033[1;33mSAIR\033[0m')
            sair_do_programa = input('\nDeseja sair do programa?\n\033[1;32m(Sim\033[0m/\033[1;31mNão)\033[0m: ').lower()
            if sair_do_programa == 'sim':
                os.system('cls')
                finalizando_app('\n\033[0;37mFinalizando app\033[0m')
                print('Até a próxima... \n')
                break
            elif sair_do_programa == 'não':
                voltar_ao_menu()
                break
            else:
                opcao_valida()
        except ValueError:
                print('\033[1;31mErro!\033[0m Digite um número válido.\n')


if __name__ == '__main__':
    main()