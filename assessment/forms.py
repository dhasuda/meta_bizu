from django import forms
from assessment.models import Item, Opinion, UserProfile, SearchText
from django.contrib.auth.models import User


##ADD ITEM
class ItemForm(forms.ModelForm):
    nome = forms.CharField(max_length=128, help_text="nome")
    category = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the forms
    class Meta:
        model = Item
        fields = ('nome',)

#SEARCH ITEM
class ItemSearchForm(forms.ModelForm):
    nome = forms.CharField(max_length=128, help_text="nome")

    # An inline class to provide additional information on the forms
    class Meta:
        model = SearchText
        fields = ('nome',)

class OpinionForm(forms.ModelForm):
    rank = forms.IntegerField(initial=5)
    comentario = forms.CharField(max_length=500, help_text="Comentários")

    class Meta:
        model = Opinion
        fields = ('rank', 'comentario',)
        #exclude = ('Item',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
