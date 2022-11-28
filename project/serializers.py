from rest_framework import serializers
from .models import Project, Issue


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'issues', 'creator']
        optional_fields = ('creator',)
        read_only_fields = ('issues',)


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'desc', 'belong_to', 'reporter', 'assignee']
        write_once_fields = ('reporter')
        required_fields=('belong_to')

