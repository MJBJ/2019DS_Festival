
from django.db import models


class Board(models.Model):
    file = models.FileField(null=True, blank=True)
    Title = models.CharField(max_length=20, blank=True) # 제목
    Text = models.TextField(max_length=200, blank=True)
    updated_at = models.DateTimeField(auto_now=True) # 현재시각
    pwd = models.CharField(max_length=10, null=False, default="0000") # 비밀번호

    def __str__(self):
        return self.Title

    def summary(self):
        return self.Text[:15]
