from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElectionViewSet, CandidateViewSet, VoterViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'elections', ElectionViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'voters', VoterViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
