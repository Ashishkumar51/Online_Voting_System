from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VoterViewSet, CandidateViewSet, ElectionViewSet, VoteViewSet

router = DefaultRouter()
router.register('voters', VoterViewSet)
router.register('candidates', CandidateViewSet)
router.register('elections', ElectionViewSet)
router.register('votes', VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
