"""first_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from news.views import index, detail_view, create_view, edit_view, delete_view, commentary_view, likes_view

from profiles.views import logout_view, login_view, register_view, detail_user_view

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout_view),
    path("login/", login_view),
    path('register/', register_view),
    # path('news/<int:pk>/', detail_view, 'detail-view'),
    path('news/<int:pk>/', detail_view, name='detail-view'),
    path('news/create/', create_view),
    path('news/edit/<int:pk>/', edit_view),
    path('news/delete/<int:pk>/', delete_view),
    path('news/commentary/<int:pk>/', commentary_view),
    path('news/like/<int:pk>/', likes_view),
    path('profile/<int:pk>/', detail_user_view, name='profile'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
