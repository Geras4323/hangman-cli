def file_opening():
    file = open("./archivos/data.txt", "r", encoding="utf-8")
    return file

def word_loading(file):
    word_list = []          # va a contener todas las palabras
    for word in file:       # guardar cada palabra en la lista
        word_list.append(str(word))
    return word_list

def run():
    f = file_opening()          # abrimos el archivo data.txt
    words = word_loading(f)     # cargamos las palabras en una lista


if __name__ == '__main__':
    run()