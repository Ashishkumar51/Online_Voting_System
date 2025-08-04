from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),

    path('parties/', PartyView.as_view()),
    path('candidates/', CandidateView.as_view()),
    path('elections/', ElectionView.as_view()),
    path('voters/', VoterListView.as_view()),
    path('api/vote/', VoteView.as_view(), name='vote'),         # POST
    path('api/votes/', VoteListCreateAPIView.as_view(), name='vote-list'),  # ✅ This must match
    path('api/votes/', VoteView.as_view(), name='votes'),  # Supports both GET and POST
    path('votes/', VoteView.as_view(), name='vote-api'),
    path('dashboard/', DashboardView.as_view()),
    path('results/', ResultView.as_view(), name='result-list'),


]
