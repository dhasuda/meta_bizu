from django.shortcuts import render
from assessment.forms import OpinionForm, ItemForm
from assessment.models import Item, Opinion

def home(request):
    return render(request, 'assessment/home.html',)

def search(request):
    return render(request, 'assessment/search.html',)


def add_review_itemPage(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        name = form['name'].value()
        return add_review_opinionPage(request, name)

    else:
        form = ItemForm()
    return render(request, 'assessment/add_review_itemPage.html', {'form': form})

def add_review_opinionPage(request, name):
    global globalVar
    if name:
        globalVar = name
    itemNameUsed = globalVar

    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            print (itemNameUsed)
            item = Item.objects.get(name=itemNameUsed)
            rank = form['rank'].value()
            description = form['description'].value()
            opinion = Opinion(item=item, rank=rank, description=description)
            opinion.save()
            return home(request)

    context_dict = {}
    context_dict['item_name'] = name

    if not Item.objects.filter(name=name).exists():
        item = Item(name=name)
        item.save()


    form = OpinionForm()
    context_dict['form'] = form
    return render(request, 'assessment/add_review_opinionPage.html', context_dict)
