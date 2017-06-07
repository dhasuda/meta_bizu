from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.contrib.auth.models import User


""" It has a name (i.e.: Yano) and a category (i.e.: professor) """
class Item(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.IntegerField(default=0) # Each number is a category; 0 is no category
    s = models.SlugField(max_length=128, editable=False)

    def save(self):
        if not self.id:
            self.s = slugify(self.name)
        super(Item, self).save()

class SearchText(models.Model):
    name = models.CharField(max_length=128)

""" It has a rank and some text and other stuff """
""" precisa estar relacionado com um objeto """
class Opinion(models.Model):
    item = models.ForeignKey(Item)
    rank = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=500)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
