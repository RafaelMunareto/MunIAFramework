
from .tratamento_base_utilizacao import TratamentoVariaveisBaseUtilizacao
from .tratamento_variaveis import TratamentoVariaveis
from .looping_algoritimos import LoopingAlgoritmos
from .maquina_comites import MaquinaDeComites
from .previsor import Previsor
from .score_best_model import ScoreBestModel
from django.shortcuts import render

def index(request):
    return render(request, 'apps/index.html')

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
