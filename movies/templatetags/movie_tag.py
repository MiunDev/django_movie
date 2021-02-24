from django import template
from movies.models import Category, Movie

"""Необходим для отображения категорий в Header на всех страницах"""

register = template.Library()


# регистрация тега
@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count=5):
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies": movies}
