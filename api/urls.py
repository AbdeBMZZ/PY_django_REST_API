from django.urls import path
from . import views

urlpatterns = [
    path('etudiants/', views.EtudiantList.as_view()),
    path('etudiants/<str:cne>', views.EtudiantDetail.as_view())
]
