from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatsGallery, name='cats_gallery'),
    path('api/', views.CatsGalleryAPI, name='cats_gallery_api')  
]
