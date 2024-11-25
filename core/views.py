# core/views.py

from django.http import HttpResponse
from rest_framework import viewsets
from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer

def home(request):
    return HttpResponse("Welcome to the Campaign System!")

# ViewSet for Agent CRUD operations
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

# ViewSet for Campaign CRUD operations
class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

# ViewSet for CampaignResult CRUD operations
class CampaignResultViewSet(viewsets.ModelViewSet):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
