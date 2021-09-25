#   Cor	       Fonte	Fundo
#   Preto	\033[1;30m	\033[1;40m
#    Vermelho	\033[1;31m	\033[1;41m
#    Verde	\033[1;32m	\033[1;42m
#    Amarelo	\033[1;33m	\033[1;43m
#    Azul	\033[1;34m	\033[1;44m
#    Magenta	\033[1;35m	\033[1;45m
#    Cyan	\033[1;36m	\033[1;46m
#    Cinza Claro	\033[1;37m	\033[1;47m
#    Cinza Escuro	\033[1;90m	\033[1;100m
#    Vermelho Claro	\033[1;91m	\033[1;101m
#    Verde Claro	\033[1;92m	\033[1;102m
#    Amarelo Claro	\033[1;93m	\033[1;103m
#    Azul Claro	\033[1;94m	\033[1;104m
#    Magenta Claro	\033[1;95m	\033[1;105m
#    Cyan Claro	\033[1;96m	\033[1;106m
#    Branco	\033[1;97m	\033[1;107m
#    Negrito	\033[;1m	-
#    Inverte	\033[;7m	-
#    Reset (remove formatação)	\033[0;0m

# o codigo se trata de passar conhecimento para todo o publico sem fins lucrativos 
# desenvolvido por Miguel D.m

#                                                   codigo                                                                                      
from colorama import init
init()
import os
import time
os.system('cls')
login = 1
if login == 1:
    user = 't'
    if input('User: ') .strip() == user:
        print('\033[1;35mBuascando dados...')
    else:
        print('usuario não existe')
        time.sleep(3)
        os.system('cls')
        exit()
    time.sleep(4)
    print('\033[1;35mdados encontrados...')
    print ('\033[1;35minsira a senha para confirma identidade..')
    snh = 't'
    if input('Pass: ') .strip() == snh:
     print ('''\033[1;35m
    informação de login:
    Nome > Simon Riley 
    Codenome > Ghost
    Frase > Um novo dia a mesma merda 
    ''')
    else:
        print ('\033[1;31mOps você não tem autorização para entrar no painel')
        exit()
ans=True
while ans:
    print('\033[1;35mpainel dedicado aos estudos então so tem conteudo aqui \n[1] sobre o nazismo \n[2] sobre o comunismo \n[3] jogos para pc \n[4] sobre a guerra fria \n[5] historia do brasil \n[6] sobre a revolução industrial \n[7] sair \n[8] caso o limpador automatico nn limpe')
    dec = input("opção: ")
    if dec == '1':
        os.system('start https://es.wikipedia.org/wiki/Nazismo')
    elif dec == '2':
        os.system('start https://es.wikipedia.org/wiki/Comunismo')
    elif dec == '3':
        print ('[1] cod 4 mw \n[2] cod mw 2 \n[3] need for speed \n[4] sniper elite 2 e 3 \n[4] brawahalla \n[5] GTA SA, GTA 3, GTA Vice City e MTA ')
    elif dec == '4':
        os.system('start https://es.wikipedia.org/wiki/Guerra_Fr%C3%ADa')
    elif dec == '5':
        os.system('start https://es.wikipedia.org/wiki/Brasil')
    elif dec == '6':
        os.system('start https://es.wikipedia.org/wiki/Revolu%C3%A7%C3%A3o_industrial')
    elif dec == '7':    
        exit()
    elif dec == '8':
        os.system('cls')
    ans= None
else:
    print('tente novamente ...')
    


























