from django.urls import path

from . import views
from .views import CompanyView

urlpatterns = [
    path("companies/", views.CompanyView().as_view()),
    path("companies/<str:pk>/", views.DetailCompanyView().as_view()),
]
