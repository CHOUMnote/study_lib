from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)              #제목
    content = models.TextField()                            #내용
    create_date = models.DateTimeField(auto_now_add=True)   #작성일자
    
    def __str__(self):
        data_set = "\n subject : "+self.subject
        return data_set
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #외래키=질문 , CASCADE delete
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)