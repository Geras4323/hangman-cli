def file_opening():
    file = open("./archivos/data.txt", "r", encoding="utf-8")
    return file

def word_loading(file):
    word_list = []
    for word in file:
        word_list.append(str(word))
    return word_list

def run():
    f = file_opening()
    words = word_loading(f)


if __name__ == '__main__':
    run()