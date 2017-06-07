from django.shortcuts import render
from assessment.forms import OpinionForm

def home(request):
    return render(request, 'assessment/home.html',)

def search(request):
    return render(request, 'assessment/search.html',)


def add_review(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST)

        if form.is_valid():
            # Save the new Opinion to the database
            form.save(commit=True)
            return home(request)

        else:
            print (form.erros)

    else:
        form = OpinionForm()
    return render(request, 'assessment/add_review.html', {'form': form})

