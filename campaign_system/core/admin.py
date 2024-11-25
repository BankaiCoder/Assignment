# core/admin.py

from django.contrib import admin
from .models import Agent, Campaign, CampaignResult

class CampaignResultAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'phone', 'cost', 'outcome', 'call_duration', 'campaign']  # Display campaign field
    search_fields = ['name', 'phone']  # Make fields searchable
    list_filter = ['outcome', 'campaign']  # Optional: add filtering options

admin.site.register(Agent)
admin.site.register(Campaign)
admin.site.register(CampaignResult, CampaignResultAdmin)  # Registering CampaignResult with the customized admin
