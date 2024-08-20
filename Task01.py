"""
Ваша задача - написать программу, которая принимает на вход директорию
и рекурсивно обходит эту директорию и все вложенные директории.
Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
Каждый результат должен содержать следующую информацию:

Путь к файлу или директории:
Абсолютный путь к файлу или директории.
Тип объекта: Это файл или директория.
Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
Для файлов сохраните их размер в байтах.
Для директорий, помимо их размера, учтите размер всех файлов и директорий,
находящихся внутри данной директории, и вложенных директорий.

Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.

Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle.
Форматы файлов должны быть выбираемыми.

Для обхода файловой системы вы можете использовать модуль os.
Вам необходимо написать функцию traverse_directory(directory),
которая будет выполнять обход директории и возвращать результаты в виде списка словарей.
После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle)
с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.

Файлы добавляются в список results в том порядке,
в котором они встречаются при рекурсивном обходе директорий.
При этом сначала добавляются файлы, а затем директории.

Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)),
и затем получается размер файла (size = os.path.getsize(path)).
Информация о файле добавляется в список results в виде словаря
{'Path': path, 'Type': 'File', 'Size': size}.

Затем, для каждой директории (name в dirs),
также создается полный путь к директории (path = os.path.join(root, name)),
и вызывается функция get_dir_size(path),
чтобы получить размер всей директории с учетом ее содержимого.
Информация о директории добавляется в список results в виде словаря
{'Path': path, 'Type': 'Directory', 'Size': size}.
"""

import os
import json
import csv
import pickle


def traverse_directory(directory: str) -> list:
    result = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            info = {'Path': path, 'Type': 'File', 'Size': os.path.getsize(path)}
            result.append(info)
        for name in dirs:
            path = os.path.join(root, name)
            info = {'Path': path, 'Type': 'Directory', 'Size': get_dir_size(path)}
            result.append(info)
    return result


def get_dir_size(path: str) -> int:
    size = 0
    for root, dirs, files in os.walk(path):
        # size += os.path.getsize(root)
        for name in files:
            path = os.path.join(root, name)
            size += os.path.getsize(path)
        # for name in dirs:
        #     path = os.path.join(root, name)
        #     size += os.path.getsize(path)
    return size


def save_results_to_json(file_list, path):
    with open(path, 'w') as f:
        json.dump(file_list, f, ensure_ascii=True, indent=2)


def save_results_to_csv(file_list, path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        if file_list:
            writer.writerow(file_list[0].keys())
        for file in file_list:
            writer.writerow(file.values())


def save_results_to_pickle(file_list, path):
    with open(path, 'wb') as f:
        pickle.dump(file_list, f)


directory = "/home/dmitry/PHP"
file_list = traverse_directory(directory)
save_results_to_json(file_list, 'result.json')
save_results_to_csv(file_list, 'result.csv')
save_results_to_pickle(file_list, 'result.pickle')
