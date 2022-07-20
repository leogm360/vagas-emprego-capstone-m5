from copy import deepcopy

from django.db.models import Q
from django_filters.rest_framework import (
    CharFilter,
    DateTimeFilter,
    FilterSet,
    NumberFilter,
)

from .models import Job


class JobsFilter(FilterSet):
    q = CharFilter(method="filter_by_text", label="Search By Text")

    issued_at = CharFilter(
        method="filter_by_issued_at", label="Search By Issued"
    )

    skills = CharFilter(method="filter_by_skills", label="Search By skills")

    vacancies_count_gte = NumberFilter(
        field_name="vacancies_count", lookup_expr="gte"
    )
    vacancies_count_lte = NumberFilter(
        field_name="vacancies_count", lookup_expr="lte"
    )

    subscribers_count_gte = NumberFilter(
        method="filter_by_subscribers_count",
        label="Search By Subscribers Count Gte",
    )
    subscribers_count_lte = NumberFilter(
        method="filter_by_subscribers_count",
        label="Search By Subscribers Count Lte",
    )

    salary_gte = NumberFilter(field_name="salary", lookup_expr="gte")
    salary_lte = NumberFilter(field_name="salary", lookup_expr="lte")

    class Meta:
        model = Job
        fields = [
            "q",
            "issued_at",
            "skills",
            "vacancies_count_gte",
            "vacancies_count_lte",
            "subscribers_count_gte",
            "subscribers_count_lte",
            "salary_gte",
            "salary_lte",
        ]

    def filter_by_text(self, queryset, _, value):
        return queryset.filter(
            Q(title__icontains=value)
            | Q(description__icontains=value)
            | Q(location__icontains=value)
            | Q(job_type__icontains=value)
            | Q(regimen_type__icontains=value)
        )

    def filter_by_issued_at(self, queryset, _, value):
        return queryset.filter(issued_at__icontains=value)

    def filter_by_subscribers_count(self, queryset, name, value):
        filtered_queryset = deepcopy(queryset)

        for job in filtered_queryset:
            matches_reference = False

            if "gte" in name:
                matches_reference = job.account.count() >= value
            else:
                matches_reference = job.account.count() <= value

            if not matches_reference:
                filtered_queryset = filtered_queryset.exclude(id=job.id)

        return filtered_queryset

    def filter_by_skills(self, queryset, _, value):
        filtered_queryset = deepcopy(queryset)

        title_filter = Q(title__icontains=value)
        description_filter = Q(description__icontains=value)

        for job in filtered_queryset:
            matches_reference = job.skills.filter(
                title_filter | description_filter
            ).exists()

            if not matches_reference:
                filtered_queryset = filtered_queryset.exclude(id=job.id)

        return filtered_queryset
