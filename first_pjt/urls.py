"""
URL configuration for first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',  views.index), #path('경로/', 실행) index라는 이정표를 세워 views에 있는 index를 불러옴
    path('', views.root),
    path('hello/', views.hello),
    path('lunch/', views.lunch),
    path('lotto', views.lotto),
    path('username/<name>/', views.username), #<>안에 들어오는 것은 변수처리
    path('cube/<int:number>/', views.cube),
    path('posts/', views.posts),
]
