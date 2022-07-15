from django.urls import path

from .views import (
    ListCreateSkillView,
    RetrieveUpdateDestroySkillView,
    SearchSkillView,
)

urlpatterns = [
    path("skills/", ListCreateSkillView.as_view()),
    path("skills/<int:pk>/", RetrieveUpdateDestroySkillView.as_view()),
    path("skills/search/", SearchSkillView.as_view()),
]
