from django.db import models
from django.contrib.auth.models import User


class Election(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']
        indexes = [
            models.Index(fields=['start_date']),
        ]

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    party = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name='candidates')
    image = models.ImageField(upload_to='candidates/', null=True, blank=True)

    class Meta:
        unique_together = ('name', 'election')
        indexes = [
            models.Index(fields=['election']),
        ]

    def __str__(self):
        return f"{self.name} ({self.party})"


class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    voter_id = models.CharField(max_length=100, unique=True)
    verified = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['voter_id']),
        ]

    def __str__(self):
        return self.user.username


class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voter', 'election')
        indexes = [
            models.Index(fields=['voter']),
            models.Index(fields=['election']),
        ]
