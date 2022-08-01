from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.Root.as_view(), name="root"),
    path('pybo/', views.index, name="index"),
    path('pybo/<int:id>/', views.detail,name='detail'),
    path('pybo/create/<int:id>/', views.answer_create, name='answer_create')
]
