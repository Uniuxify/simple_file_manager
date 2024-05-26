import os
import pathvalidate


def create_dir(dir_):
    if os.path.isdir(dir_):
        raise ValueError(f'Директория {dir_} уже существует')
    else:
        try:
            os.makedirs(dir_)
        except OSError:
            raise ValueError(f'Некорректное имя директории: {dir_}')


def create_file(fp):
    if os.path.isfile(fp):
        raise ValueError(f'Файл {fp} уже существует')
    file_name = os.path.basename(fp)
    if not pathvalidate.is_valid_filename(file_name):
        raise ValueError(f'Некорректное имя файла: {fp}')
    f = open(fp, 'w')
    f.close()


def del_path(fp):
    if not os.path.exists(fp):
        raise ValueError(f'Файла {fp} не существует')
    os.remove(fp)


def read_file(fp):
    if not os.path.isfile(fp):
        raise ValueError(f'Файла {fp} не существует')
    with open(fp, 'r') as f:
        return f.read()


def write_file(fp, text):
    if not os.path.isfile(fp):
        raise ValueError(f'Файла {fp} не существует')
    with open(fp, 'w') as f:
        f.write(text)


def get_files(dir_):
    if not os.path.isdir(dir_):
        raise ValueError(f'Директории {dir_} не существует')
    return '\n'.join(os.listdir(dir_))
