from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import Question,Answer
from django.views.decorators.csrf import csrf_exempt
from .forms import QuestionForm
from django.core.paginator import Paginator

class Root(View):
    def get(self, request):
        return redirect("/pybo/")

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page) #10개짜리 해당 페이지 쿼리 변환
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

@csrf_exempt    #csrf 검증 무시
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #question.answer_set.create(content=request.POST.get('content')) #Question - Answer 외래키 의존 -> ~~_set 생성
    answer = Answer(question=question, content=request.POST.get('content'))
    answer.save()
    return redirect('pybo:detail', question_id=question.id)

@csrf_exempt
def question_create(request):
    if request.method == "GET":
        form = QuestionForm()
    
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('pybo:home')
    return render(request, 'pybo/question_form.html', {'form': form})