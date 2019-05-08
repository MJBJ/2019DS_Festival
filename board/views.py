from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Board
from .forms import BoardForm
from django.http import HttpResponseRedirect

def show(request):
    boards = Board.objects
    return render(request, 'show.html', {'boards':boards})

def photo(request):
    boards = Board.objects
    return render(request, 'photo.html', {'boards':boards})

def detail(request,board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board':board_detail})

# def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
#     if request.method == 'POST':
#         board = Board()
#         board.title = request.GET['title']
#         board.body = request.GET['body']
#         board.updated_at = timezone.datetime.now()
#         board.pwd = request.GET['pwd']
#         board.save() #객채.delete()도 있다.
#         return redirect('/board/'+str(board.id)) #redirect안에 url을 써줘야함.
#         # board id는 int형. url은 string. 따라서 문자열로 형변환해줌

def boardpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST    
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # 저장하지 않고 모델객체를 반환
            post.updated_at = timezone.now()
            post.save()
            return redirect('show')
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BoardForm()
        return render(request, 'post.html', {'form':form})

def delete(request, board_id):
        board = Board.objects.get(pk=board_id)
        if board.pwd==request.GET['passwd']:
                board.delete()
                return redirect('show')
        else:
                return redirect('show')
