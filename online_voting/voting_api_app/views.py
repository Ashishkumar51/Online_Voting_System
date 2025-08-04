from rest_framework import viewsets
from .models import Election, Candidate, Voter, Vote
from .serializers import ElectionSerializer, CandidateSerializer, VoterSerializer, VoteSerializer

class ElectionViewSet(viewsets.ModelViewSet):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
