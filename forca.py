import requests
#import re
from lxml import html  
#import csv,os,json
import unidecode
import os

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def carrega_palavra_secreta():
    url = "http://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1"
    resposta = requests.get(url)
    elemento = html.fromstring(resposta.content)
    palavra_secreta = elemento.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')
    palavra_secreta = palavra_secreta[0].strip()
    return palavra_secreta

# transformando a palavra em letras minusculas e sem acentos
palavra = carrega_palavra_secreta()
palavra = palavra.lower()
palavra = unidecode.unidecode(palavra)

resposta = '_'*len(palavra)
print(resposta)

##################### TIRAR COMENTÁRIO PARA TER A RESPOSTA
#print(palavra)
######################

letras_erradas = []
numero_de_vidas = 6

end_of_game = False
print(stages[numero_de_vidas])
while not end_of_game:
    letra = input("Escolha uma letra: ").lower()
    os.system('cls')

    for ii in range(len(palavra)):
        if palavra[ii] == letra:
            resposta = list(resposta)
            resposta[ii] = letra
            resposta = "".join(resposta)
        else:
            pass
    if letra not in palavra:
        letras_erradas.append(letra)
        numero_de_vidas -=1
        print("ERROU!")

    #Verificação de Letras Erradas
    print("Letras Erradas: ")
    print(letras_erradas)
    nblanks = resposta.count('_')
    print(resposta)

    if nblanks == 0:
        end_of_game = True
        print("Resposta: " + palavra.upper())
        print("Você Venceu!!!")
    elif numero_de_vidas == 0:
        end_of_game = True
        print("Você Perdeu.")
        print("Resposta: " + palavra.upper())

    print(stages[numero_de_vidas])
    print("\n")
