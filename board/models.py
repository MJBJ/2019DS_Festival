from django.db import models

class Board(models.Model):
    file = models.FileField(null=True)
    title = models.CharField(max_length=20, blank=True) # 제목
    body = models.TextField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True) # 현재시각
    pwd = models.CharField(max_length=10, null=False, default="0000") # 비밀번호

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:15]