import random
import unidecode
import json
from urllib.request import urlopen
import os

class Forca:
    def is_repeated(self, palavras, words, i, categoria):
        search = '%s-%s' % (categoria, words[categoria][i]['palavra'])
        #print(search)
        return search in palavras

    def is_connected(self):
        #return False
        try:
            urlopen('https://raw.githubusercontent.com/vitorassis/db_forca_enzo_vitorassis/master/BDWords.json', timeout=10)
            return True
        except: 
            return False                                                                                                                                                                                                                                                                                                                          

    def get_max(self, words, categorias):
        soma = 0
        for i in categorias:
            soma += len(words[i])
        return soma

    def get_len_cat(self, categoria, palavras):
        return len([s for s in palavras if categoria in s])
            
    def __init__(self, palavras, categoria = None, categorias = []):
        if self.is_connected():
            if categoria != None and categoria != 'rank':
                read = urlopen('https://raw.githubusercontent.com/vitorassis/db_forca_enzo_vitorassis/master/BDWords.json').read().decode('utf-8')
                words = json.loads(read)
                if len(palavras) == self.get_max(words=words, categorias=categorias): #acabaram as palavras
                    self.palavra = None
                if self.get_len_cat(palavras=palavras, categoria=categoria) >= len(words[categoria]): #acabaram as palavras daquela categoria
                    self.palavra = None
                
                else:
                    index = random.randint(0,len(words[categoria])-1)
                    while self.is_repeated(palavras=palavras, words=words, i=index, categoria=categoria):
                       # print(index)
                        index = random.randint(0,len(words[categoria])-1)
                    palavra = words [categoria][index]
                    self.palavra, self.dica = palavra['palavra'], palavra['dica']
                    self.chances = 7
                    self.letras = []
                    self.wrongLetras = []
                    self.tamanho = len(self.palavra)
                    self.pontuacao = palavra['pontos']
                    self.pontos_max = self.pontuacao
            else:
                self.palavra = ''
        else:
            self.palavra = '404'
        
    def get_categorias(self):
        if self.is_connected():
            self.palavra = ''
            read = urlopen('https://raw.githubusercontent.com/vitorassis/db_forca_enzo_vitorassis/master/BDWords.json').read().decode('utf-8')
            words = json.loads(read)
            return list(words.keys())
        self.palavra = '404'
        return None

    def get_char(self,i):
        palavra = unidecode.unidecode(self.palavra)
        if palavra[i] in unidecode.unidecode(''.join(self.letras)):
            return self.palavra[i].upper()
        elif self.palavra[i] not in [' ', '-']:
            return '_'
        else:
            return self.palavra[i]
        
    def diff_letra(self, letra):
        return letra not in self.wrongLetras and letra not in self.letras

    def marca_letra(self,letra):
        letra = letra.lower()
        self.palavra = self.palavra.lower()
      #  print(unidecode.unidecode(self.palavra))
        if unidecode.unidecode(letra) in unidecode.unidecode(self.palavra) and self.diff_letra(letra):
            self.letras.append(letra)
            return True
        elif self.diff_letra(letra):
            self.wrongLetras.append(letra)
            self.chances -= 1
            self.pontuacao -= self.pontos_max * 0.14
            return True
        else:
            return False

    def testa_palavra(self, palavra):
        palavra = palavra[1:]
        if unidecode.unidecode(palavra.lower()) == unidecode.unidecode(self.palavra.lower()):
            for letra in palavra:
                self.marca_letra(letra)
            if self.chances == 7:
                self.pontuacao += self.pontos_max
        else:
            self.chances-=1
            self.pontuacao -= self.pontos_max * 0.14

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

    def get_ranking(self, posicoes = 10):
        if self.checkExist('db_scores.json'):
            dash = '\\' if os.name == 'nt' else '/'
            with open('files%sdb_scores.json' % dash, 'r') as f:
                read = f.read()
            scores = json.loads(read)
            scores = sorted(scores, key = lambda i: i['pontos'], reverse=True) 
            return scores[0:posicoes]

    def checkExist(self, file):
        dash = '\\' if os.name == 'nt' else '/'
        if os.path.exists('files%s%s' % (dash, file)):
            return True
        if self.is_connected():
            read = urlopen('https://raw.githubusercontent.com/vitorassis/db_forca_enzo_vitorassis/master/%s' % file).read().decode('utf-8')
            with open('files%s%s' % (dash, file), 'w+') as f:
                f.write(read)
            return True
        self.palavra = '404'
        return False

    def salvar_pontuacao(self, nome, pontuacao):
        if self.checkExist('db_scores.json'):
            dash = '\\' if os.name == 'nt' else '/'
            with open('files%sdb_scores.json' % dash, 'r') as f:
                read = f.read()
            scores = json.loads(read)
            scores.append(dict({'nome': nome, 'pontos': pontuacao}))
            scores = json.dumps(scores, indent=4)
            with open('files%sdb_scores.json' % dash, 'w') as f:
                f.write(scores)


    def get_settings(self):
        if self.checkExist('settings.json'):
            dash = '\\' if os.name == 'nt' else '/'
            with open('files%ssettings.json' % dash, 'r') as f:
                read = f.read()
            settings = json.loads(read)
            return settings

    def salvar_setting(self, setting, option):
        if self.checkExist('settings.json'):
            dash = '\\' if os.name == 'nt' else '/'
            settings = self.get_settings()
            settings[setting]['valor'] = settings[setting]['opcoes'][option]
            settings = json.dumps(settings, indent=4)
            with open('files%ssettings.json' % dash, 'w') as f:
                f.write(settings)

    def get_setting(self, cod):
        settings = self.get_settings()
        for setting in settings:
            if setting['cod'] == cod:
                return setting['valor']