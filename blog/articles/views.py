from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = Note.objects.all()
    return render(request, 'articles/index.html', {'menu': menu, 'title': 'Главная страница', 'posts': posts})


def about(request):
    return render(request, 'articles/about.html', {'title': 'О сайте'})


def categories(request, catid):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2021:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
