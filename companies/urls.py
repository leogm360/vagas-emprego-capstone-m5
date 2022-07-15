from django.urls import path

from . import views

urlpatterns = [
    path("companies/jobs/", views.ListJobView().as_view()),
    path("companies/jobs/register/", views.CreateJobView().as_view()),
    path("companies/jobs/<int:pk>/", views.DetailJobView().as_view()),

    path("companies/", views.CompanyView().as_view()),
    path("companies/register/", views.CompanyView().as_view()),
    path("companies/<str:pk>/", views.DetailCompanyView().as_view()),
]
