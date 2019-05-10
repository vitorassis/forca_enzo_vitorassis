import random
import unidecode

class Forca :
    def is_repeated(self, palavras, words, i):
        return words[i].split(',')[0] in palavras

    def __init__(self, palavras):
        with open("BDWords.zzt",'r') as f:
            words = f.read().split('\n')
        if len(palavras) == len(words):
            self.palavra = None
        else:
            index = random.randint(0,len(words)-1)
            while self.is_repeated(palavras=palavras, words=words, i=index):
                index = random.randint(0,len(words)-1)
            palavra = words[index].split(',')
            self.palavra, self.dica = palavra[0], palavra[1]
            self.chances = 7
            self.letras = []
            self.wrongLetras = []
            self.tamanho = len(self.palavra)

    def get_char(self,i):
        palavra = unidecode.unidecode(self.palavra)
        if palavra[i] in self.letras:
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
