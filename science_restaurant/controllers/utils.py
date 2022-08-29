from django.db.models import Count
from .models import *


menu = [{'title': 'About US', 'url_name': 'about_us'},
        {'title': 'Add news', 'url_name': 'add_news'},
        {'title': 'Address', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'}
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = Category.objects.all()
        cats = Category.objects.annotate(Count('visitor'))

        # Если авторизован то нет меню Login
        user_menu = menu.copy()
        if self.request.user.is_authenticated:
            user_menu.pop(3)

        # context['menu'] = menu
        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
