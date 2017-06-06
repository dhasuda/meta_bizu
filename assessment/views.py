from django.shortcuts import render

def home(request):
    return render(request, 'assessment/home.html',)

def search(request):
    return render(request, 'assessment/home.html',)
