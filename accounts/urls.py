from django.urls import path

from . import views

urlpatterns = [
    path("accounts/register/", views.RegisterAccountView.as_view()),
    path("accounts/", views.ListAccountsView.as_view()),
    path("accounts/login/", views.LoginAccountsView.as_view()),
    path("accounts/education/", views.ListCreateEducationsView.as_view()),
    path(
        "accounts/education/<pk>/", views.RetrievePatchEducationView.as_view()
    ),
    path(
        "accounts/<int:account_id>/education/",
        views.ListEducationsAccount.as_view(),
    ),
    path("accounts/<pk>/", views.AccountsDetailsView.as_view()),
    path(
        "accounts/<pk>/management/activation/",
        views.ActiveDeactiveAccountView.as_view(),
    ),
    path(
        "accounts/jobs/<int:job_id>/", views.UserRegisterJobView.as_view()
    ),  # CRIAR VIEW PARA ASSOCIAR USER COM A VAGA JOB
]
