from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Project, Issue
from .serializers import ProjectSerializer, IssueSerializer
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin

# Create your views here.

class ProjectList(APIView):
    def get(self, request):
        query_set = Project.objects.all()
        serializer = ProjectSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProjectDetails(APIView):
    def get(self, request, id):
        project = get_object_or_404(Project, pk=id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, id):
        project = get_object_or_404(Project, pk=id)
        serializer = ProjectSerializer(project, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def delete(self, request, id):
        project = get_object_or_404(Project, pk=id)
        if project.issue_set.count() > 0:
            return Response({'error': 'cannot delete the project as it is associated with an issue'})
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IssueList(APIView):
    def get(self, request):
        query_set = Issue.objects.select_related('belong_to').all()
        serializer = IssueSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IssueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IssueDetails(APIView):
    def get(self, request, id):
        issue = get_object_or_404(Issue, pk=id)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)

    def put(self, request, id):
        issue = get_object_or_404(Issue, pk=id)
        serializer = IssueSerializer(issue, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def delete(self, request, id):
        issue = get_object_or_404(Issue, pk=id)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
