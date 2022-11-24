from django.urls import path

from . import views

urlpatterns = [
    path('fish', views.index, name='pages-index'),
    path('new', views.create, name='pages-new')
]

