import os


def obhodFiles(path, level=1):
    print("Level=", level, "Content:", os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print("Спускаємось", path + '\\' + i)
            obhodFiles(path + '\\' + i, level + 1)
            print("Повертаємось", path)


path = "D:\\image"

obhodFiles(path)
