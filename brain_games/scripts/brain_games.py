"""Главный модуль программы."""
# !/usr/bin/env python
from ..cli import welcome_user


def main():
    """Главная функция запуска программы."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
