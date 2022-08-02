from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import Question,Answer
from django.views.decorators.csrf import csrf_exempt

class Root(View):
    def get(self, request):
        return redirect("/pybo/")

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
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