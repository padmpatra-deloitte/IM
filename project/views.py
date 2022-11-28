from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Project, Issue
from .serializers import ProjectSerializer, IssueSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model



User = get_user_model()

@permission_classes((IsAuthenticated,))
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self, request, *args, **kwargs):
        request.data.update({"creator": request.user.__dict__['id']})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        if Issue.objects.filter(belong_to_id=kwargs['pk']).count() > 0: 
            return Response({'error': 'cannot delete the project as it is associated with an issue'})
        return super().destroy(request, *args, **kwargs)
    

@permission_classes((IsAuthenticated,))
class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.select_related('belong_to').all()
    serializer_class = IssueSerializer

    def create(self, request, *args, **kwargs):
        request.data.update({"reporter": request.user.__dict__['id']})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
