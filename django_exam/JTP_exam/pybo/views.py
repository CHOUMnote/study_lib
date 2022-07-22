from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import Question

class Root(View):
    def get(self, request):
        return redirect("/pybo/")

def index(request):  
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    #==> render(request, 템플릿, 템플릿으로 보낼 데이터(dict))