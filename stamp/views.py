from django.shortcuts import render, get_object_or_404,redirect # 404, redirect
from .models import Quest # Quest모델 import
# stamp 판이 나오는 페이지
def home(request):
    
    #혜영: 확인용
    photo=request.session.get('photo')
    game=request.session.get('game')
    bangbang=request.session.get('bangbang')
    viking=request.session.get('viking')
    popcorn=request.session.get('popcorn')

    finishbtn=request.session.get('finishbtn')
    
    return render(request,'stamp.html', {
                                                'photo':photo,
                                                'game':game,
                                                'bangbang':bangbang,
                                                'viking':viking,
                                                'popcorn':popcorn, 
                                                
                                                'finishbtn':finishbtn,
                                                })
def quest1(request):
    #quest_id=get_object_or_404(Quest,pk=quest_id)
    return render(request,'q1.html') 
def quest2(request):
    #quest_id=get_object_or_404(Quest,pk=quest_id)
    return render(request,'q2.html') 
def quest3(request):
    #quest_id=get_object_or_404(Quest,pk=quest_id)
    return render(request,'q3.html') 
def quest4(request):
    #quest_id=get_object_or_404(Quest,pk=quest_id)
    return render(request,'q4.html') 
def quest5(request):
    #quest_id=get_object_or_404(Quest,pk=quest_id)
    return render(request,'q5.html')     

def clear(request):
    finishbtn=request.GET['goinit']
    if finishbtn=="goinit":
        request.session['finishbtn']="goinit"
    return redirect('/stamp')

    return redirect('/stamp')
# 비밀번호가 맞는 지 처리하고 세션 설정을 할 함수
def check(request):
    # form에서 사용자가 입력한 내용 받아옴
    user_pwd=request.GET['pwd']
    spotNum=request.GET['spot_num'] 

    # 혜영: if-elif spotNum 찾기. 각 비밀번호 맞으면세션 저장
    if spotNum == "1":
        print("1")
        if user_pwd == "lionking":
            print("ok")
            request.session['photo'] = spotNum    
    elif spotNum == "2":
        print("2")
        if user_pwd == "lionking":
            print("ok")
            request.session['game'] = spotNum
    elif spotNum == "3":
        print("3")
        if user_pwd == "lionking":
            print("ok")
            request.session['bangbang'] = spotNum
    elif spotNum == "4":
        print("4")
        if user_pwd == "lionking":
            print("ok")
            request.session['viking'] = spotNum
    elif spotNum == "5":
        print("5")
        if user_pwd == "lionking":
            print("ok")
            request.session['popcorn'] = spotNum

    return redirect('/stamp')
# Create your views here.