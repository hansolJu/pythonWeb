from django.urls import path,include

from bookmark.views import *

urlpatterns = [
    # ex: /bookmark/
    path('', BookmarkLV.as_view(), name = 'index'),
    # ex: /bookmark/5/
    path('<int:pk>/',BookmarkDV.as_view(),name='detail'),
    # ex:
]
