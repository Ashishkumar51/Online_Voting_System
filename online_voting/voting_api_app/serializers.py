from rest_framework import serializers
from .models import Party, Election, Voter, Candidate, Vote
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'

class VoterSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Voter
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    party = PartySerializer()
    class Meta:
        model = Candidate
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
