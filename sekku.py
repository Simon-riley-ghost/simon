#                                   bloco 0
import os, time , colorama 
os.system('cls')
print ('instalando recursos...')
" "

colorama.init()
# variavel de cores
padrão = '\033[0;0m' 
cinza_es = '\033[1;90m';fun_cinza = '\033[1;100m'
vermelho = '\033[1;31m';fun_vermelho = '\033[1;41m'
magenta = '\033[1;35m';fun_magenta = '\033[1;45m'
verde = '\033[1;32m';fun_verde = '\033[1;42m'
amarelo = '\033[1;33m';fun_amarelo = '\033[1;43m'
azul = '\033[1;34m'; fun_azul = '\033[1;44m'
print ('Definindo variavels... Aguarde ate o fim do processo')
time.sleep(3)
print(f'{azul}pronto  as seguintes blibliotecas foram instalada... colorama ')
print ('\033[1;35minsira a senha para confirma identidade..')
menu1 = True
while menu1:
    print(f'''{cinza_es}
    [1]  logica de programação
    [2]  cursos
    [3]  ciencias quantica
    [4]  anatomia humana 
    [5]  deep web
    [6]  projetos  
    [7]  melhores linguagems
    [8]  livros 
    [9]  jogos
    [10] musicas
    [11] melhores repo do github
    [12] about
    [13] exit\quit\sair
    {padrão}''')
    dec = input("opção: ")
    if dec == '1':
        os.system('start https://downloadcursos.top/logica-de-programacao/')
    elif dec == '2':
        os.system('start https://downloadcursos.top/')
    elif dec == '3':
        os.system('start https://books.scielo.org/id/xwhf5/pdf/freire-9788578791261.pdf')
    elif dec == '4':
        os.system('start https://brazilianjournals.com.br/assets/ebooks/11074e35552614e6bcfc57545790ce70.pdf')
    elif dec == '5':
        print(f'Bem você ira abaixar o Broser Tor no google "https://www.torproject.org/download/" logo apos baixa você vai instalar ele e executar e dai tu coloca HIDDEN WIKI e logo apos selecione o site \n bem isso e um metodo simplis para a navegação simples nn abaixe nd de la ')
    elif dec == '6':
        print(f'bem eu tenho o projeto sekku,simon e o a1 eles são painel educativo vou ver se implanto ele aqui ')
    elif dec == '7':
        print(f'''bem nn existe linguagems melhores uma doque a outra apenas uma que se encaixa melhor em cada coisa mais esse e o topico delas As 5 linguagens de programação mais usadas em 2021
        1 – Python. Python tem como diferencial a facilidade no aprendizado
        2 – Java. Java é uma das linguagens mais utilizadas no mundo.
        3 – C++ (e C) C++ e C são duas linguagens geralmente aprendidas nas faculdades de tecnologia.
        4 – JavaScript. 
        5 – Go.''')
    elif dec == '8':
        os.system('start https://www3.livrariacultura.com.br/')
    elif dec == '9':
        print('call of duty todos eles \nneed for speed a saga toda \nsniper elite todos eles\ngod of war desde do 2 ate o ragnarok\nbatllefields desde 3 ate o 5\ndead cells\n CS 1.6 e CS:GO e gta desde do san andreas ate o 5')
    elif dec == '10':
        from menus import musicas
    elif dec == '11':
        print('off ate eu acha os melhores')
    elif dec == '12':
        print('bem me chamo miguel adoro porgramar em python e estou aprendendo OS e essas coisas ent o codigo pode dar erro okay ')
    elif dec == '13':
        print('Okay fechando')
        exit()
    else:  
            print(f'{vermelho}{fun_amarelo}opção invalida')







