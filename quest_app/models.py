from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Quest(models.Model):
    name = models.CharField(max_length=100)  # クエスト名
    description = models.TextField(blank=True, null=True)  # クエストの説明（任意）

    def __str__(self):
        return self.name

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')  # ユーザーとの関連
    name = models.CharField(max_length=255)  # 習慣名
    description = models.TextField(blank=True, null=True)  # 説明（任意）
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    quest = models.ForeignKey(
        Quest,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='habits'
    )  # クエストとの関連

    def __str__(self):
        return self.name
