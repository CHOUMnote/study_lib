from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):    #forms.Form-> 일반 폼, 모델폼은 모델과 연결
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성