"""science_restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from controllers.views import *
from science_restaurant import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('science_restaurant/', include('controllers.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# While DEBUG = False
handler404 = page_not_found  # handler404 == func page_not_found
# handler500  # Ошибка сервнра
# handler403  # Доступ запрещен
# handler400  # Невозможно обработать запрос

