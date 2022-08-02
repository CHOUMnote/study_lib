from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.Root.as_view(), name="root"),
    path('pybo/', views.index, name="home"),
    path('pybo/<int:question_id>/', views.detail, name="detail"),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]
