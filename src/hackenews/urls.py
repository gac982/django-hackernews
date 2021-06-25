"""hackenews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.web.views import home, add_news
from app.api.views import NewsViewSet

router = routers.DefaultRouter()
# ruta del api http://127.0.0.1:8000/api/v1/news/
router.register(r'v1/news', NewsViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('add-news', add_news, name='add-news'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
