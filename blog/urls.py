from django.urls import path,re_path

from blog.views import *

app_name='blog'
urlpatterns = [
    # ex: /blog/
    path('', PostLV.as_view(), name = 'index'),

    # ex: /post/
    path('post/',PostLV.as_view(),name='post_list'),

    # ex: /post/django-example/
    # path('post/<slug:slug>/',PostDV.as_view(),name ='post_detail'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name = 'post_detail'),
    # ex: /archive/
    path('archive/',PostAV.as_view(),name='post_archive'),

    #ex: /2012/
    path('<int:year>/',PostYAV.as_view(),name='post_year_archive'),
    # ex: /2012/nov
    path('<int:year>/<int:month>/',PostMAV.as_view(),name='post_month_archive'),
    # ex: /2012/nov/10
    path('<int:year>/<int:month>/<int:day>',PostDAV.as_view(),name='post_day_archive'),

    # ex: /today/
    path('today/',PostTAV.as_view(),name='post_day_archive'),

    # ex: /tag/
    path('tag/',TagTV.as_view(),name='tag_cloud'),
    # path('tag/<tag:tag>',PostTOL.as_view(),name='tagged_object_list'),
    re_path(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(),name='tagged_object_list'),
]
