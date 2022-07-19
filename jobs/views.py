from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from .filters import JobsFilter
from .models import Job
from .serializers import JobSearchSerializer


class SearchJobsView(generics.ListAPIView):
    queryset = Job.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    serializer_class = JobSearchSerializer
    filterset_class = JobsFilter
    ordering_fields = "__all__"
