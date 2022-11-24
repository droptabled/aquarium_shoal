from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='parser-index'),
    path('start', views.create, name='parser-start')
]

