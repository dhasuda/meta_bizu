from django.shortcuts import render

def home(request):
    return render(request, 'assessment/test.html',)

def search(request):
    return render(request, 'assessment/test.html',)
