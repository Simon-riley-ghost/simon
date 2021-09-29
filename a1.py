import os
import colorama
colorama.init()
a2 = True
while a2:
    print("""\033[1;33m
    inteface mais simples porém dinamica e informativa

                baixar IDEs
    01.  Visual Studio Code
    02.  Atom
    03.  Notepad ++
    04.  Jupyter
    05.  Pycharm
    06.  Wing Python IDE
    07.  Thonny
    08.  IDLE Python IDE
    09.  Pydev
    10.  Elpy
    11.  Komodo IDE
                 importancia
    12.  Qual a diferença entre IDE e Editor de Código?
    13.  Por que usar um IDE
    14.  Debugger
    15. Sair
    """)
    dec = input("opção: ")
    if dec == '1': # Visual Studio Code
        os.system('start https://code.visualstudio.com/')
    elif dec == '2': # atom
        os.system('start https://atom.io/')
    elif dec == '3': # notepad ++
        os.system('start https://notepad-plus-plus.org/downloads/')
    elif dec == '4': # Jupyter
        os.system('start https://jupyter.org/')
    elif dec == '5': # Pycharm
        os.system('start https://www.jetbrains.com/pt-br/pycharm/download/#section=windows')
    elif dec == '6': # Wing Python IDE
        os.system('start https://wingware.com/')
    elif dec == '7': # Thonny
        os.system('start https://thonny.org/')
    elif dec == '8': # IDLE Python IDE
        print(' site ofc da python a IDE ja vem junto com o pacote')
        os.system('start https://www.python.org/downloads/')
    elif dec == '9': # Pydev
        os.system('start Pydev.org')
    elif dec == '10': # Elpy
        os.system('start https://elpy.readthedocs.io/en/latest/')
    elif dec == '11': # Komodo IDE
        os.system('start https://www.activestate.com/products/komodo-ide/')
    elif dec == '12': #
        print('')
    elif dec == '13':
        print('')
    elif dec == '14':
        print('')
    elif dec == '15':
        exit()
    a2 = None
else:
    print ('opção ivalida...')
