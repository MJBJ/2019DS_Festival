from django.shortcuts import render

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