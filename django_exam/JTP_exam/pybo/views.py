from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import Question

class Root(View):
    def get(self, request):
        return redirect("pybo:index")

def index(request):  
    question_list = Question.objects.order_by('-create_date')
    context = {'q_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    #==> render(request, 템플릿, 템플릿으로 보낼 데이터(dict))

def detail(request, id):
    question = get_object_or_404(Question, pk=id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)