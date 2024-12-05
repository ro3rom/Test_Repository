# quest_app/urls.py
from django.urls import path
from . import views  # quest_app 内の views をインポート
from django.contrib.auth import views as auth_views  # ログインビューをインポート

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('habit_list/', views.habit_list, name='habit_list'),  
    path('add_habit/', views.add_habit, name='add_habit'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
]
