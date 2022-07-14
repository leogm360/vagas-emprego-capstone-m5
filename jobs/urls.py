from django.urls import path

from . import views

urlpatterns = [
    path("jobs/", views.JobView().as_view()),
    path("jobs/<str:pk>/", views.DetailJobView().as_view()),
]
