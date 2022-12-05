from rest_framework import serializers
from .models import Project, Issue


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'issues',
                  'creator', 'created_at', 'updated_at']
        optional_fields = ('creator',)
        read_only_fields = ('issues', 'created_at', 'updated_at',)


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'desc', 'belong_to', 'reporter', 'assignee', 'type']
        write_once_fields = ('reporter', 'type')
        required_fields = ('belong_to')
