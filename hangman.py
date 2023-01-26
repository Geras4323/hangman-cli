import os
import random
import sys
import time

EQUIVALENCES = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u"
}

def file_opening(directory, mode):
    try:
        f = open(directory, mode, encoding="utf-8")
        return f
    except FileNotFoundError:
        print("No se encontró el archivo con palabras.")
        sys.exit(1)

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
    change = False
    for index, value in enumerate(word):
        if u_input == value:
            undscs[index] = u_input
            change = True ### para las vidas
    return change

def chk_used_letters(lives, list, u_input):     # resta vidas si lo ingresado todavia no se habia ingresado
    subtract_live = True
    for i in list:          # por cada letra incorrecta ingresada antes...
        if u_input == i:    # si lo que ingreso el usuario ya estaba en la lista...
            subtract_live = False   # entonces no hay que restar vidas
    if subtract_live == True:
        return lives-1
    return lives

def chk_lives(lives):
    if lives > 0:
        print("FELICIDADES!!!")
    else:
        print("GAME OVER")


def run():
    file = file_opening("./archivos/data.txt", "r")      # abrimos el archivo data.txt
    words = word_loading(file)     # cargamos las palabras en una lista
    chosen_word = word_picking(words)   # pido una palabra al azar de la lista y la recibo como lista
    final_word = word_ready(chosen_word)    # saca acentos y pone la palabra en mayuscula
    underscores = create_undscs(final_word)     # tengo otra lista que tenga un "_" por cada letra de la palabra
    used_letters_correct = []
    used_letters_incorrect = []
    lives = 10
    os.system("cls")        # limpiamos pantalla
    while underscores != final_word and lives > 0:    # mientras las listas sean distintas, mostrar la lista a medida que se va completando
        print("- Ahorcado! -")
        print(" ".join(underscores), "\n")
        print("Vidas: ", lives)
        print("Letras correctas usadas: ", ", ".join(used_letters_correct))
        print("Letras incorrectas usadas: ", ", ".join(used_letters_incorrect))
        try:
            user_input = str(input("Ingrese una letra: ")).upper()
        ############################################################
            if user_input<"A" or user_input>"Z" and user_input != "Ñ":
                raise TypeError("Solo letras de la A a la Z.")
        except TypeError as TE:
            print(TE)
            time.sleep(2)
        ############################################################
        else:
            change = replace(final_word, underscores, user_input)
            if change != True:
                lives = chk_used_letters(lives, used_letters_incorrect, user_input)     # obtiene las vidas correspondientes segun la lista de incorrectas
                used_letters_incorrect.append(user_input)     # va agregando las letras que se usaron
            else:
                used_letters_correct.append(user_input)
        os.system("cls")
    
    chk_lives(lives)    # imprime mensaje segun vidas
    print("La palabra era: ", ("". join(final_word)))
    file.close()


if __name__ == '__main__':
    run()