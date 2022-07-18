from django.db.models import Q

from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    NumberFilter,
    DateTimeFilter,
)

from .models import Job


class JobsFilter(FilterSet):
    # GET /api/jobs/search?q=’desenvolvedor fullstack junior’
    q = CharFilter(method="filter_by_text", label="Search By Text")
    # GET /api/jobs/search?issued=oldest
    issued = DateTimeFilter(field_name="issued_at", lookup_expr="gte")
    # GET /api/jobs/search?type=presential | hybrid | remote
    type = CharFilter(field_name="job_type", lookup_expr="iexact")
    # GET /api/jobs/search?vacancies=1
    vacancies = NumberFilter(field_name="vacancies_count", lookup_expr="lte")
    # GET /api/jobs/search?subscribers=1
    subscribes = NumberFilter(field_name="account__id", lookup_expr="icontains")

    """
    GET /api/jobs/search?salary=3567.29
    GET /api/jobs/search?location=RJ
    GET /api/jobs/search?skills=Django
    """

    class Meta:
        model = Job
        fields = [
            "issued_at",
            "job_type",
            "vacancies_count",
            "account",
            "salary",
            "location",
            "skills",
        ]

    def filter_by_text(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value)
            | Q(description__icontains=value)
            | Q(location__icontains=value)
            | Q(job_type__icontains=value)
            | Q(regimen_type__icontains=value)
        )
