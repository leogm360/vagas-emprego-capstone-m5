from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .filters import SkillTextFilter
from .models import Skill
from .serializers import SkillSerializer


class ListCreateSkillView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class RetrieveUpdateDestroySkillView(RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SearchSkillView(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SkillTextFilter
