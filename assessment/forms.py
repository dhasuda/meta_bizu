from django import forms
from assessment.models import Item, Opinion, SearchText

##ADD ITEM
class ItemForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name")
    category = forms.IntegerField(initial=0)

    # An inline class to provide additional information on the forms
    class Meta:
        model = Item
        fields = ('name',)

#SEARCH ITEM
class ItemSearchForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name")

    # An inline class to provide additional information on the forms
    class Meta:
        model = SearchText
        fields = ('name',)

class OpinionForm(forms.ModelForm):
    rank = forms.IntegerField(initial=5)
    description = forms.CharField(max_length=500, help_text="Comment about it here")

    class Meta:
        model = Opinion
        fields = ('rank', 'description',)
        #exclude = ('Item',)
