from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
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


class VisitorHome(ListView):
    model = Visitor
    template_name = 'restaurant/home_class.html'
    context_object_name = 'posts'  # Использовать старый контекст
    # extra_context = {'title': 'Home page'}  # Static title context

    def get_context_data(self, *, object_list=None, **kwargs):  # dynamic title context
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Home page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Visitor.objects.filter(is_published=True)


class RestaurantCategory(ListView):
    model = Visitor
    template_name = 'restaurant/home_class.html'
    context_object_name = 'posts'  # Использовать старый контекст
    allow_empty = False  # If empy - Error 404

    def get_context_data(self, *, object_list=None, **kwargs):  # dynamic title context
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Category -' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Visitor.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


def show_category(request, cat_id):
    # return HttpResponseNotFound(f'<h1> Страница Category {cat_id} </h1>')

    posts = Visitor.objects.filter(cat_id=cat_id)
    # cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': f'Category {cat_id}',
        'cat_selected': cat_id,
    }

    return render(request, 'restaurant/home.html', context=context)


def home(request):  # HttpRequest
    posts = Visitor.objects.all()  # Connect to table Visitor in BD
    # cats = Category.objects.all()  # Connect to table Category in BD
    home_context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Home page',
        'cat_selected': 0,
    }
    return render(request, 'restaurant/home.html', context=home_context)


# def show_news(request, post_slug):
#     # return HttpResponseNotFound(f'<h1> Страница NEWS id = {news_id} </h1>')
#     post = get_object_or_404(Visitor, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.about,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'restaurant/post.html', context=context)
class ShowNews(DetailView):
    model = Visitor
    template_name = 'restaurant/post.html'
    # slug_url_kwarg = 'post_slug'
    slug_url_kwarg = 'news_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):  # dynamic title context
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


def about_us(request):
    au_context = {'menu': menu, 'title': 'About US'}
    return render(request, 'restaurant/about.html', context=au_context)
    # return HttpResponseNotFound('<h1> Страница About US </h1>')


class AddNews(CreateView):
    form_class = AddPostForm
    template_name = 'restaurant/add_news.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):  # dynamic title context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add news'
        context['menu'] = menu
        return context

# def add_news(request):
#     # an_context = {'menu': menu, 'title': 'Add news'}
#     # return render(request, 'restaurant/add_news.html', context=an_context)
#     # return HttpResponseNotFound('<h1> Страница  ADD NEW </h1>')
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#             # print(form.cleaned_data)
#             # try:
#                 # Visitor.objects.create(**form.cleaned_data)
#             #     form.save()
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'restaurant/add_news.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    # return HttpResponseNotFound('<h1> Страница CONTACT </h1>')
    c_context = {'menu': menu, 'title': 'Contacts'}
    return render(request, 'restaurant/contact.html', context=c_context)


def login(request):
    # return HttpResponseNotFound('<h1> Страница LOGIN </h1>')
    l_context = {'menu': menu, 'title': 'Login'}
    return render(request, 'restaurant/login.html', context=l_context)


def actors(request):
    return HttpResponseNotFound('<h1> Страница Актёров </h1>')


def billionaires(request):
    return HttpResponseNotFound('<h1> Страница Миллионеры </h1>')


def others(request):
    return HttpResponseNotFound('<h1> Страница Others </h1>')






