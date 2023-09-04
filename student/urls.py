from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('ajouter-un-nouveau-etudient/', views.add_student, name='create'),
]
