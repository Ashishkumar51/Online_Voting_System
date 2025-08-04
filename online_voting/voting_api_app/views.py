from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Count
from .models import *
from .serializers import *

# --------------------- LOGIN / REGISTER ---------------------
class RegisterView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if Voter.objects.filter(email=email).exists():
            return Response({"msg": "Already registered"}, status=400)
        serializer = VoterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Registered successfully"}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            voter = Voter.objects.get(email=email, password=password)
            return Response({"msg": "Login successful", "voter_id": voter.id})
        except Voter.DoesNotExist:
            return Response({"msg": "Invalid credentials"}, status=401)

# --------------------- CRUD VIEWS ---------------------
class PartyView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # ✅ Required for file uploads

    def get(self, request):
        parties = Party.objects.all()
        serializer = PartySerializer(parties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CandidateView(APIView):
    def get(self, request):
        return Response(CandidateSerializer(Candidate.objects.all(), many=True).data)
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class ElectionView(APIView):
    def get(self, request):
        return Response(ElectionSerializer(Election.objects.all(), many=True).data)
    def post(self, request):
        serializer = ElectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class VoterListView(APIView):
    def get(self, request):
        return Response(VoterSerializer(Voter.objects.all(), many=True).data)
    
class VoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vote.objects.select_related('voter', 'candidate__party').all()
    serializer_class = VoteSerializer

class VoteView(APIView):
    def get(self, request):
        votes = Vote.objects.select_related('voter', 'candidate__party', 'candidate__election').all()
        vote_data = []

        for vote in votes:
            vote_data.append({
                "voter": vote.voter.name,
                "candidate": vote.candidate.name,
                "party": vote.candidate.party.name,
                "election": vote.candidate.election.title,  # fixed this line
            })

        return Response(vote_data)

    def post(self, request):
        voter_id = request.data.get("voter")
        election_id = request.data.get("election")
        candidate_id = request.data.get("candidate")

        # Validate required fields
        if not all([voter_id, election_id, candidate_id]):
            return Response({"error": "voter, election, and candidate fields are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Prevent duplicate vote
        if Vote.objects.filter(voter_id=voter_id, election_id=election_id).exists():
            return Response({"error": "You have already voted in this election."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Save vote
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Vote cast successfully."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DashboardView(APIView):
    def get(self, request):
        elections = ElectionSerializer(Election.objects.all(), many=True).data
        candidates = CandidateSerializer(Candidate.objects.all(), many=True).data
        voters = VoterSerializer(Voter.objects.all(), many=True).data
        votes = VoteSerializer(Vote.objects.all(), many=True).data
        return Response({
            "elections": elections,
            "candidates": candidates,
            "voters": voters,
            "votes": votes
        })

class ResultView(APIView):
    def get(self, request):
        results = []

        # Group by election
        elections = Election.objects.all()
        for election in elections:
            candidates = Candidate.objects.filter(election=election).annotate(
                total_votes=Count('vote')
            ).order_by('-total_votes')

            candidates_data = []
            for candidate in candidates:
                candidates_data.append({
                    "candidate_id": candidate.id,
                    "candidate_name": candidate.name,
                    "party_name": candidate.party.name if candidate.party else None,
                    "party_logo": request.build_absolute_uri(candidate.party.logo.url) if candidate.party.logo else None,
                    "total_votes": candidate.total_votes,
                })

            results.append({
                "election_id": election.id,
                "election_title": election.title,
                "candidates": candidates_data,
                "top_candidate": candidates_data[0] if candidates_data else None
            })

        return Response(results)