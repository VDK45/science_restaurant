from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home, name='re_main'),
    path('home/', home, name='re_main'),
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
    path('about_us', about_us, name='about_us'),

]
