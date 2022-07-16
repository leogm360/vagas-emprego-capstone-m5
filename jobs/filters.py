from django.db.models import Q

from django_filters.rest_framework import FilterSet, CharFilter, NumberFilter, DateTimeFilter

from .models import Job

"""
PELO QUE VI NA DOC, NÃO É POSSIVEL COLOCAR VARIAS CLASSES DE FILTER
NO PARAMETRO filterset_class, SOMENTE NO PARAMETRO filterset_fields, 
POREM ACREDITO QUE SE VISERMOS TODOS OS FILTERS EM UMA CLASS, FUNCIONARIA,
ACREDITO...

DOC django-filters:
https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#adding-a-filterset-with-filterset-class


FILTROS TODO:

GET /api/jobs/search?issued=oldest
GET /api/jobs/search?type=presential | hybrid | remote
GET /api/jobs/search?vacancies=1
GET /api/jobs/search?subscribers=1
GET /api/jobs/search?salary=3567.29
GET /api/jobs/search?egt=true | elt=true | eql=true
GET /api/jobs/search?location=RJ
GET /api/jobs/search?skills=Django
GET /api/jobs/search?q=’desenvolvedor fullstack junior’ V

"""
# GET /api/jobs/search?q=’desenvolvedor fullstack junior’
class JobsFilter(FilterSet):
    q = CharFilter(
        method="filter_by_text", label="Search By Text", required=True
    )

    issed = DateTimeFilter()

    type = CharFilter()

    vacancies = NumberFilter()

    subscribes = NumberFilter()


    class Meta:
        model = Job
        fields = [
            "q", 
            "issed", 
            "type", 
            "vacancies", 
            "subscribes", 
            "salary", 
            "location", 
            "skills"
            ]

    def filter_by_text(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | 
            Q(description__icontains=value) |
            Q(location__icontains=value) |
            Q(job_type__icontains=value) |
            Q(regimen_type__icontains=value)
        )



