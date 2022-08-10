from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *


# Create your views here.


# def home(request):  # HttpRequest
#     return HttpResponse("<h1>Страница приложения Home page </h1>")


def index(request, index_id):  # HttpRequest
    return HttpResponse(f"<h1>Страница приложения Index </h1> <h2>{index_id}</h2>")


def categories(request, cat_str):
    return HttpResponse(f"<h1>Страница приложения Categories </h1> <p>{cat_str}</p>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('/')
        # raise Http404()
    return HttpResponse(f"<h1>Архив по годам </h1> <h2>{year}</h2>")


def test_get(request, test_get_str):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Страница приложения Test GET </h1> <p>{test_get_str}</p>")


def test_post(request, test_post_str):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Страница приложения Test GET </h1> <p>{test_post_str}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')


def redirect_301(request, month):
    if int(month) > 9:
        return redirect('re_main', permanent=False)  # Всегда
        # return redirect('/')  # Времено
    return HttpResponse(f"<h1>Архив по месяцам </h1> <h2>{month}</h2>")


# base.html
menu = ['About restaurant', 'Add news', 'Feedback', 'Longin']


def home(request):  # HttpRequest
    posts = Visitor.objects.all()  # Connect to BD
    return render(request, 'restaurant/home.html', {'posts': posts, 'menu': menu, 'title': 'Home page'})


def about_us(request):
    return render(request, 'restaurant/about.html', {'menu': menu, 'title': 'About US'})

