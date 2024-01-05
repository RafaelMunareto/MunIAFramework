import pickle
import pandas as pd
from sklearn.ensemble import VotingClassifier
import constantes
from tqdm import tqdm

class MaquinaDeComites:
    def __init__(self):
        self.resultados = None
        self.previsores = None
        self.alvo = None
        self.modelos = {}

    def carregarResultados(self):
        try:
            with open(f'{constantes.algoritimos_dir}/{constantes.resultado_completo_df}', 'rb') as file:
                self.resultados = pickle.load(file)
            print("Resultado dos algoritmos carregados.")
        except FileNotFoundError:
            print(f"Arquivo {constantes.resultado_completo_df} não encontrado.")
            self.resultados = None

    def carregarModelos(self):
        if not self.resultados or 'resultados' not in self.resultados:
            print("Resultados não disponíveis ou mal formatados.")
            return
        
        for nome in tqdm(self.resultados['resultados'], desc="Carregando modelos", unit="modelo"):
            try:
                with open(f'{constantes.algoritimos_dir}/{nome}_modelo.pickle', 'rb') as file:
                    self.modelos[nome] = pickle.load(file)
            except FileNotFoundError:
                print(f"Modelo {nome} não encontrado.")
                self.modelos[nome] = None
        print("Todos os modelos de treino carregados.")

    def criarComite(self):
        tamanho = int(input('Tamanho Máximo do previsor e alvo? '))
        self.carregarResultados()
        if self.resultados is None:
            print("Não é possível criar o comitê sem resultados.")
            return

        self.carregarModelos()
        if not self.modelos:
            print("Nenhum modelo válido foi carregado. Não é possível criar o comitê.")
            return

        # Carrega os dados de previsores e alvo
        with open(f'{constantes.variaveis_dir}/{constantes.alvo}', 'rb') as file:
            self.alvo = pickle.load(file)
            if tamanho < len(self.alvo):  # Garante que o tamanho solicitado não exceda o comprimento do alvo
                self.alvo = self.alvo[:tamanho]
            else:
                print("Tamanho solicitado excede o comprimento do alvo.")

        with open(f'{constantes.variaveis_dir}/{constantes.previsor_utilizado}', 'rb') as file:
            self.previsores = pickle.load(file)
            if tamanho < len(self.previsores): 
                self.previsores = self.previsores[:tamanho]
            else:
                print("Tamanho solicitado excede o comprimento dos previsores.")

        if isinstance(self.alvo, pd.DataFrame):
            y = self.alvo.iloc[:, 0].values.ravel()
        else:
            y = self.alvo.ravel()
            print(self.alvo)

        # Cria a lista de modelos para o comitê
        modelos_para_comite = []
        for nome, modelo in tqdm(self.modelos.items(), desc="Preparando comitê", unit="modelo"):
            if modelo is not None:
                modelos_para_comite.append((nome, modelo))

        if not modelos_para_comite:
            print("Nenhum modelo válido para formar o comitê.")
            return

        print("Iniciando o treinamento do comitê de algoritmos...")
        voting = VotingClassifier(estimators=modelos_para_comite, voting='soft')
        voting.fit(self.previsores, y)
        print("Criação do comitê de algoritmos concluída.")

        # Salva o modelo de comitê
        with open(f'{constantes.algoritimos_dir}/{constantes.bm}.pickle', 'wb') as file:
            pickle.dump(voting, file)

        return voting
