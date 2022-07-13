from django.urls import path

from . import views

urlpatterns = [
    path("accounts/register/", views.RegisterAccountView.as_view()),
    path("accounts/", views.ListAccountsView.as_view()),
    path("accounts/login/", views.LoginAccountsView.as_view()),

    path("accounts/education/",views.ListCreateEducationsView.as_view()),
    path("accounts/education/<pk>/",views.RetrievePatchEducationView.as_view()),
    path("accounts/<int:account_id>/education/", views.ListEducationsAccount.as_view()),
    path("accounts/<pk>/", views.AccountsDetailsView.as_view()),
]


"""
POST /api/accounts/register/ - registra um usuário. V

POST /api/accounts/login/ - inicia sessão do usuário. V

GET /api/accounts/ - lista todos os usuários, somente admin.  V


GET /api/accounts/<int:pk>/ - recupera os dados do usuário, somente dono da conta.

PATCH  /api/accounts/<int:pk>/ - atualiza parcialmente os dados do usuário, somente dono da conta.

DELETE /api/accounts/<int:pk>/ - desativa a conta de um usuário, somente dono da conta.


GET /api/accounts/<int:pk>/jobs/ - lista todas as vagas nas quais o candidato se inscreveu, somente dono da conta.

PATCH  /api/accounts/<int:pk>/company/<int:pk>/bind - associa um usuário recrutador a uma empresa, somente usuários recrutadores.

PATCH /api/accounts/<str:email>/recover/ - reativa a conta de um usuário desativado, livre.

PATCH /api/accounts/<pk:int>/management/activation/ - ativa/desativa conta do usuário, somente admin.


"""
