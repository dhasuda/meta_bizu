from django.shortcuts import render
from assessment.models import Item, Opinion

def home(request):
    return render(request, 'assessment/test.html',)

def search(request):
    return render(request, 'assessment/test.html',)

def review(request):
    if request.method == 'POST':
        form = Opinion(request.POST)

        if form.is_valid():
            # Save the new Opinion to the database
            form.save(commit=True)
            return home(request)

        else:
            print (form.erros)

    else:
        form = Opinion()
    return render(request, 'assessment/test.html', {'form': form})
