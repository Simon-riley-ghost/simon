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
import colorama, time, os
os.system('cls')
#   executara uma aba de login não grafica você tera que ter senha e usuario para entra
login = 1
if login == 1:
    user = 'miguel'
    if input('User: ') .strip() == user:
        print('\033[1;35mBuascando dados...') # coloquei apenas por stazk
    else: # caso não exista usuario ele ira dizer espera um time e fecha o progrma
        print('usuario não existe')
        time.sleep(3)
        os.system('cls')
        exit()
    time.sleep(1)
    print('\033[1;35mdados encontrados...')
    print ('\033[1;35minsira a senha para confirma identidade..') # ele ira te pedir a senha e a senha tem que ser igual
    snh = '1812'
    if input('Pass: ') .strip() == snh: #vai confirma se a senha e valida
     print ('''\033[1;35m
    informação de login:
    Nome > Simon Riley
    Codenome > Ghost
    Frase > Um novo dia a mesma merda
    ''')
    else:  # caso a senha não seja ele irar fechar o script
        print ('\033[1;31mOps você não tem autorização para entrar no painel')
        exit()
ans=True
while ans:
    print('\033[1;35mpainel dedicado aos estudos então so tem conteudo aqui \n[1] sobre o nazismo \n[2] sobre o comunismo \n[3] jogos para pc \n[4] sobre a guerra fria \n[5] historia do brasil \n[6] sobre a revolução industrial \n[7] sair \n[8] caso o limpador automatico nn limpe \n[9] proximo menu\n[10] sekku')
    dec = input("opção: ")
    if dec == '1':
        os.system('start https://es.wikipedia.org/wiki/Nazismo')
    elif dec == '2':
        os.system('start https://es.wikipedia.org/wiki/Comunismo')
    elif dec == '3':
        print ('cod 4 mw \ncod mw 2 \nneed for speed \nsniper elite 2 e 3 \nbrawahalla \nGTA SA, GTA 3, GTA Vice City e MTA ')
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
    elif dec == '9':
        os.system('cls')
        from menus import a1
    elif dec == '10':
        from menus import sekku
else:
    print('opção invalida')