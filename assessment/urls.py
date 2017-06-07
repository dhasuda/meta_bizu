from django.conf.urls import url
from assessment import views

urlpatterns = [
    url(r'^$', views.home),

    #TODO: It has to go to the result of the search... how to do that??
    url(r'^search/$', views.search),
    url(r'^add_review_itemPage/$', views.add_review_itemPage),
    url(r'^item/(?P<item_name_slug>[\w\-]+)/$', views.add_review_itemPage),
    url(r'^add_review_opinionPage/$', views.add_review_opinionPage),
]
