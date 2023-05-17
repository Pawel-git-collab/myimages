from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('original', views.index, name='index'),
    path('display200', views.index1, name='index1'),
    path('display400', views.index2, name='index2'),

]
