from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Skill
from .serializers import SkillSerializer
from .permissions import IsAdminOrReadOnly


class ListCreateSkillView(ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class RetrieveUpdateDestroySkillView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
