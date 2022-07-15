from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from .models import Skill


class SkillTextFilter(FilterSet):
    q = CharFilter(
        method="filter_by_text", label="Search By Text", required=True
    )

    class Meta:
        model = Skill
        fields = ["q"]

    def filter_by_text(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(description__icontains=value)
        )
