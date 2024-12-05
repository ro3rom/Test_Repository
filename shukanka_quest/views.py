from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.contrib.auth.models import User

# habit_list ビュー
def habit_list(request):
    # 必要なデータをテンプレートに渡す
    return render(request, 'habit_list.html')  # habit_list.htmlのテンプレートを表示

# ユーザー登録ビュー
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # パスワード確認
        if password != password_confirm:
            return render(request, 'registration/register.html', {'error': 'パスワードが一致しません'})

        # ユーザー作成
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # 自動的にログインさせる
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

        return redirect('home')  # ログイン後、ホーム画面にリダイレクト

    return render(request, 'registration/register.html')

# ホームページビュー
def home(request):
    return render(request, 'home.html')  # home.htmlというテンプレートを表示

# ログインビュー
def login_view(request):
    if request.method == 'POST':
        # フォームが送信された場合、ユーザー名とパスワードで認証を行う
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # ユーザーをログインさせる
            return redirect('home')  # ログイン後、ホームページにリダイレクト
        else:
            return render(request, 'login.html', {'error': '無効なユーザー名またはパスワードです。'})
    else:
        return render(request, 'login.html')  # GETリクエストの場合はログインフォームを表示

# 習慣追加ビュー
def add_habit(request):
    return render(request, 'add_habit.html')  # add_habit.htmlのテンプレートを表示

def index(request):
    # トップページを表示するためのビュー
    return render(request, 'index.html')  # index.htmlというテンプレートを表示
