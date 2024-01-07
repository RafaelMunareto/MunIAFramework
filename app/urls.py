from django.urls import path
from .controller import app

urlpatterns = [
    path('', app.index, name='index'),
    path('processar-base/', app.processarBase, name='processar_base'),
    path('rodar-modelos/', app.rodarModelos, name='rodar-modelos'),
    path('maquina-comites/', app.maquinaComites, name='maquina-comites'),
    path('previsao/', app.previsao, name='previsao'),
    path('score/', app.score, name='score'),
    path('base-utilizacao/', app.processarBaseUtilizacao, name='base-utilizacao'),
    path('rodar-tudo/', app.rodarTudo, name='rodar-tudo'),
    path('upload/', app.upload_file, name='upload'),
    path('rename_file/<str:file_name>/', app.rename_file, name='rename_file'),
    path('delete_file/<str:file_name>/', app.excluir_arquivo, name='delete_file'),

]
