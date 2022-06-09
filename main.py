import os
import time


def way():
    while True:
        path = str(input("Введите путь до папки:"))
        if os.path.exists(path):
            return path
        else:
            print("Неверный путь")


def dictionary():
    pass


def duplicate():
    pass


def my_print():
    pass


if __name__ == '__main__':
    pass
