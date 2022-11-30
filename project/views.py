from rest_framework.decorators import permission_classes, action
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Issue
from .serializers import ProjectSerializer, IssueSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from django.db.models import Q, F


User = get_user_model()


@permission_classes((IsAuthenticated,))
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self, request, *args, **kwargs):
        if not self.if_title_exist(self, request.data['title']):
            request.data.update({"creator": request.user.__dict__['id']})
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"error": "Project with same title already exists", "data": None}, status=400)

    def update(self, request, *args, **kwargs):
        if not self.get_queryset().filter(title=request.data['title']).exists():
            return super().update(request, *args, **kwargs)
        else:
            return Response({"error": "Project with same title already exists", "data": None}, status=400)

    def destroy(self, request, *args, **kwargs):
        if Issue.objects.filter(belong_to_id=kwargs['pk']).count() > 0:
            return Response({'error': 'cannot delete the project as it is associated with an issue'})
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['get'], url_path=r'get_by_title')
    def get_project_by_title(self, request):
        title = request.query_params.get('title')
        print(title)
        project = self.get_queryset().filter(title=title).first()
        serializer = self.get_serializer(project)
        return Response(serializer.data)

    def if_title_exist(self, title):
        return self.get_queryset().filter(title=title).exists()
        


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

    @action(detail=False, methods=['get'], url_path=r'get_by_title')
    def get_project_by_title(self, request):
        title = request.query_params.get('title')
        issue = self.get_queryset().filter(title=title).first()
        serializer = self.get_serializer(issue)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
