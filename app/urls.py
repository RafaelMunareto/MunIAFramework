from django.urls import path
from .views import home

urlpatterns = [
    path('', home.index, name='index'),
    path('processar-base/', home.processarBase, name='processar_base'),
    path('rodar-modelos/', home.rodarModelos, name='rodar-modelos'),
    path('maquina-comites/', home.maquinaComites, name='maquina-comites'),
    path('previsao/', home.previsao, name='previsao'),
    path('score/', home.score, name='score'),
    path('base-utilizacao/', home.processarBaseUtilizacao, name='base-utilizacao'),
    path('rodar-tudo/', home.rodarTudo, name='rodar-tudo'),
    path('upload/', home.upload_file, name='upload'),
    path('rename_file/<str:file_name>/', home.rename_file, name='rename_file'),
    path('delete_file/<str:file_name>/', home.excluir_arquivo, name='delete_file'),

]
