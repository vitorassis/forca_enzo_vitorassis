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
setting_to_change =99

def draw_header(fim=False):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=========== Jogo da Forca ===========')
    print('Coded by Vitor Assis & %s ' % ('Enzo Benvengo' if not fim else 'Cristhian Figueredo'))
    print('=====================================')

def draw_interface(fim= False):
    draw_header(fim)
    if jogo.get_setting("show_max_pnt"):
        print('Pontuação Máxima: %d' % jogo.pontos_max)
    else:
        print()
    print('Pontuação: %d' % pontuacao, end = ' ' if jogo.get_setting('show_nome') else '\n')
    if jogo.get_setting('show_nome'):
        print('\t\tNome: %s' % nome)
    print('Erradas: %s' % jogo.show_wrong_letras())
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
        print()
        print('1-> Jogar')
        print('2-> Ranking')
        print('3-> Configurações')
        print('\n0-> Sair')
        menu = input('#> ')
        menu = int(menu if menu.isnumeric() and int(menu) <4 and int(menu) >=0 else 9)
    elif menu == 1:
        cats = jogo.get_categorias()
        if jogo.palavra != '404':
            num = 1
            if nome == '':
                draw_header()
                print('Jogar:')
                print()
                nome = input('#> Nome (0-> Voltar ao menu): ')
                nome = nome if len(nome) <=6 else nome[0:6]
                if nome.isnumeric() and int(nome) == 0:
                    menu = 9
                    nome = ''
            if nome != '':
                if categoria == '':
                    draw_header()
                    print('Jogar')
                    print()
                    print('Pontuação: %d' % pontuacao, end = ' ' if jogo.get_setting('show_nome') else '\n')
                    if jogo.get_setting('show_nome'):
                        print('\t\tNome: %s' % nome)
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
                            if pontuacao > 0:
                                op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                                while op != 's' and op != 'n':
                                    op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                                if op == 's':
                                    jogo.salvar_pontuacao(nome, pontuacao)
                            menu = 9
        else:
            print('Sem conexão com a internet, tente novamente depois :\'(')
            sair = True
        if categoria != '':
            jogo = Forca(palavras, categoria, categorias)
            if jogo.palavra != None:
                palavras.append('%s-%s' % (categoria, jogo.palavra))

            while not sair and jogo.palavra != None and jogo.palavra != '404' and jogo.chances > 0 and not jogo.get_ganhou():
                draw_interface()
                letra = input('#> ')
                if letra.isalpha() and len(letra)==1:
                    jogo.marca_letra(letra)
                if len(letra) > 0 and letra[0] == '/':
                    jogo.testa_palavra(letra)
                if letra == '/0':
                    if pontuacao > 0:
                        op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                        while op != 's' and op != 'n':
                            op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                        if op == 's':
                            jogo.salvar_pontuacao(nome, pontuacao)
                    exit()

            if jogo.palavra == '404':
                print('Sem conexão com a internet, tente novamente depois :\'(')
                sair = True
            
            if jogo.palavra != None and not sair and jogo.get_ganhou()==False:
                print('QUE PENA, VOCÊ ERROU! A PALAVRA ERA: %s' % jogo.palavra.capitalize())
            elif jogo.palavra != None and not sair:
                pontuacao += jogo.pontuacao
                #jogo.salvar_pontuacao(nome, pontuacao)
                draw_interface(True)
                print('VOCÊ ACERTOU! A PALAVRA ERA: %s' % jogo.palavra.capitalize())
            if jogo.palavra != None and not sair:
                de_novo = input('Deseja jogar de novo? <S/N> (M- Jogar de novo e trocar a categoria) ')
                while de_novo.lower() != 's' and de_novo.lower() != 'n' and de_novo.lower() != 'm':
                    de_novo = input('Deseja jogar de novo? <S/N>  (M- Jogar de novo e trocar categoriaia) ')
                if de_novo.lower() == 'm':
                    de_novo = 's'
                    categoria = ''
                if de_novo.lower() == 'n':
                    if pontuacao > 0:
                        op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                        while op != 's' and op != 'n':
                            op = input('%s, deseja salvar a pontuação de: %d pontos? <S/N>'%(nome, pontuacao)).lower()
                        if op == 's':
                            jogo.salvar_pontuacao(nome, pontuacao)
                    exit()
            
            elif not sair:
                print('Acabaram nossas palavras, cadastre mais pelo editor.py ^-^\nRetornando à seleção de categrias...')
                categoria = ''
                input()
    elif menu == 2:
        draw_header()
        top = jogo.get_setting('top_rank')
        posicao = 1
        rank = jogo.get_ranking(top)
        if jogo.palavra != '404':
            print('Ranking! (%d melhores pontuações)' % top)
            print()
            if len(rank):
                print('Posição\tNome\tPontos')
                for player in rank:
                    print('%dº\t%s\t%d' % (posicao, player['nome'], player['pontos']))
                    posicao += 1
                while posicao <= top:
                    print('%dº\t--\t--' % (posicao))
                    posicao += 1
            else:
                print('Sem registros, jogue!')
            input("Aperte <Enter> para voltar.")
            menu = 9
        else:
            print('Sem conexão com a internet, tente novamente depois :\'(')
            sair = True
    elif menu == 3:
        if setting_to_change == 99:
            draw_header()
            settings = jogo.get_settings()

            if jogo.palavra != '404':
                print('Selecione a configuração que deseja alterar:\n')
                op = 1
                for setting in settings:
                    print('%d-> %s: %s' %(op, setting['nome'], str(setting['valor'])))
                    op += 1
                print('\n0-> Voltar ao menu   ')
                entry = input('#> ')
                setting_to_change = int(entry if entry.isnumeric() and int(entry) <op and int(op) >=0 else 99)
                if setting_to_change == 0:
                    menu = 9
                    setting_to_change = 99
            else:
                print('Sem conexão com a internet, tente novamente depois :\'(')
                sair = True

        else:
            entry = int(entry)
            if entry > 0 and entry < op:
                draw_header()
                op=1
                print('Alterar a configuração de: %s' % settings[entry-1]['nome'])
                print()
                for opcao in settings[entry-1]['opcoes']:
                    print('%d-> %s' % (op, opcao))
                    op+=1
                option = input('#> ')
                option = int(option if option.isnumeric() and int(option) <op and int(option) >=0 else 1000)
                if option != 1000:
                    jogo.salvar_setting(entry-1, option-1)
                    setting_to_change = 99
    else:
        sair = True