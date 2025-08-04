from django.urls import path
from . import views

urlpatterns = [
  path('', views.login , name='login'),
  path('dashboard/', views.dahboard, name='dashboard'),
  path('form/', views.form, name='form'),
  path('overview/', views.overview, name='overview'),
  
]

