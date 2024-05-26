import os

import file_manager as fm


class App:
    def __init__(self):
        with open('base_dir', 'r') as f:
            self.working_directory = f.read()

        if not os.path.isdir(self.working_directory):
            print(f'Указанного в конфигурационном файле каталога ({self.working_directory}) не существует.')
        self.base_dir = self.working_directory

        self.commands = {
            'help': self.help_cmd,
            'files': fm.get_files,
            'move_up': self.move_up_cmd,
            'move': self.move_cmd,
            'del': fm.del_path,
            'create_dir': fm.create_dir,
            'create_file': fm.create_file,
            'read_file': fm.read_file,
            'write_file': fm.write_file,
            'rename': fm.rename,
            'stop': self.stop_cmd
        }

    def move_up_cmd(self):
        if os.path.samefile(self.working_directory, self.base_dir):
            print('Нельзя выйти за пределы изначальной директории')
            return
        self.working_directory = os.path.dirname(self.working_directory)

    def move_cmd(self, dir_):
        new_wd = os.path.join(self.working_directory, dir_)
        if not os.path.isdir(new_wd):
            print(f'Директории {new_wd} не существует')
        self.working_directory = new_wd

    def stop_cmd(self):
        print('Выход из программы')

    def help_cmd(self):
        cmd_list = """
        help - выводит список доступных команд
        files - выводит список файлов и директорий в текущей директории
        move_up - перейти в родительскую директорию
        move {название каталога} - переходит в указанную директорию 
        del {название файла или каталога} - удаляет указанный файл или директорию
        create_dir {название каталога} - создает директорию с заданным названием
        create_file {название файла} - создает файл с заданным названием
        read_file {название файла} - выводит содержимое указанного файла
        write_file {название файла} {text} - записывает текст в указанный файл
        rename {изменяемый файл/директория} {новое название} - переименовывает (перемещает) файл или директорию
        stop - выход из программы
        """
        print(cmd_list)

    def start(self):
        print('Введите help для просмотра доступных команд')
        cmd = ''
        while cmd != 'stop':
            cmd, *args = input(f'{self.working_directory} >>> ').split(' ')
            if cmd not in self.commands.keys():
                print(f'Команды \'{cmd}\' не существует')
                continue
            try:
                if cmd in ['create_dir', 'create_file', 'read_file', 'write_file', 'del']:
                    args = [os.path.join(self.working_directory, ' '.join(args)), ]
                if cmd == 'files':
                    args = [self.working_directory]
                if cmd == 'rename':
                    try:
                        old_name = os.path.join(self.working_directory, args[0])
                        new_name = os.path.join(self.working_directory, args[1])
                        self.commands[cmd](old_name, new_name)

                    except IndexError:
                        print('Некорректно указаны аргументы')
                    continue
                out = self.commands[cmd](*args)
                if out:
                    print(out)

            except TypeError:
                print('Некорректно указаны аргументы')
            except ValueError as e:
                print(e)
            except PermissionError as e:
                print(f'Невозможно получить доступ к файлу/директории')
