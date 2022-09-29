from django.urls import path

from . import views

urlpatterns = [
    path('index/',  views.index, name="index"),
    path('cadrastrar/',  views.cadrastrar, name="cadrastrar"),
    path('criar/',  views.criar, name="criar"),
    path('post1/',  views.post1, name="post1"),
  
]