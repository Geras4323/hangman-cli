import os
import random

EQUIVALENCES = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u"
}

def file_opening(directory, mode):
    f = open(directory, mode, encoding="utf-8")
    return f

def word_loading(file):
    word_list = []          # va a contener todas las palabras
    for word in file:       # guardar cada palabra en la lista
        word_list.append(str(word))
    return word_list

def word_picking(word_list):
    rand_word = random.choice(word_list)        # agarra una palabra de la lista al azar
    word = [w for w in rand_word if w != "\n"]  # crea una lista con rand_word sin "\n"
    return word                                 # devuelve la palabra en formato de lista

def word_ready(word):
    final_word = []
    for letter in word:     # por cada letra en la palabra
        for key, value in EQUIVALENCES.items():     # por cada entrada del diccionario
            if letter == key:       # si hay algun acento
                letter = value      # reemplazarlo por la misma letra sin acento
        final_word.append(letter.upper())
    return final_word

def create_undscs(word):
    undscs_list = []
    for i in word:
        undscs_list.append("_")
    return undscs_list

def replace(word, undscs, u_input):
    for index, value in enumerate(word):
        if u_input == value:
            undscs[index] = u_input
            # change = True ### para las vidas


def run():
    file = file_opening("./archivos/data.txt", "r")      # abrimos el archivo data.txt
    words = word_loading(file)     # cargamos las palabras en una lista
    chosen_word = word_picking(words)   # pido una palabra al azar de la lista y la recibo como lista
    final_word = word_ready(chosen_word)    # saca acentos y pone la palabra en mayuscula
    underscores = create_undscs(final_word)     # tengo otra lista que tenga un "_" por cada letra de la palabra
    os.system("cls")               # limpiamos pantalla
    while underscores != final_word:    # mientras las listas sean distintas, mostrar la lista a medida que se va completando
        print("- Ahorcado! -")
        print(" ".join(underscores))
        user_input = str(input("Ingrese una letra: ")).upper()
        replace(final_word, underscores, user_input)
        os.system("cls")
    
    print("La palabra era: ", ("". join(final_word)))
    file.close()


if __name__ == '__main__':
    run()