"""
Файл для переопределения команды runserver в Django.

Этот файл содержит класс `Command`, который наследуется от `RunserverCommand` и переопределяет его методы для
добавления аргументов командной строки и обработки команды. Команда позволяет запускать сервер Django с
указанными хостом и портом по умолчанию, если они не были явно указаны в командной строке.

Класс `Command`:
- `add_arguments(self, parser)`: Переопределяет метод для добавления аргументов командной строки.
- `handle(self, *args, **options)`: Переопределяет метод для обработки команды. Проверяет, установлен ли аргумент
  `addrport` (адрес и порт), и если нет, устанавливает его по умолчанию на основе значений `SERVER_HOST` и `SERVER_PORT`.

Пример использования:
Для запуска сервера с хостом и портом по умолчанию:
>>> python src/manage.py runserver

Для запуска сервера с явно указанным хостом и портом:
>>> python src/manage.py runserver 0.0.0.0:8000
"""

from django.core.management.commands.runserver import Command as RunserverCommand
from src.config.settings.server import SERVER_PORT, SERVER_HOST

class Command(RunserverCommand):
    """
    Переопределенная команда runserver для Django.

    Этот класс наследуется от `RunserverCommand` и переопределяет его методы для добавления аргументов командной строки
    и обработки команды. Команда позволяет запускать сервер Django с указанными хостом и портом по умолчанию, если они
    не были явно указаны в командной строке.

    Методы:
        add_arguments(self, parser): Переопределяет метод для добавления аргументов командной строки.
        handle(self, *args, **options): Переопределяет метод для обработки команды. Проверяет, установлен ли аргумент
                                        `addrport` (адрес и порт), и если нет, устанавливает его по умолчанию на основе
                                        значений `SERVER_HOST` и `SERVER_PORT`.
    """
    poetry_command_name = 'start_dev'
    help = 'Starts development server with all necessary services'

    def add_arguments(self, parser):
        """
        Переопределяет метод для добавления аргументов командной строки.

        Аргументы:
            parser: Объект парсера аргументов командной строки.
        """
        super().add_arguments(parser)

    def handle(self, *args, **options):
        """
        Переопределяет метод для обработки команды.

        Проверяет, установлен ли аргумент `addrport` (адрес и порт), и если нет, устанавливает его по умолчанию на
        основе значений `SERVER_HOST` и `SERVER_PORT`.

        Аргументы:
            *args: Дополнительные аргументы, переданные в команду.
            **options: Дополнительные именованные аргументы, переданные в команду.
        """
        if not options['addrport']:
            options['addrport'] = f'{SERVER_HOST}:{SERVER_PORT}'
        
        # Используем родительский метод напрямую вместо call_command
        super().handle(*args, **options)