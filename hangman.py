import random


def file_opening():
    file = open("./archivos/data.txt", "r", encoding="utf-8")
    return file

def word_loading(file):
    word_list = []          # va a contener todas las palabras
    for word in file:       # guardar cada palabra en la lista
        word_list.append(str(word))
    return word_list

def word_picking(word_list):
    rand_word = random.choice(word_list)        # agarra una palabra de la lista al azar
    word = [w for w in rand_word if w != "\n"]  # crea una lista con rand_word sin "\n"
    return word                                 # devuelve la palabra en formato de lista


def run():
    f = file_opening()          # abrimos el archivo data.txt
    words = word_loading(f)     # cargamos las palabras en una lista
    chosen_word = word_picking(words)   # pido una palabra al azar de la lista y la recibo como lista


if __name__ == '__main__':
    run()