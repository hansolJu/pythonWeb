from django.urls import path,include
from django.contrib import admin
from blog.views import *

urlpatterns = [
    # ex: /admin/

    # ex: /blog/
    path('', PostLV.as_view(), name = 'index'),

    # ex: /post/
    path('post/',PostLV.as_view(),name='post_list'),

    # ex: /post/django-example/
    # path('post/(?P<slug>[-\w]+/',PostDV.as_view(),name ='post_detail'),

    # ex: /archive/
    path('archive/',PostAV.as_view(),name='post_archive'),

    #ex: /2012/
    path('<int:pk>/',PostYAV.as_view(),name='post_year_archive'),
    # ex: /2012/nov
    path('<int:pk>/<month:??>/',PostMAV.as_view(),name='post_month_archive'),
    # ex: /2012/nov/10
    path('<int:pk>/<month:??>/<int:pk>',PostDAV.as_view(),name='post_day_archive'),

    # ex: /today/
    path('today/',PostTAV.as_view(),name='post_day_archive'),

]
