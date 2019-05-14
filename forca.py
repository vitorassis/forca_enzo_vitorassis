import random
import unidecode
import json
from urllib.request import urlopen

class Forca :
    def is_repeated(self, palavras, words, i, categoria):
        search = '%s-%s' % (categoria, words[categoria][i]['palavra'])
        return search in palavras

    def is_connected(self):
        try:
            urlopen('https://www.google.com/', timeout=10)
            return True
        except: 
            return False                                                                                                                                                                                                                                                                                                                          

    def __init__(self, palavras, categoria = None):
        if self.is_connected():
            if categoria != None:
                words = json.loads(urlopen('https://raw.githubusercontent.com/vitorassis/db_forca_enzo_vitorassis/master/BDWords.json').read())
                #with open("BDWords.json",'r') as f:
                #    words = f.read()
                #words = json.loads(words)
                if len(palavras) == len(words[categoria]):
                    self.palavra = None
                else:
                    index = random.randint(0,len(words[categoria])-1)
                    while self.is_repeated(palavras=palavras, words=words, i=index, categoria=categoria):
                        index = random.randint(0,len(words[categoria])-1)
                    palavra = words [categoria][index]
                    self.palavra, self.dica = palavra['palavra'], palavra['dica']
                    self.chances = 7
                    self.letras = []
                    self.wrongLetras = []
                    self.tamanho = len(self.palavra)
            else:
                self.palavra = ''
        else:
            self.palavra = '404'
        
    def get_categorias(self):
        #with open("BDWords.json",'r') as f:
        #    words = f.read()
        #words = json.loads(words)
        words = json.loads(urlopen('https://raw.githubusercontent.com/vitorassis/db_forca_enzo_vitorassis/master/BDWords.json').read())
        return list(words.keys())

    def get_char(self,i):
        palavra = unidecode.unidecode(self.palavra)
        if palavra[i] in unidecode.unidecode(''.join(self.letras)):
            return self.palavra[i].upper()
        elif self.palavra[i] != ' ':
            return '_'
        else:
            return ' '
        
    def diff_letra(self, letra):
        return letra not in self.wrongLetras and letra not in self.letras

    def marca_letra(self,letra):
        letra = letra.lower()
        self.palavra = self.palavra.lower()
        print(unidecode.unidecode(self.palavra))
        if unidecode.unidecode(letra) in unidecode.unidecode(self.palavra) and self.diff_letra(letra):
            self.letras.append(letra)
            return True
        elif self.diff_letra(letra):
            self.wrongLetras.append(letra)
            self.chances -= 1
            return True
        else:
            return False

    def testa_palavra(self, palavra):
        palavra = palavra[1:]
        if unidecode.unidecode(palavra.lower()) == unidecode.unidecode(self.palavra.lower()):
            for letra in palavra:
                self.marca_letra(letra)
        else:
            self.chances-=1

    def get_ganhou(self):
        for i in range(self.tamanho):
            if self.get_char(i) == '_':
                return False
        return True

    def show_wrong_letras(self):
        letras = ''
        for letra in self.wrongLetras:
            letras += letra.upper() + ' '
        return letras
