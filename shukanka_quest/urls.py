"""
URL configuration for shukanka_quest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# shukanka_quest/urls.py
from django.contrib import admin
from django.urls import path, include
from shukanka_quest import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('quests/', include('quest_app.urls')),  # quest_appのURL設定をインクルード    path('login/', auth_views.LoginView.as_view(), name='login'),  # ログインページ
    path('', views.home, name='home'),  # ルートURLでhomeビューを表示
    path('register/', views.register, name='register'),  # 'register/' URLに対応するビューを設定
    path('login/', views.login_view, name='login'),  # ログイン画面
    path('habit_list/', views.habit_list, name='habit_list'),  # 新規ページ（習慣一覧）
    path('add-habit/', views.add_habit, name='add_habit'),  # 名前付きパターンを追加
    path('', include('quest_app.urls')), 
]





