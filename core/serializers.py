from rest_framework import serializers
from core.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        #optional_fields = ['id', 'project_name', 'start_date', 'finish_date', 'proj_amount', 'proj_risk', 'proj_team']
