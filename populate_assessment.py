import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meta_bizu.settings')

from assessment import representations

import django
django.setup()

from assessment.models import Item, Opinion


def populate():
    yano_item = add_item('Yano',representations.itemCategories["PROFESSOR"])

    add_opinion(item=yano_item,
        rank=5,
        description="Super Legal.")

    add_opinion(item=yano_item,
        rank=4,
        description="Legal.")

    add_opinion(item=yano_item,
        rank=3,
        description="Normal.")


    jackson_item = add_item("Jackson",representations.itemCategories["PROFESSOR"])

    add_opinion(item=jackson_item,
        rank=1,
        description="Nada legal.")

    add_opinion(item=jackson_item,
        rank=2,
        description="Não tão legal.")

    # Print out what we have added to the user.
    for c in Item.objects.all():
        for p in Opinion.objects.filter(item=c):
            print( "- {0} - {1}".format(c.name,p.description ))

def add_opinion(item, rank, description):
    opn = Opinion.objects.get_or_create(item=item, rank=rank,description = description)[0]
    opn.save()
    return opn

def add_item(name,category):
    c = Item.objects.get_or_create(name=name,category= category)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print ("Starting Assessment population script...")
    populate()