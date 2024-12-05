from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm  # HabitFormは自作のフォームクラス
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        # POSTデータを確認してみる
        print(request.POST)  # POSTデータ全体を出力
        username = request.POST.get('ユーザー名')  # get()を使用
        if not username:
            return HttpResponse("ユーザー名がありません", status=400)
        
        # ユーザー名があれば、ここでユーザー登録処理などを行います。
        return HttpResponse(f"ユーザー名: {username}が登録されました！")

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, '無効なユーザー名またはパスワードです。')
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def index(request):
    if request.user.is_authenticated:
        return redirect('habit_list')  # ログイン済みなら習慣リストページにリダイレクト
    return redirect('register')  # ログインしていなければ新規登録画面にリダイレクト


def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user  # ユーザーを習慣に紐づけ
            habit.save()
            return redirect('habit_list')  # 習慣リストページにリダイレクト
    else:
        form = HabitForm()

    return render(request, 'add_habit.html', {'form': form})

def habit_list(request):
    # ユーザーが作成した習慣を取得（ユーザーがログインしていることを前提）
    habits = Habit.objects.filter(user=request.user)  # ユーザーに紐づく習慣を取得
    return render(request, 'habit_list.html', {'habits': habits})

