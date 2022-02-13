import os
import shutil
import datetime


# функция для создания файла
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# функция создания папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


# функция просмотра списка файлов и папок
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# функция удаления файлов/папок
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# функция копирования файлов/папок
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


# функция изменения текущей директории
def change_dir(path):
    os.chdir(path)
    print(f'Директория изменена на {os.getcwd()}')



# функция записи работы менеджера в файл
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == "__main__":

    change_dir(r'C:\Users\tatya\OneDrive\Pictures')

