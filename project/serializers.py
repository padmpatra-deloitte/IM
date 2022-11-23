from rest_framework import serializers
from .models import Project, Issue

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= ['id', 'title']

  
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields= ['id', 'title', 'desc', 'belong_to']
        write_once_fields = ('reporter')
        
