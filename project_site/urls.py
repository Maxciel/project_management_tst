from project_site.views import IndexTemplateView , ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

from django.urls import path

app_name = 'projects'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('projetos/', ProjectListView.as_view(), name='lista_projetos'),
    path('projeto/cadastrar', ProjectCreateView.as_view(), name='cadastra_projeto'),
    path('projeto/<pk>', ProjectUpdateView.as_view(), name='atualiza_projeto'),
    path('projeto/excluir/<pk>', ProjectDeleteView.as_view(), name='exclui_projeto'),
]
