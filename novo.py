import os

def sair():
    while True:
        os.system('cls')
        sair_do_programa = input('\nDeseja sair do programa? (Sim/Não): ').strip().lower()

        if sair_do_programa in ['sim', 's']:
            print('\n\033[1;35mFinalizando app\033[0m')
            break
        elif sair_do_programa in ['não', 'nao', 'n']:
            print('teste')
            break
        else:
            print('\033[1;31mOpção inválida!\033[0m Por favor, digite "Sim" ou "Não".\n')
