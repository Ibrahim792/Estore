from django.urls import path
from messageapp import views

urlpatterns = [
    path('testing', views.testing),
    path('create', views.create),
    path('dashboard', views.dashboard),
    path('delete/<rid>', views.delete),
    path('edit/<rid>', views.edit),
]
