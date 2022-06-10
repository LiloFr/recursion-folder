import os
import time


def way():
    while True:
        path = str(input("Введите путь до папки:"))
        if os.path.exists(path):
            return path
        else:
            print("Неверный путь")


def dictionary(path):
    res = {}
    for filename in os.listdir(path):
        current_path = os.path.join(path, filename)
        if os.path.isdir(current_path):
            res.update(dictionary(current_path))
        else:
            res.update({current_path: os.path.getsize(current_path)})
    return res


def duplicate(a: dict):
    keys = list(a.keys())
    copies = {}
    for key_ind1 in range(len(keys) - 1):
        key1 = keys[key_ind1]
        result_key = (a[key1], key1)
        for key_ind2 in range(key_ind1 + 1, len(keys)):
            key2 = keys[key_ind2]
            if os.path.basename(key1) == os.path.basename(key2) and a[key1] == a[key2]:
                if result_key not in copies:
                    copies[result_key] = []
                copies[result_key].append(key2)
        if result_key in copies:
            yield result_key, copies[result_key]


def my_print(x):
    for key, value in x:
        print((key[0], key[1]), *value, sep='\n')
        print()


if __name__ == '__main__':
    p = way()
    s = dictionary(p)
    print('Обход папок завершен')
    time.sleep(1)
    print('Вывод файлов:')
    time.sleep(2)
    r = duplicate(s)
    my_print(r)
    print('Вывод файлов завершен')
