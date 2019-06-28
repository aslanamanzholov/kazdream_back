from rest_framework import viewsets
from . models import Tasks, Tags
from . serializers import TaskSerializer, TagsSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer