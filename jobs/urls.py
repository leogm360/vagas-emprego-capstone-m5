from django.urls import path

from .views import SearchJobsView

urlpatterns = [path("jobs/search/", SearchJobsView.as_view())]
