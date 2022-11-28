from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Project, Issue
from .serializers import ProjectSerializer, IssueSerializer
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# class ProjectList(APIView):


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def destroy(self, request, *args, **kwargs):
        if Issue.objects.filter(belong_to_id=kwargs['pk']).count() > 0: 
            return Response({'error': 'cannot delete the project as it is associated with an issue'})
        return super().destroy(request, *args, **kwargs)
    

class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.select_related('belong_to').all()
    serializer_class = IssueSerializer

# class ProjectList(ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# Implement these methods if you have any logic to implement.
    # def get_queryset(self):
    #     return Project.objects.all()

    # def get_serializer_class(self):
    #     return ProjectSerializer

# Normal Implemetation using serializer
    # def get(self, request):
    #     query_set = Project.objects.all()
    #     serializer = ProjectSerializer(query_set, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = ProjectSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ProjectDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

#     def delete(self, request, pk):
#         project = get_object_or_404(Project, pk=pk)
#         if project.issue_set.count() > 0:
#             return Response({'error': 'cannot delete the project as it is associated with an issue'})
#         project.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class IssueList(APIView):




# class IssueList(ListCreateAPIView):
#     queryset = Issue.objects.select_related('belong_to').all()
#     serializer_class = IssueSerializer

    # def get_queryset(self):
    #     return Issue.objects.select_related('belong_to').all()

    # def get_serializer_class(self):
    #     return IssueSerializer

    # def get(self, request):
    #     query_set = Issue.objects.select_related('belong_to').all()
    #     serializer = IssueSerializer(query_set, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = IssueSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class IssueDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Issue.objects.select_related('belong_to').all()
#     serializer_class = IssueSerializer
    # def get(self, request, pk):
    #     issue = get_object_or_404(Issue, pk=pk)
    #     serializer = IssueSerializer(issue)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     issue = get_object_or_404(Issue, pk=pk)
    #     serializer = IssueSerializer(issue, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.data)

    # def delete(self, request, pk):
    #     issue = get_object_or_404(Issue, pk=pk)
    #     issue.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
