from django.urls import path

from bookmark.views import *

app_name='bookmark'
urlpatterns = [
    # ex: /bookmark/
    path('', BookmarkLV.as_view(), name ='index'),
    # ex: /bookmark/5/
    path('<int:pk>/',BookmarkDV.as_view(),name='detail'),
]
