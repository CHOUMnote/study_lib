from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

class Root(View):
    def get(self, request):
        return redirect("/pybo/")

def index(request):
    return HttpResponse("dksadjflkjdsalkfjlkaf")
