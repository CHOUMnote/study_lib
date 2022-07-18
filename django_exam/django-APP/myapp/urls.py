from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),              #root
    path('create/', views.create),      #root/create/ 요청 -> create() 실행 -> 리턴
    path('read/<id>/', views.read),     #read/<id>/ 요청 -> <?> ?에 들어가는 문자를 콜백에 인자로 줄 수 있다. read(rq, ?)
    path('delete/', views.delete),      #root/delete/ 요청 -> delete()
    path('update/<id>/', views.update)  #update/<id>/ 요청 -> update()
]
