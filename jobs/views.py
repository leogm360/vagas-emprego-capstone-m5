from rest_framework import generics

from jobs.models import Job
from jobs.serializers import JobSerializer

class JobView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class DetailJobView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
