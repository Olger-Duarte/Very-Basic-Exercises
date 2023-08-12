###
#Juego del ahorcado: Implementa el juego del ahorcado en el que el jugador debe adivinar una palabra oculta letra por letra.
##

import random
import os

secret_words = [
    "manzana",
    "perro",
    "gato",
    "casa",
    "árbol",
    "coche",
    "pelota",
    "libro",
    "mesa",
    "silla",
    "sol",
    "playa",
    "ciudad",
    "jardín",
    "flor",
    "verde",
    "azul",
    "rojo",
    "amarillo",
    "naranja",
    "blanco",
    "negro",
    "música",
    "familia",
    "amigo"
]


choosen_word = secret_words[random.randrange(25)]
word_split = ['_' for _ in choosen_word]

print(f"The word is:  {' '.join(word_split)} \n")

def hangman(letter,word):
    
    if len(letter) == len(word):
        if letter.lower() == word:
            return f"The word was {word.capitalize()}"
        else:
            return "Tray again"
    else:
        for i, character in enumerate(word):
            if character == letter:
                word_split[i] = character
        return ' '.join(word_split) if "_" in word_split else f"The word was{''.join(word_split).capitalize()}"

for _ in range(len(choosen_word)):
    #os.system('cls')
    print(hangman(input("Enter a letter or word: "), choosen_word))
    