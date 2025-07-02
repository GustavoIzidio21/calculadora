import os

def frase_inicial():
    print ('''

█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█
''')

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
    5. Tabuada
    6. Sair
    \033[0m
    ''')

def exibir_texto(texto):
    os.system('cls')
    print(texto)

def voltar_ao_menu():
    input('\nDigite Enter para voltar ao menu principal... ')
    main()

def soma(): # essa função serve para o usuário inserir dois valores e realizar a soma dos mesmos.
    while True: 
        try:
            os.system('cls')
            exibir_texto('A opção escolhida foi a de \033[1;34msoma\033[0m\n')
            x = float(input('Digite o primeiro número: '))
            y = float(input('Digite o segundo número: '))            
            soma = x + y
            print(f'\nO resultado de {x} + {y} é = \033[1;32m{soma}\033[0m\n')
        except ValueError:
            print('\033[1;31mErro!\033[0m Digite um número válido.')    
        while True:
            try:    
                realizar_outra_soma = (input('Deseja continuar o programa? (Sim/Não): ')).lower()
                if realizar_outra_soma == 'sim':
                  break
                elif realizar_outra_soma == 'não':
                    voltar_ao_menu()
                else:
                    opcao_valida()
            except ValueError:
               print('\033[1;31mErro!\033[0m Digite um número válido.')
                    

def subtracao(): # essa função serve para o usuário inserir dois valores e realizar a subtração dos mesmos.
 while True:
    try:
        os.system('cls')
        exibir_texto('A opção escolhida foi a de \033[1;34msubtração\033[0m\n')
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        subtracao = x - y
        print(f'\nO resultado de {x} - {y} é = \033[1;32m{subtracao}\033[0m\n')
    except ValueError:
     print('\033[1;31mErro!\033[0m Digite um número válido.\n')
    while True:
        try:    
            realizar_outra_subtracao = str(input('Deseja continuar o programa? (Sim/Não): ')).lower()
            if realizar_outra_subtracao == 'sim':
                break
            elif realizar_outra_subtracao == 'não':
                voltar_ao_menu()
            else:
                opcao_valida()
        except ValueError:
           print('\033[1;31mErro!\033[0m Digite um número válido.\n')


def multiplicacao(): # essa função serve para o usuário inserir dois valores e realizar a multiplicação dos mesmos.
 while True:
    try:
        os.system('cls')
        exibir_texto('A opção escolhida foi a de \033[1;34mmultiplicação\033[0m\n')
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        multiplicacao = x * y
        print(f'\nO resultado de {x} x {y} é = \033[1;32m{multiplicacao}\033[0m\n') 
    except ValueError:
        print('\033[1;31mErro!\033[0m Digite um número válido.\n')
    while True:
        try:    
            realizar_outra_multiplicacao = str(input('Deseja continuar o programa? (Sim/Não): ')).lower()
            if realizar_outra_multiplicacao == 'sim':
                x = float(input('\nDigite o primeiro número: '))
                y = float(input('Digite o segundo número: '))            
                multiplicacao = x * y
                print(f'\nO resultado de {x} x {y} é = \033[1;32m{multiplicacao}\033[0m\n')
            elif realizar_outra_multiplicacao == 'não':
                voltar_ao_menu()
            else:
                opcao_valida()
        except ValueError:
            print('\033[1;31mErro!\033[0m Digite um número válido.')

def divisao(): # essa função serve para o usuário inserir dois valores e realizar a divisão dos mesmos.
    while True:
        try:
            os.system('cls')
            exibir_texto(f'A opção escolhida foi a de \033[1;34mdivisão\033[0m\n')
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
        continuar_programa()


def tabuada():

    while True:
        try:    
            os.system('cls')
            exibir_texto (f'A opção escolhida foi a \033[1;34mtabuada\033[0m\n')
            tabuada = int(input('Insira um número desejado: '))
            print(f'\nSegue abaixo o resultado da tabuada do \033[1;32m{tabuada}:\033[0m\n')
            for i in range(1, 11):
                print(f'{tabuada} x {i} = \033[1;32m{tabuada * i}\033[0m')
            print()
        except ValueError:
            print('\033[1;31mErro!\033[0m Digite um número válido.\n')
        while True:
            realizar_outra_tabuada = input('Deseja continuar o programa? (Sim/Não): ').lower()
            if realizar_outra_tabuada == 'sim':
                break
            elif realizar_outra_tabuada == 'não':
                voltar_ao_menu()
            else:
                opcao_valida()

def finalizando_app(texto):
    print(texto)


def escolher_opcao():
    while True:
        try:
            escolher_opcao = int(input('Escolha uma opção: '))

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
                break
            else:
                opcao_valida()
                os.system('cls')
                frase_inicial()
                exibir_opcoes()
                print('\033[1;31mErro!\033[0m Digite uma opção de 1 até 6: \n')
        except ValueError:
            os.system('cls')
            frase_inicial()
            exibir_opcoes()
            print('\033[1;31mErro!\033[0m Digite uma opção de 1 até 6: \n')

def sair_do_programa():
    while True:
        try:
            os.system('cls')
            exibir_texto ('A opção escolhida foi a \033[1;34msair\033[0m')
            sair_do_programa = input('\nDeseja sair do programa? (Sim/Não): ').lower()
            if sair_do_programa == 'sim':
                finalizando_app('\n\033[1;35mFinalizando app\033[0m')
                print('Até a próxima... \n')
                break
            elif sair_do_programa == 'não':
                voltar_ao_menu()
                break
            else:
                opcao_valida()
        except ValueError:
                print('\033[1;31mErro!\033[0m Digite um número válido.\n')
                


def continuar_programa(): 
    while True: 
        realizar_outra_divisao = input('Deseja continuar o programa? (Sim/Não): ').strip().lower()
        if realizar_outra_divisao == 'sim':
            break
        elif realizar_outra_divisao == 'não':
            voltar_ao_menu()
        else:
            opcao_valida()
        



if __name__ == '__main__':
    main()