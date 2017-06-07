from django.shortcuts import render
from assessment.forms import OpinionForm, ItemForm, ItemSearchForm
from assessment.models import Item ,Opinion


def home(request):

    if request.method == 'POST':
        form = ItemSearchForm(request.POST)
        if form.is_valid():
            return search_resultPage(request,form['name'].value())
        else:
            print (form.errors)
    else:
        form = ItemSearchForm()
        return render(request, 'assessment/home.html', {'form':form})

def search_resultPage(request,name):
    context_dict = {}
    context_dict['item_name'] = name
    print("entrou no search")
    if Item.objects.filter(name=name).exists():
        print("Entrou no if")
        return itemPage(request, name)
    else:
        print("Entrou no else")
        return render(request, 'assessment/item_not_foundPage.html', context_dict)


def itemPage(request, name):
    print("Entrou no itemPage")
    context_dict = {}
    item = Item.objects.get(name = name)
    context_dict['item_name'] = item.name
    opinions = Opinion.objects.filter(item = item)
    context_dict['opinions'] = opinions
    context_dict['item'] = item
    return render(request, 'assessment/itemPage.html', context_dict)

def successful_register(request):
    return render(request, 'assessment/successful_register.html',)


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
            return successful_register(request)

    context_dict = {}
    context_dict['item_name'] = name

    if not Item.objects.filter(name=name).exists():
        item = Item(name=name)
        item.save()


    form = OpinionForm()
    context_dict['form'] = form
    return render(request, 'assessment/add_review_opinionPage.html', context_dict)
