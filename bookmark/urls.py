from django.urls import path

from bookmark.views import *

app_name='bookmark'
urlpatterns = [
    # ex: /bookmark/
    path('', BookmarkLV.as_view(), name ='index'),
    # ex: /bookmark/5/
    path('<int:pk>/',BookmarkDV.as_view(),name='detail'),

    #CRUD
    # ex; /add/
    path('add/',BookmarkCreateView.as_view(),name='add'),
    # ex: /99/change/
    path('change/',BookmarkChangeLV.as_view(),name='change'),
    # ex: /5/update/
    path('<int:pk>/update/',BookmarkUpdateView.as_view(),name='update'),
    # ex: /5/delete
    path('<int:pk>/delete/',BookmarkDeleteView.as_view(),name='delete'),

]
