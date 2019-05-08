from django.db import models

# 도장장소 모델
class Quest(models.Model):
    title=models.CharField(max_length=200) # 장소명
    body=models.TextField() # 장소 설명
    pwd=models.TextField() # 비밀번호 
    # 객체이름 title로 보이게 함
    def __str__(self):
        return self.title