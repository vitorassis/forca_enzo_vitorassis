from random import randint
from asciimatics.screen import Screen

fim=False
pontuacao=100
erradas='A B C D'
des_forca = [
    [' +---+',' |   |','     |','     |','     |','     |    ','========='], 
    [' +---+',' |   |',' O   |','     |','     |','     |    ','========='], 
    [' +---+',' |   |',' O   |',' |   |','     |','     |    ','========='], 
    [' +---+',' |   |',' O   |','/|   |','     |','     |    ','========='] ,
    [' +---+',' |   |',' O   |','/|\  |','     |','     |    ','========='], 
    [' +---+',' |   |',' O   |','/|\  |','/    |','     |    ','========='], 
    [' +---+',' |   |',' O   |','/|\  |','/ \  |','     |    ','=========']
]
de_novo = 's'

def jogo(screen):
    while not fim:
        screen.print_at('=========== Jogo da Forca ===========',0, 0,colour=13)
        screen.print_at('Coded by Vitor Assis & %s ' % ('Enzo Benvengo' if not fim else 'Cristhian Figueredo'),0, 1,colour=13)
        screen.print_at('=========== Jogo da Forca ===========',0, 2,colour=13)
        screen.print_at('Pontuação: ',15, 4,colour=10)
        screen.print_at('%d'%pontuacao,26, 4,colour=3)
        screen.print_at('Erradas: ',15, 5,colour=10)
        screen.print_at('%s'%erradas,24, 5,colour=3)
        line=4
        for forca in des_forca[5]:
            screen.print_at('%s'%forca,0, line,colour=9)
            line+=1
        screen.print_at('_ _ _ _ _ _ _',10, 14,colour=10)

        letra = screen.get_key()
        try:
            if letra.isalpha() and len(letra)==1:
                jogo.marca_letra(letra)
            if len(letra) > 0 and letra[0] == '/':
                jogo.testa_palavra(letra)
        except:
            pass
        screen.refresh()


Screen.wrapper(jogo)

