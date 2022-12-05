from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
# from django.contrib.auth import get_user_model
from .models import Tag
from .serializer import TagSerializer


# Create your views here.
class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def create(self, request, *args, **kwargs):
        tag = self.get_by_title(request.data['title'])
        if tag is None:
            request.data.update({"title": request.data['title'].upper()})
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            # print("tag size : ", tag.size())
            serializer = self.get_serializer(tag)
            return Response({"message": "Tag already exists", "data": serializer.data}, status=200)

    def destroy(self, request, *args, **kwargs):
        tagInstance = Tag.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(tagInstance)
        if (len(serializer.data['tagged_issues']) > 0):
            return Response({'error': 'cannot delete the project as it is associated with an issue'})
        return super().destroy(request, *args, **kwargs)

    def get_by_title(self, title):
        return self.get_queryset().filter(title__iexact=title).first()
