import os
import json

os.system('color 3')
print('====== Jogo da Forca - EDITOR =======')
print('Coded by Vitor Assis & Enzo Benvengo ')
print('=====================================')
print()
with open("BDWords.json",'r') as f:
    words = f.read()
if words != []:
    words = json.loads(words)
else:
    words = []
newPalavra = input("#> Palavra: ")
while newPalavra != '':
    dica = input('#> Dica: ')
    words.append({'palavra': newPalavra, 'dica': dica})
    newPalavra = input("#> Palavra: ")

with open("BDWords.json",'w') as f:
    f.write(json.dumps(words))