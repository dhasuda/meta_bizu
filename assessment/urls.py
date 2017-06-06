from django.conf.urls import url
from assessment import views

urlpatterns = [
    url(r'^review', views.review, name='index'),

    #TODO: It has to go to the result of the search... how to do that??
    url(r'^search', views.search, name='index'), 
]
