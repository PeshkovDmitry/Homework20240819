"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle, traverse_directory.
"""

code_to_write = '''
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
        for name in files:
            path = os.path.join(root, name)
            size += os.path.getsize(path)
    return size


def save_results_to_json(file_list, path):
    with open(path, 'w') as f:
        json.dump(file_list, f, ensure_ascii=True, indent=2)


def save_results_to_csv(file_list, path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        if file_list:
            writer.writerow(file_list[0].keys())
        for file in file_list:
            writer.writerow(file.values())


def save_results_to_pickle(file_list, path):
    with open(path, 'wb') as f:
        pickle.dump(file_list, f)
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)