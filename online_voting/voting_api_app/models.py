from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Party(models.Model):
    name = models.CharField(max_length=100, unique=True)
    symbol = models.ImageField(upload_to='party_symbols/', null=True, blank=True)

    def __str__(self):
        return self.name

class Election(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    address = models.TextField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, null=True, blank=True)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    vote_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.party.name if self.party else 'Independent'})"

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voter', 'election')
