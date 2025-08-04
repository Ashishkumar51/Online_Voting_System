from django.db import models
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

class Party(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='party_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    election = models.ForeignKey("Election", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.party.name})"

class Voter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # NOTE: Simple password (no hashing)

    def __str__(self):
        return self.name

class Election(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


class Vote(models.Model):
    voter = models.ForeignKey('Voter', on_delete=models.CASCADE)
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    election = models.ForeignKey('Election', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)  # ✅ Add this if missing

    def __str__(self):
        return f"{self.voter} voted for {self.candidate} in {self.election}"
    
class ElectionResultView(APIView):
    def get(self, request, election_id):
        results = (
            Candidate.objects
            .filter(election_id=election_id)
            .annotate(vote_count=Count('vote'))
            .values('name', 'party__name', 'vote_count')
        )
        return Response(results)
