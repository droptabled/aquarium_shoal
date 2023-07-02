from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='pages-index'),
    path('new', views.new, name='pages-new'),
    path('create', views.create, name='pages-create'),
    path('fish/<int:fish_id>', views.fish, name='pages-fish')
]

