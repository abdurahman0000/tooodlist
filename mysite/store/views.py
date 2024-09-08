from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter
from rest_framework.filters import SearchFilter

class TaslViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['title']




