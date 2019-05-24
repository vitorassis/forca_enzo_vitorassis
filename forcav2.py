from src.forca import Forca
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

menu = 9
sair = False
palavras = []
categorias = []
categoria = ''
nome = ''
pontuacao=0

def draw_header(fim=False):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=========== Jogo da Forca ===========')
    print('Coded by Vitor Assis & %s ' % ('Enzo Benvengo' if not fim else 'Cristhian Figueredo'))
    print('=====================================')

def draw_interface(fim= False):
    draw_header(fim)
    print('Pontuação: %d' % pontuacao)
    print('Erradas: %s' % jogo.show_wrong_letras())
    print()
    print(des_forca[7 - jogo.chances])
    print()
    print('Categoria: %s' % categoria)
    print('Dica: %s' % jogo.dica)
    print()
    print()
    for i in range(jogo.tamanho):
        print('%c ' % jogo.get_char(i),end='')
    print()
    print()
    print("DIGITE UMA LETRA OU /PALAVRA (/0 - Sair)")
    print()

while not sair:
    jogo = Forca(palavras)
    if menu == 9:
        draw_header()
        print('Menu:')
        print('1-> Jogar')
        print('2-> Ranking')
        print('\n0-> Sair')
        menu = input('#> ')
        menu = int(menu if menu.isnumeric() and int(menu) <3 and int(menu) >=0 else 9)
    elif menu == 1:
        cats = jogo.get_categorias()
        num = 1
        if nome == '':
            draw_header()
            nome = input('#> Nome: ')
            nome = nome if len(nome) <=6 else ''
        if nome != '':
            if categoria == '':
                draw_header()
                print('Selecione uma categoria: ')
                for cat in cats:
                    print('%d -> %s' % (num, cat))
                    num +=1
                print('\n%d -> Voltar ao menu' % num)
                entry = input('#> ')
                if entry.isnumeric():
                    entry = int(entry)
                    if entry > 0 and entry <= len(cats):
                        categoria = cats[entry-1]
                        categorias.append(categoria)
                    if entry == len(cats)+1:
                        op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                        while op != 's' and op != 'n':
                            op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                        if op == 's':
                            jogo.salvar_pontuacao(nome, pontuacao)
                        menu = 9
        if categoria != '':
            jogo = Forca(palavras, categoria, categorias)
            if jogo.palavra != None:
                palavras.append('%s-%s' % (categoria, jogo.palavra))

            while jogo.palavra != None and jogo.palavra != '404' and jogo.chances > 0 and not jogo.get_ganhou():
                draw_interface()
                letra = input('#> ')
                if letra.isalpha() and len(letra)==1:
                    jogo.marca_letra(letra)
                if len(letra) > 0 and letra[0] == '/':
                    jogo.testa_palavra(letra)
                if letra == '/0':
                    op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>' %(nome, pontuacao)).lower()
                    while op != 's' and op != 'n':
                            op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                    if op == 's':
                        jogo.salvar_pontuacao(nome, pontuacao)
                    exit()

            if jogo.palavra == '404':
                print('Sem conexão com a internet, tente novamente depois :\'(')
                sair = True
            
            if jogo.palavra != None and jogo.get_ganhou()==False:
                print('QUE PENA, VOCÊ ERROU! A PALAVRA ERA: %s' % jogo.palavra.capitalize())
            elif jogo.palavra != None:
                pontuacao += jogo.pontuacao
                #jogo.salvar_pontuacao(nome, pontuacao)
                draw_interface(True)
                print('VOCÊ ACERTOU! A PALAVRA ERA: %s' % jogo.palavra.capitalize())
            if jogo.palavra != None:
                de_novo = input('Deseja jogar de novo? <S/N> (M- Jogar de novo e trocar a categoria) ')
                while de_novo.lower() != 's' and de_novo.lower() != 'n' and de_novo.lower() != 'm':
                    de_novo = input('Deseja jogar de novo? <S/N>  (M- Jogar de novo e trocar categoriaia) ')
                if de_novo.lower() == 'm':
                    de_novo = 's'
                    categoria = ''
                if de_novo.lower() == 'n':
                    op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>' %(nome, pontuacao)).lower()
                    while op != 's' and op != 'n':
                        op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                    if op == 's':
                        jogo.salvar_pontuacao(nome, pontuacao)
                    exit()
            
            else:
                print('Acabaram nossas palavras, cadastre mais pelo editor.py ^-^\nRetornando à seleção de categrias...')
                categoria = ''
                input()
    elif menu == 2:
        draw_header()
        top = 10
        print('Ranking! (%d melhores pontuações)' % top)
        print()
        posicao = 1
        rank = jogo.get_ranking(top)
        if len(rank):
            print('Posição\tNome\tPontos')
            for player in rank:
                print('%dº\t%s\t%d' % (posicao, player['nome'], player['pontos']))
                posicao += 1
        else:
            print('Sem registros, jogue!')
        input("Aperte <Enter> para voltar.")
        menu = 9
    else:
        sair = True