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


os.system('color 2' if os.name == 'nt' else '')
de_novo = 's'

palavras = []

categorias = []
categoria = None

draw_header()
nome = input('#> Nome: ')
while nome == '' and len(nome) > 6:
    nome = input('#> Nome: ')

while de_novo.lower() == 's':
    jogo = Forca(palavras, categoria, categorias)
    if categoria != None and categoria != 'rank':
        
    elif categoria == 'rank':
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
        categoria = None
    elif jogo.palavra != '404':
        draw_header()
        cats = jogo.get_categorias()
        num = 1
        print('Selecione uma categoria: ')
        for cat in cats:
            print('%d -> %s' % (num, cat))
            num +=1
        print('\n%d -> Ranking' % num)
        print('0 -> Sair')
        entry = input('#> ')
        if entry.isnumeric():
            entry = int(entry)
            if entry > 0 and entry <= len(cats):
                categoria = cats[entry-1]
                categorias.append(categoria)
            if entry == 0:
                op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                while op != 's' and op != 'n':
                    op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                if op == 's':
                    jogo.salvar_pontuacao(nome, pontuacao)
                sair = True
            if entry == len(cats)+1:
                categoria = 'rank'
    else:
        print('Sem conexão com a internet, tente novamente depois :\'(')
        sair = True
