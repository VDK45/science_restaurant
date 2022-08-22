from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home, name='main'),
    path('home/', home, name='home'),
    path('index/<int:index_id>/', index),  # http://127.0.0.1:8000/science_restaurant/index/45
    path('categories/<str:cat_str>/', categories),  # http://127.0.0.1:8000/science_restaurant/categories/a  NOT /
    # path('slug/<slug:cat_slug>/', categories),  # ASCII =  Latin + int
    # path('uuid/<uuid:cat_uuid>/', categories),  # ASCII lower
    # path('path/<path:cat_path>/', categories),  # Any symbol
    # path('regular_expression/<re_path:cat_path>/', categories),  # regular expression
    re_path(r'^archive_y/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/science_restaurant/archive/year/2022
    path('test_get/<str:test_get_str>/', test_get),
    # http://127.0.0.1:8000/science_restaurant/test_get/a/?name=Garik&type=actor
    path('test_post/<str:test_post_str>/', test_post),
    # http://127.0.0.1:8000/science_restaurant/test_get/a/?name=Garik&type=actor
    re_path(r'^archive_m/(?P<month>[0-9])/', redirect_301),
    # http://127.0.0.1:8000/science_restaurant/archive/month/9
    path('about_us/', about_us, name='about_us'),
    path('add_news/', add_news, name='add_news'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('news/<slug:post_slug>/', show_news, name='news'),
    path('actors/', actors, name='actors'),
    path('billionaires/', billionaires, name='billionaires'),
    path('others/', others, name='others'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<int:cat_id>/', show_category, name='category'),

]
