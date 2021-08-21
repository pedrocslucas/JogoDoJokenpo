#JOGO DO JOKENPÔ
import random as rd
from time import sleep
from emoji import emojize

print('\033[1;34m!!!JOGO DO JOKENPÔ!!!')

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
escolhaCPU = opcoes[rd.randint(0,2)]

print(emojize('''\033[1;97m
OPÇÕES:
:white_medium_square: PEDRA
:scroll: PAPEL
:scissors: TESOURA''', use_aliases=True))
escolhaPlayer = str(input('Escolha: ')).strip().upper()

sleep(0.5)
print('\033[3;97m\nJO', end='')
sleep(1)
print('KEN', end='')
sleep(1)
print('PÔ\n')
sleep(1)

if escolhaPlayer == escolhaCPU:
    print('\033[1;33m!!!EMPATE!!! =|')
elif escolhaPlayer == 'PEDRA' and escolhaCPU == 'TESOURA':
    print('\033[1;32m!!!GANHOU!!! =)')
elif escolhaPlayer == 'PAPEL' and escolhaCPU == 'PEDRA':
    print('\033[1;32m!!!GANHOU!!! =)')
elif escolhaPlayer == 'TESOURA' and escolhaCPU == 'PAPEL':
    print('\033[1;32m!!!GANHOU!!! =)')
elif escolhaPlayer == 'PEDRA' and escolhaCPU == 'PAPEL':
    print('\033[1;91m!!!PERDEU!!! =(')
elif escolhaPlayer == 'TESOURA' and escolhaCPU == 'PEDRA':
    print('\033[1;91m!!!PERDEU!!! =(')
elif escolhaPlayer == 'PAPEL' and escolhaCPU == 'TESOURA':
    print('\033[1;91m!!!PERDEU!!! =(')

print(f'\033[1;34m\nA CPU escolheu {escolhaCPU} e VOCÊ escolheu {escolhaPlayer}.')