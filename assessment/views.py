from django.shortcuts import render
from assessment.forms import OpinionForm, ItemForm
from assessment.models import Item

def home(request):
    return render(request, 'assessment/home.html',)

def search(request):
    return render(request, 'assessment/test.html',)

def add_review_itemPage(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            name = form['name'].value()
            """category = form['category'].value()
            print (name)
            print(category)"""
            #return add_review_opinionPage(request,)
            return add_review_opinionPage(request, name)
        else:
            print (form.erros)

    else:
        form = ItemForm()
    return render(request, 'assessment/add_review_itemPage.html', {'form': form})

"""
def add_review_opinionPage(request, itemName):
    newItem = Item.objects.get_or_create(name=itemName)
    #newItem.save() # Save the Item associated with the Opinion

    # Get the information about the item it refers
    context_dict = {}
    try:
        item = Item.objects.get_or_create(slug=item_name_slug)
        context_dict['item_name'] = item.name
    except Item.DoesNotExist:
        pass

    if request.method == 'POST':
        form = OpinionForm(request.POST)

        if form.is_valid():
            return home(request)
        else:
            print (form.erros)

    else:
        form = OpinionForm()
    return render(request, 'assessment/add_review_opinionPage.html', context_dict, {'form': form})
"""
def add_review_opinionPage(request, name):
    context_dict = {}

    #item = Item.objects.get_or_create(name=name)
    #context_dict['item_name'] = item.name

    form = OpinionForm()
    return render(request, 'assessment/add_review_opinionPage.html', context_dict, {'form': form})
