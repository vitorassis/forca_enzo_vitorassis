import os

os.system('color 3')
print('====== Jogo da Forca - EDITOR =======')
print('Coded by Vitor Assis & Enzo Benvengo ')
print('=====================================')
print()
newPalavra = input("#> Palavra: ")
while newPalavra != '':
    dica = input('#> Dica: ')
    with open("BDWords.zzt",'a') as f:
        f.write('\n'+newPalavra+','+dica)
    newPalavra = input("#> Palavra: ")



