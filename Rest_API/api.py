from .models import project
from rest_framework import viewsets, permissions
from .serializers import project_serializers

class project_view_set(viewsets.ModelViewSet):
    queryset = project.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = project_serializers
    