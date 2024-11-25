# core/serializers.py

from rest_framework import serializers
from .models import Agent, Campaign, CampaignResult

# Serializer for Agent model
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

# Serializer for Campaign model
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

# Serializer for CampaignResult model
class CampaignResultSerializer(serializers.ModelSerializer):
    # This will allow us to use 'campaign_id' instead of serializing the full 'Campaign' object
    campaign = serializers.PrimaryKeyRelatedField(queryset=Campaign.objects.all())

    class Meta:
        model = CampaignResult
        fields = '__all__'
