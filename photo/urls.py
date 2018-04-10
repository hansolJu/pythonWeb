from django.urls import path
from photo.views import *

urlpatterns = {

    # ex: /
    path('', AlbumLV.as_view(),name='index'),

    # ex: /album/, same as /
    path('album/',AlbumLV.as_view(),name='album_list'),
    # ex: /album/99/
    path('album/<int:pk>/',AlbumDV.as_view(),name='album_detail'),
    # ex: /photo/99/
    path('photo/<int:pk>/',PhotoDV.as_view(),name='photo_detail'),
}