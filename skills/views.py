from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Skill
from .serializers import SkillSerializer


class ListCreateSkillView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class RetrieveUpdateDestroySkillView(RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
