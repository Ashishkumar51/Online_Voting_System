from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartyViewSet, ElectionViewSet, VoterViewSet, CandidateViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'parties', PartyViewSet)
router.register(r'elections', ElectionViewSet)
router.register(r'voters', VoterViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
