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
#os.system('color 2' if os.name == 'nt' else '')
de_novo = 's'

palavras = []

def interface(game=True):
	os.system('cls' if os.name == 'nt' else 'clear')

	print('=========== Jogo da Forca ===========')
	print('Coded by Vitor Assis & %s' % ('Enzo Benvengo' if game else 'Cristhian Figueredo'))
	print('=====================================')
	print()
	print('Erradas: %s' % jogo.show_wrong_letras())
	print()
	print(des_forca[7 - jogo.chances])
	print()
	print()
	print('Dica: %s' % jogo.dica)
	print()
	print()
	for i in range(jogo.tamanho):
		print('%c ' % jogo.get_char(i),end='')
	print()
	print()	
	print("DIGITE UMA LETRA OU /PALAVRA" if game else '')
	print()

while de_novo.lower() == 's':
    jogo = Forca(palavras)
    palavras.append(jogo.palavra)

    while jogo.palavra != None and jogo.chances > 0 and not jogo.get_ganhou():
        interface()
        letra = input('#> ')
        if letra.isalpha() and len(letra)==1:
            jogo.marca_letra(letra)
        if len(letra) > 0 and letra[0] == '/':
            jogo.testa_palavra(letra)
    if jogo.palavra != None and jogo.get_ganhou()==False:
        print('QUE PENA, VOCÊ ERROU! A PALAVRA ERA: %s' % jogo.palavra.capitalize())
    elif jogo.palavra != None:
        os.system('cls' if os.name == 'nt' else 'clear')

        interface(False)
        print('VOCÊ ACERTOU! A PALAVRA ERA: %s' % jogo.palavra.capitalize())
    if jogo.palavra != None:
        de_novo = input('Deseja jogar de novo? <S/N> ')
        while de_novo.lower() != 's' and de_novo.lower() != 'n':
            de_novo = input('Deseja jogar de novo? <S/N> ')
    else:
        print('Acabaram nossas palavras, cadastre mais pelo editor.py ^-^')
        exit()
