from django.urls import path
from . import views

urlpatterns = [
  path('', views.login , name='login'),
  path('dashboard/', views.dahboard, name='dashboard'),
  path('overview/', views.overview, name='overview'),
  path('candidates/', views.candidates, name='candidates'),
  path('parties/', views.parties, name='parties'),
  path('elections/', views.elections, name='elections'),
  path('voters/', views.voters, name='voters'),
  path('vote/', views.vote, name='vote'),
  path('candidates_list/', views.candidates_list, name='candidates_list'),
  path('parties_list/', views.parties_list, name='parties_list'),
  path('elections_list/', views.elections_list, name='elections_list'),
  path('voters_list/', views.voters_list, name='voters_list'),
  path('vote_list/', views.vote_list, name='vote_list'),
  path('result_list/', views.result_list, name='result_list'),
  path('result/', views.result, name='result')
]

