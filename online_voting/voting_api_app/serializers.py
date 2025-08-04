from rest_framework import serializers
from .models import Party, Candidate, Voter, Election, Vote

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['id', 'name', 'logo']

class CandidateSerializer(serializers.ModelSerializer):
    party_name = serializers.CharField(source='party.name', read_only=True)
    party_logo = serializers.ImageField(source='party.logo', read_only=True)
    election_title = serializers.CharField(source='election.title', read_only=True)

    class Meta:
        model = Candidate
        fields = ['id', 'name', 'party', 'party_name', 'party_logo', 'election', 'election_title']


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ['id', 'name', 'email', 'password']

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'

# serializers.py


class VoteWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['voter', 'candidate', 'election']

class VoteSerializer(serializers.ModelSerializer):
    voter = serializers.StringRelatedField()
    candidate = serializers.StringRelatedField()
    party = serializers.SerializerMethodField()
    election = serializers.StringRelatedField()
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status = serializers.SerializerMethodField()

    class Meta:
        model = Vote
        fields = ['id', 'voter', 'candidate', 'party', 'election', 'timestamp', 'status']

    def get_party(self, obj):
        return obj.candidate.party.name if obj.candidate and obj.candidate.party else None

    def get_status(self, obj):
        return True  # Or add actual status logic if needed

