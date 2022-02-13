import sys
from core import create_file, create_folder, get_list, delete_file, save_info, copy_file, change_dir

save_info('Старт')
try:
    command = sys.argv[1]
except IndexError:
    print('Необходмо ввести команду, для помощи введите "help"')
else:

    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Вы не ввели имя папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо указать имя файла или папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('не введены названия файлов/папки')
        else:
            copy_file(name, new_name)
    elif command == 'change_dir':
        # TODO проработать исключения неверного пути -FileNotFoundError:
        try:
            path = sys.argv[2]
        except IndexError:
            print('Эх, ты, простофиля, не указал новый путь!!!')
        else:
            change_dir(path)

    elif command == 'help':
        print('помощь')
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла/папки')
    print('copy - копирование файла/папки')

# TODO Добавить возможность развлечения в процессе работы с менеджером.
# Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.

save_info('окончание')
