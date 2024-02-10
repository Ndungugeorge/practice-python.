def read_file(filename=""):
    with open(filename, encoding="utf8")as file:
        print(file.read())

read_file("my_file_0.txt")