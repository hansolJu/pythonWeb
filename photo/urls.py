from django.urls import path
from photo.views import *

app_name='photo'
urlpatterns = [

    # ex: /
    path('', AlbumLV.as_view(),name='index'),

    # ex: /album/, same as /
    path('album/',AlbumLV.as_view(),name='album_list'),
    # ex: /album/99/
    path('album/<int:pk>/',AlbumDV.as_view(),name='album_detail'),

    # album CRUD
    # ex: /album/add/
    path('album/add/',AlbumPhotoCV.as_view(),name = 'album_add'),
    # ex: /album/change/
    path('album/change',AlbumChangeLV.as_view(),name='album_change'),
    # ex: /album/99/update/
    path('album/<int:pk>/update/',AlbumPhotoUV.as_view(),name='album_update'),
    # ex: /album/99/delete/
    path('album/<int:pk>/update/', AlbumDeleteView.as_view(), name='album_delete'),

    # photo CRUD
    # ex: /photo/add
    path('photo/add/', PhotoCreateView.as_view(),name='photo_add'),
    # ex: /photo/change
    path('photo/change/', PhotoChangeLV.as_view(),name='photo_change'),
    # ex: /photo/99/update
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(),name='photo_update'),
    # ex: /photo/99/delete
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(),name='photo_delete'),

    # ex: /photo/99/
    path('photo/<int:pk>/',PhotoDV.as_view(),name='photo_detail'),

]