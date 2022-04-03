def file_opening():
    file = open("./archivos/data.txt", "r")
    return file

def run():
    f = file_opening()


if __name__ == '__main__':
    run()