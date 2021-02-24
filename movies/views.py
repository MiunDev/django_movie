from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Movie, Category, Actor
from .forms import ReviewForm


class MovieView(ListView):
    """Список фильмов"""

    model = Movie
    # получаем список фильмов, исключая фильмы в черновиках через поле draft
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    """Полное описание фильма"""

    model = Movie
    slug_field = "url"


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)  # запрос в БД для получения объекта с фильмом
        if form.is_valid():
            form = form.save(commit=False)  # приостановка сохранения формы для внесения каких то изменений
            if request.POST.get("parent", None):  # если поле parent (на странице) не пустое
                form.parent_id = int(request.POST.get("parent"))  # то заполняем поле parent у отзыва
            form.movie = movie  # передаем объект Movie из БД для формы
            form.save()  # сохранение данных формы в БД
        return redirect(movie.get_absolute_url())


class ActorView(DetailView):
    """Вывод информации об актере"""
    model = Actor
    template_name = "movies/actor.html"
    slug_field = "name"
