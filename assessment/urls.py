from django.conf.urls import url
from assessment import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home/$', views.home),
    url(r'^home/add_review_itemPage/$', views.add_review_itemPage),
    url(r'^home/item/(?P<item_name_slug>[\w\-]+)/$', views.add_review_itemPage),
    url(r'^home/add_review_opinionPage/$', views.add_review_opinionPage),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),

]
