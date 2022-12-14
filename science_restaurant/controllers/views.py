# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from .utils import *


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
# menu = [{'title': 'About US', 'url_name': 'about_us'},
#         {'title': 'Add news', 'url_name': 'add_news'},
#         {'title': 'Address', 'url_name': 'contact'},
#         {'title': 'Login', 'url_name': 'login'}
#         ]


class VisitorHome(DataMixin, ListView):
    paginate_by = 2  # Elements in page
    model = Visitor
    template_name = 'restaurant/home_class.html'
    context_object_name = 'posts'  # Использовать старый контекст
    # extra_context = {'title': 'Home page'}  # Static title context

    def get_context_data(self, *, object_list=None, **kwargs):  # dynamic title context
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = 'Home page'
        # context['cat_selected'] = 0
        c_def = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        # select_related(key) для загрузки по внешнему ключу foreignkey
        # prefetch_related(key) для загрузки по внешнему ключу many to many field
        return Visitor.objects.filter(is_published=True).select_related('cat')  #


class RestaurantCategory(DataMixin, ListView):
    paginate_by = 2  # Elements in page
    model = Visitor
    template_name = 'restaurant/home_class.html'
    context_object_name = 'posts'  # Использовать старый контекст
    allow_empty = False  # If empy - Error 404

    def get_context_data(self, *, object_list=None, **kwargs):  # dynamic title context
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = 'Category -' + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        # c_def = self.get_user_context(title='Category -' + str(context['posts'][0].cat),
        #                               cat_selected=context['posts'][0].cat_id)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Visitor.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


# def show_category(request, cat_id):
#     # return HttpResponseNotFound(f'<h1> Страница Category {cat_id} </h1>')
#
#     posts = Visitor.objects.filter(cat_id=cat_id)
#     # cats = Category.objects.all()
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         # 'cats': cats,
#         'menu': menu,
#         'title': f'Category {cat_id}',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'restaurant/home_class.html', context=context)


# def home(request):  # HttpRequest
#     posts = Visitor.objects.all()  # Connect to table Visitor in BD
#     # cats = Category.objects.all()  # Connect to table Category in BD
#     home_context = {
#         'posts': posts,
#         # 'cats': cats,
#         'menu': menu,
#         'title': 'Home page',
#         'cat_selected': 0,
#     }
#     return render(request, 'restaurant/home.html', context=home_context)


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
class ShowNews(DataMixin, DetailView):
    model = Visitor
    template_name = 'restaurant/post.html'
    # slug_url_kwarg = 'post_slug'
    slug_url_kwarg = 'news_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):  # dynamic title context
        context = super().get_context_data(**kwargs)
        # context['title'] = context['post']
        # context['menu'] = menu
        c_def = self.get_user_context(title=str('Visitor'))
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# def about_us(request):
#     au_context = {'menu': menu, 'title': 'About US'}
#     return render(request, 'restaurant/about.html', context=au_context)
#     # return HttpResponseNotFound('<h1> Страница About US </h1>')
def about_def(request):
    contact_list = Visitor.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurant/about_def.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


class AboutUs(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'restaurant/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Add news'
        # context['menu'] = menu
        c_def = self.get_user_context(title="About US")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# def login(request):
#     # return HttpResponseNotFound('<h1> Страница LOGIN </h1>')
#     l_context = {'menu': menu, 'title': 'Login'}
#     return render(request, 'restaurant/login.html', context=l_context)


class LogIn(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'restaurant/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Add news'
        # context['menu'] = menu
        c_def = self.get_user_context(title="Login")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AddNews(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'restaurant/add_news.html'
    success_url = reverse_lazy('home')
    # login_url = '/admin/'   # Переход на страницу логина
    login_url = reverse_lazy('login')  # Переход на страницу логина

    def get_context_data(self, *, object_list=None, **kwargs):  # dynamic title context
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Add news'
        # context['menu'] = menu
        c_def = self.get_user_context(title="Добавить новость")
        context = dict(list(context.items()) + list(c_def.items()))
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


# def contact(request):
#     # return HttpResponseNotFound('<h1> Страница CONTACT </h1>')
#     c_context = {'menu': menu, 'title': 'Contacts'}
#     return render(request, 'restaurant/contact.html', context=c_context)
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'restaurant/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class Contact(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'restaurant/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Add news'
        # context['menu'] = menu
        c_def = self.get_user_context(title="Contacts")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# def actors(request):
#     return HttpResponseNotFound('<h1> Страница Актёров </h1>')
#
#
# def billionaires(request):
#     return HttpResponseNotFound('<h1> Страница Миллионеры </h1>')
#
#
# def others(request):
#     return HttpResponseNotFound('<h1> Страница Others </h1>')


class RegisterUser(DataMixin, CreateView):
    # form_class = UserCreationForm
    form_class = RegisterUserForm
    template_name = 'restaurant/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()  # Save in DB
        login(self.request, user)
        return redirect('home')


# class LoginUserForm:
#     pass


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm  # Standart form
    # form_class = LoginUserForm  # Created form
    template_name = 'restaurant/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')












