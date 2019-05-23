from forca import Forca
import os

des_forca = ['''
 +---+
 |   |
     |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |    
=========
''']

def draw_interface(fim= False):
    os.system('cls' if os.name == 'nt' else 'clear')

    print('=========== Jogo da Forca ===========')
    print('Coded by Vitor Assis & %s ' % ('Enzo Benvengo' if not fim else 'Cristhian Figueredo'))
    print('=====================================')
    print()
    print('Erradas: %s' % jogo.show_wrong_letras())
    print()
    print(des_forca[6 - jogo.chances])
    print()
    print('Categoria: %s' % categoria)
    print('Dica: %s' % jogo.dica)
    print()
    print()
    for i in range(jogo.tamanho):
        print('%c ' % jogo.get_char(i),end='')
    print()
    print()
    print("DIGITE UMA LETRA OU /PALAVRA")
    print()


os.system('color 2' if os.name == 'nt' else '')
de_novo = 's'

palavras = []

categorias = []
categoria = None

while de_novo.lower() == 's':
    jogo = Forca(palavras, categoria, categorias)
    if categoria != None:
        if jogo.palavra != None:
            palavras.append('%s-%s' % (categoria, jogo.palavra))

        while jogo.palavra != None and jogo.palavra != '404' and jogo.chances > 0 and not jogo.get_ganhou():
            draw_interface()
            letra = input('#> ')
            if letra.isalpha() and len(letra)==1:
                jogo.marca_letra(letra)
            if len(letra) > 0 and letra[0] == '/':
                jogo.testa_palavra(letra)

        if jogo.palavra == '404':
            print('Sem conexão com a internet, tente novamente depois :\'(')
            exit()
        
        if jogo.palavra != None and jogo.get_ganhou()==False:
            print('QUE PENA, VOCÊ ERROU! A PALAVRA ERA: %s' % jogo.palavra.capitalize())
        elif jogo.palavra != None:
            draw_interface(True)
            print('VOCÊ ACERTOU! A PALAVRA ERA: %s' % jogo.palavra.capitalize())
        if jogo.palavra != None:
            de_novo = input('Deseja jogar de novo? <S/N> (M- Jogar de novo e trocar a categoria) ')
            while de_novo.lower() != 's' and de_novo.lower() != 'n' and de_novo.lower() != 'm':
                de_novo = input('Deseja jogar de novo? <S/N>  (M- Jogar de novo e trocar categoriaia) ')
            if de_novo.lower() == 'm':
                de_novo = 's'
                categoria = None
        
        else:
            print('Acabaram nossas palavras, cadastre mais pelo editor.py ^-^\nRetornando à seleção de categrias...')
            categoria = None
            input()
    elif jogo.palavra != '404':
        os.system('cls' if os.name == 'nt' else 'clear')
        cats = jogo.get_categorias()
        num = 1
        print('Selecione uma categoria: ')
        for cat in cats:
            print('%d -> %s' % (num, cat))
            num +=1
        print('\n0 -> Sair')
        entry = input('#> ')
        if entry.isnumeric():
            entry = int(entry)
            if entry > 0 and entry <= len(cats):
                categoria = cats[entry-1]
                categorias.append(categoria)
            if entry == 0:
                exit()

    else:
        print('Sem conexão com a internet, tente novamente depois :\'(')
        exit()
