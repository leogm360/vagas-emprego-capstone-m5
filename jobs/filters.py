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
    issued = CharFilter(method="filter_by_issued", label="Search By Issued")
    # GET /api/jobs/search?type=presential | hybrid | remote
    type = CharFilter(method="filter_by_type", label="Search By Type")
    # GET /api/jobs/search?skills=Django
    skills = CharFilter(method="filter_by_skills", label="Search By skills")
    # GET /api/jobs/search?location=RJ
    location = CharFilter(method="filter_by_location", label="Search By Location")
    # GET /api/jobs/search?vacancies=1
    vacancies = NumberFilter(field_name="vacancies_count", lookup_expr="lte")
    # GET /api/jobs/search?subscribers=1
    subscribes = NumberFilter(field_name="account__id", lookup_expr="icontains")
    # GET /api/jobs/search?salary=3567.29
    salary_gt = NumberFilter(field_name="salary", lookup_expr="gte")
    salary_lt = NumberFilter(field_name="salary", lookup_expr="lte")
    salary_in = NumberFilter(field_name="salary", lookup_expr="icontains")
   

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
    def filter_by_issued(self, queryset, name, value):
        return queryset.filter(
            Q(issued_at__icontains=value)
        )
    def filter_by_type(self, queryset, name, value):
        return queryset.filter(
            Q(job_type__icontains=value)
        )
    def filter_by_location(self, queryset, name, value):
        return queryset.filter(
            Q(location__icontains=value)
        )
    def filter_by_skills(self, queryset, name, value):
        return queryset.filter(
            Q(skills__icontains=value)
        )
