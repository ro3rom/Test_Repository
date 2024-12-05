# shukanka_quest/models.py

from django.db import models
from django.utils.timezone import now
from django.utils import timezone


class Quest(models.Model):
    title = models.CharField(max_length=100)  # クエスト名
    description = models.TextField()          # クエスト詳細
    points = models.PositiveIntegerField()    # 獲得ポイント
    deadline = models.DateField()             # 期限
    completed = models.BooleanField(default=False)  # 完了状態
    priority = models.IntegerField(default=0)  # 優先度

    class Meta:
        app_label = 'shukanka_quest'  # 明示的にアプリ名を指定

    def __str__(self):
        return self.title


class Habit(models.Model):
    created_at = models.DateTimeField(default=now)  # 適切なdefault値
    def __str__(self):
        return self.name

