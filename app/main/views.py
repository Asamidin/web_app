from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('index')


def about(request):
    return HttpResponse('<h3>about</h3>')


def index1(request):
    return HttpResponse('index1')


def index2(request):
    return render(request,'main/index2.html')


def about1(request):
    return render(request,'main/about1 .html')





