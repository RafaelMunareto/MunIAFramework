
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.forms import UploadFileForm

from .tratamento_base_utilizacao import TratamentoVariaveisBaseUtilizacao
from .tratamento_variaveis import TratamentoVariaveis
from .looping_algoritimos import LoopingAlgoritmos
from .maquina_comites import MaquinaDeComites
from .previsor import Previsor
from .score_best_model import ScoreBestModel
from django.contrib import messages
import os

def index(request):
    base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'model', 'base')
    files_in_base = os.listdir(base_folder)
    allowed_extensions = ['.pickle', '.txt', '.csv', '.xls']
    filtered_files = [file for file in files_in_base if os.path.splitext(file)[1] in allowed_extensions]
    
    return render(request, 'apps/home/index.html', {'filtered_files': filtered_files})


def rename_file(request, file_name):
    if request.method == 'POST':
        new_file_name = request.POST.get('new_file_name')
        file_extension = request.POST.get('file_extension')
        base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'model', 'base')
        file_path = os.path.join(base_folder, file_name)
        new_file_path = os.path.join(base_folder, f"{new_file_name}.{file_extension}")

        try:
            os.rename(file_path, new_file_path)
            messages.success(request, 'Arquivo renomeado com sucesso.')
        except Exception as e:
            messages.error(request, f'Erro ao renomear arquivo: {str(e)}')

    return redirect('index')  

def excluir_arquivo(request, file_name):
    base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'model', 'base')
    file_path = os.path.join(base_folder, file_name)

    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            messages.success(request,  'Arquivo excluído com sucesso.')
        else:
            messages.error(request, f'Erro ao renomear arquivo: {str(e)}')
            
    except Exception as e:
        messages.error(request, f'Erro ao renomear arquivo: {str(e)}')
    
    return redirect('index')  

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            
            # Obtém a extensão do arquivo original
            file_extension = os.path.splitext(uploaded_file.name)[1]
            
            # Gere um nome único para o arquivo, por exemplo, usando um timestamp
            import time
            timestamp = str(int(time.time()))
            
            # Crie um novo nome de arquivo com a extensão
            new_file_name = f"uploaded_file_{timestamp}{file_extension}"
            
            # Salve o arquivo no servidor com o novo nome
            base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'model', 'base')
            with open(os.path.join(base_folder, new_file_name), 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            messages.success(request, 'Arquivo enviado com sucesso.')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao enviar o arquivo.')
    else:
        form = UploadFileForm()
    return render(request, 'apps/home/upload.html', {'form': form})

def processarBase(request):
    # data_processor = TratamentoVariaveis()
    # data_processor.capturaDados()  
    # data_processor.salvarVariaveis()
    return render(request, 'apps/processar-base.html')
        
def processarBaseUtilizacao(request):
    # data_utilizacao = TratamentoVariaveisBaseUtilizacao()
    # data_utilizacao.capturaDadosUtilizacao()  
    # data_utilizacao.salvarVariaveisBaseUtilizacao()
    return render(request, 'apps/base-utilizacao.html')

def rodarModelos(request):
    # loop = LoopingAlgoritmos()
    # loop.carregarDados()
    # loop.treinarModelos()
    # loop.obterResultados()
    return render(request, 'apps/rodar-modelos.html')

def maquinaComites(request):
    # comites = MaquinaDeComites()
    # comites.criarComite()
    return render(request, 'apps/maquina-comites.html')

def previsao(request):
    # preditor = Previsor()
    # preditor.carregarModelo()
    return render(request, 'apps/previsao.html')

def score(request):     
    # analise = ScoreBestModel()
    # analise.juntarComBestModel()
    return render(request, 'apps/score.html')

def rodarTudo(request):
    # processarBase()
    # rodarModelos()
    # maquinaComites()
    # previsao()
    # score()
    return render(request, 'apps/rodar-tudo.html')

def menu_principal():
    while True:
        print("\nEscolha uma opção:")
        print("P - Processar a base")
        print("M - Rodar modelos")
        print("C - Máquina de comitês")
        print("PR - Propensão")
        print("A - Score")
        print("T - Tudo")
        print("E - Preparar Base para utilização")
        print("S - Sair")
    
        escolha = input("Digite sua escolha? ").lower()
    
        if escolha == "p":
            processarBase()
            pass
        elif escolha == "m":
            rodarModelos()
            pass
        elif escolha == "c":
            maquinaComites()
            pass
        elif escolha == "pr":
            previsao()
            pass
        elif escolha == "a":
            score()
            pass
        elif escolha == "t":
            rodarTudo()
            pass
        elif escolha == "e":
            processarBaseUtilizacao()
        elif escolha == "s":
            print("Saindo do programa.")
            break
        else:
            print("Escolha inválida. Tente novamente.")

#menu_principal()
