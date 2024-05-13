from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
