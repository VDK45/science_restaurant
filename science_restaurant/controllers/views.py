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
        # return redirect('main', permanent=False)  # Всегда
        return redirect('main')  # Времено
    return HttpResponse(f"<h1>Архив по месяцам </h1> <h2>{month}</h2>")


# base.html
# menu = ['About restaurant', 'Add news', 'Feedback', 'Longin']
menu = [{'title': 'About US', 'url_name': 'about_us'},
        {'title': 'Add news', 'url_name': 'add_news'},
        {'title': 'Address', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'}
        ]


def home(request):  # HttpRequest
    posts = Visitor.objects.all()  # Connect to BD
    home_context = {
        'posts': posts,
        'menu': menu,
        'title': 'Home page'
    }
    return render(request, 'restaurant/home.html', context=home_context)


def about_us(request):
    au_context = {'menu': menu, 'title': 'About US'}
    return render(request, 'restaurant/about.html', context=au_context)


def add_news(request):
    an_context = {'menu': menu, 'title': 'Add news'}
    # return HttpResponseNotFound('<h1> Страница  ADD NEW </h1>')
    return render(request, 'restaurant/add_news.html', context=an_context)


def contact(request):
    return HttpResponseNotFound('<h1> Страница CONTACT </h1>')


def login(request):
    return HttpResponseNotFound('<h1> Страница LOGIN </h1>')


def show_news(request, news_id):
    return HttpResponseNotFound(f'<h1> Страница NEWS id = {news_id} </h1>')


def food_menu(request):
    return HttpResponseNotFound('<h1> Страница FOOD MENU </h1>')


def games(request):
    return HttpResponseNotFound('<h1> Страница Games </h1>')


def others(request):
    return HttpResponseNotFound('<h1> Страница Others </h1>')


