from django.urls import path, re_path

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

    # ex: /2012/
    re_path(r'^(?P<year>\d{4})/$',PostYAV.as_view(),name='post_year_archive'),
    # ex: /2012/nov
    re_path(r'^(?P<year>\d{4})/$(?P<month>[0-9ㄱ-힣]{1,3})/$',PostMAV.as_view(),name='post_month_archive'),
    # ex: /2012/nov/10
    re_path(r'^(?P<year>\d{4})/$(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$',PostDAV.as_view(),name='post_day_archive'),

    # ex: /today/
    path('today/',PostTAV.as_view(),name='post_day_archive'),

    # ex: /tag/
    path('tag/',TagTV.as_view(),name='tag_cloud'),
    # ex: /tag/tagname/
    # path('tag/<tag:tag>',PostTOL.as_view(),name='tagged_object_list'),
    re_path(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(),name='tagged_object_list'),

    # ex: /search/
    path('search/',SearchFormView.as_view(),name='search'),

    # CRUD
    # ex: /add/
    path('add/',PostCreateView.as_view(),name='add'),
    # ex: /change/
    path('change/',PostChangeLV.as_view(),name='change'),
    # ex: /5/update/
    path('<int:pk>/update/',PostUpdateView.as_view(),name='update'),
    # ex: /5/delete/
    path('<int:pk>/delete/',PostDeleteView.as_view(),name='delete'),

]

