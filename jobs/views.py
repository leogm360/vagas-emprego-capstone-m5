from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics

from .filters import JobsFilter

from .models import Job

from .serializers import JobSerializer

# from .permissions


class SearchJobsView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = JobsFilter
    ordering_fields = "__all__"
