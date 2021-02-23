from django.apps import AppConfig


class MoviesConfig(AppConfig):
    name = 'movies'
    verbose_name = "Фильмы"  # наименование категории в админке, также смотреть файл __init__.py
