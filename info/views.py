from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

# d-day
def dday(request):
    return render(request,'Dday.html')

# 메인페이지 
def main(request):
    return render(request,'main.html')

# # 디테일 페이지
def detail(request):
    return render(request,'detail.html')

# # 각 부스별 배치
def map(request):
     return render(request, 'map.html')

# # 총학 게시판
def notice(request):
    return render(request, 'notice.html')

# # 공연 타임테이블
def timetable(request):
     return render(request,'timetable.html')

def develop(request):
     return render(request,'develop.html')

