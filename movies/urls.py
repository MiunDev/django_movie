from django.urls import path
from . import views

urlpatterns = [
    path("", views.MovieView.as_view()),  # главная страница
    # запрашиваем целое число в строке запроса
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review")
]
