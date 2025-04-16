import os

def mostrar_placar(time_A,time_B,pontos_time_A,pontos_time_B):
        print('')
        print(F'{'PLACAR':^87}')
        print('=-=' * 28)
        print(f'{'':>20} TIME A: {time_A.title()} ',end='')
        print(f'{'':10} TIME B: {time_B.title()}')
        print(f'{'':>27} {pontos_time_A} ',end='')
        print(f'{'':>23} {pontos_time_B}')
        print('=-=' * 28)

def adicionar_pontos(time):
     while True:
        try:
            valor = int(input(' Quantos pontos foram? (1/2/3): '))
            if valor in [1,2,3]:
                return valor
            else:
                print(' Inválido, digite 1, 2 ou 3.')

        except ValueError:
             print(' Inválido, digite 1, 2 ou 3.')

def finalizar_partida(time_A,time_B,pontos_time_A,pontos_time_B):
    mostrar_placar(time_A,time_B,pontos_time_A,pontos_time_B)
    print(' Partida finalizada.')
    exit()

def clear_system():
    os.system('cls' if os.name == 'nt' else 'clear')


pontos_time_A = 0
pontos_time_B = 0

time_A = input(' Time A: ').strip()
time_B = input(' Time B: ').strip()


while True:

    clear_system()
    print('info: Caso queira finalizar, digite: (exit)')
    mostrar_placar(time_A ,time_B , pontos_time_A, pontos_time_B)

    p = input(' Quem pontuou ? (A/B) Time: ').strip().upper()
    if p in ['A']:
        
        pontos_time_A += adicionar_pontos(time_A)
    elif p in ['B']:
        
        pontos_time_B += adicionar_pontos(time_B)
    elif p in ['EXIT']:
        clear_system()
        finalizar_partida(time_A, time_B, pontos_time_A, pontos_time_B,)
    else:
        print(' Inválido, digite novamente.')