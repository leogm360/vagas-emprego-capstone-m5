from django.urls import path

from .views import ListCreateSkillView, RetrieveUpdateDestroySkillView

urlpatterns = [
    path("skills/", ListCreateSkillView.as_view()),
    path("skills/<int:pk>/", RetrieveUpdateDestroySkillView.as_view()),
]
