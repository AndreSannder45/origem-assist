from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("emergencial/", views.emergencial, name="emergencial"),
    path("tipo/", views.tipo_ocorrencia, name="tipo_ocorrencia"),
    path("questionario/<str:tipo_nome>/", views.questionario, name="questionario"),
    path("resumo/", views.resumo, name="resumo"),
    path("procedimentos/<int:ocorrencia_id>/", views.procedimentos, name="procedimentos"),

    # Fluxo Não Emergencial
    path("nao-emergencial/", views.nao_emergencial, name="nao_emergencial"),
    path("procedimentos-ne/<int:ocorrencia_id>/", views.procedimentos_ne, name="procedimentos_ne"),

    # Histórico de Ocorrências
    path("historico/", views.historico, name="historico"),
]