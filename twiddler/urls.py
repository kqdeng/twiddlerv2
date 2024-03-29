"""twiddler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# import database_files.views
import items.views
import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('db/', include('database_files.urls')),
    # re_path(r'^files/(?P<name>.+)$', database_files.views.serve_mixed, name='database_file'),
    path('', users.views.index, name="index"),
    path('adduser', users.views.add_user, name="adduser"),
    path('signup', users.views.add_user, name="adduser"),
    path('login', users.views.login_user, name="login"),
    path('verify', users.views.verify, name="verify"),
    path('logout', users.views.logout_user, name="logout"),
    path('home', items.views.home, name="home"),
    path('additem', items.views.add_item, name="additem"),
    path('item/<int:id>', items.views.get_item, name="getitem"),
    path('search', items.views.search, name="search"),
    path('like', items.views.like, name="like"),
]
