from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from .models import Task
# Create your views here.


class TaskCreateListApiView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskRetrieveDeleteUpdateApiView(
    generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = "pk"

    def perform_update(self, serializer):
        return super().perform_update(serializer)
    

