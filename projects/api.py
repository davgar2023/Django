from .models import Project
from rest_framework import viewsets, permissions
from .serializers import projectSerializer

class projectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = projectSerializer
    permission_classes = [permissions.AllowAny]

