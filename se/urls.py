from django.urls import path

from . import views

urlpatterns = [
   
    path('criar/',  views.criar, name="criar"),
    path('',  views.index, name="index"),
    path('post/', views.post, name='post'),
    path('<int:curso_id>/', views.detail, name='detail'),
    path('excluir/<int:curso_id>/', views.excluir, name='excluir'),
    
]