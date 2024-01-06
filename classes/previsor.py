import pandas as pd
import pickle
import constantes 
from sklearn.preprocessing import StandardScaler
import json

class Previsor:
    def __init__(self):
        self.modelo = None
        self.X = None
        self.df = None
        self.df = None
        self.scaler = None
        self.modelo_escolhido = None
    

    def carregarModelo(self):
        with open(f'{constantes.algoritimos_dir}/{constantes.resultado_completo_df}', 'rb') as file:
            resultados_formatados = pickle.load(file)
        print(json.dumps(resultados_formatados, indent=4))

        self.modelo_escolhido = self.pergunta()
        if self.modelo_escolhido == '':
            self.modelo_escolhido = self.pergunta()
        caminho_modelo = constantes.algoritimos_dir + self.modelo_escolhido + '.pickle'
        print(f"Carregando modelo de {caminho_modelo}")
        with open(caminho_modelo, 'rb') as file:
            self.modelo = pickle.load(file)

        print("Modelo Carregado:")
        print(self.modelo)
            
        with open(constantes.teste_dir + constantes.previsor_utilizado, 'rb') as file:
            self.X = pickle.load(file)

        with open(constantes.teste_dir + constantes.previsores, 'rb') as file:
            self.df = pickle.load(file)
        
        print("Teste Carregado")
        print(json.dumps(self.X.head().to_dict(), indent=4))
        
        self.adicionarPredicoesAoDataFrame()

    def prever(self):
        if self.modelo is None:
            raise ValueError("Nenhum modelo foi carregado.")
        return self.modelo.predict(self.X)

    def preverProba(self):
        if self.modelo is None:
            raise ValueError("Nenhum modelo foi carregado.")
        return self.modelo.predict_proba(self.X)[:, 1]

    def adicionarPredicoesAoDataFrame(self):
        predicoes = self.prever()
        print("\n Primeiras previsões:", predicoes[:10]) 

        if hasattr(self.modelo, 'predict_proba'):
            scores = self.preverProba()
            self.df[constantes.score] = scores
            print("Primeiros scores:", scores[:10])
            print("Score positivo: \n", self.df.query('score > 0')[:10]) 

        self.df[constantes.predicao] = predicoes
        print("\n Predições positivas:  \n", self.df.query('predicao == 1')[:10]) 
        print(constantes.previsor_utilizado)
       
        self.salvarDataFrame(self.df, self.modelo_escolhido)

    @staticmethod
    def salvarDataFrame(X, nome):
        caminho_completo = constantes.resultado_dir + nome
        df2 = pd.DataFrame(X)
        df2.to_csv(caminho_completo + '.csv' )
        print(f"DataFrame salvo com sucesso em {caminho_completo}.csv")
        
    @staticmethod
    def pergunta():
        while True:
            print("\nEscolha uma opção:")
            print("BM - Best Model")
            print("NB - Naive Bayes")
            print("ET - ExtraTrees")
            print("LR - Logistic Regression")
            print("KNN - KNeighbors")
            print("GD - GradientBoosting")
            print("AB - AdaBoost")
            print("RF - RandomForest")
            print("S - Sair")
            modelo = input('Qual o modelo a ser usado ? ' ).lower()
            if modelo == 'nb':
                return constantes.nb
            elif modelo == 'et':
                return constantes.et
            elif modelo == 'lr':
                return constantes.lr
            elif modelo == 'knn':
                return constantes.knn
            elif modelo == 'gd':
                return constantes.gb
            elif modelo == 'ab':
                return constantes.ab
            elif modelo == 'rf':
                return constantes.rf
            elif modelo == 'bm':
                return constantes.bm
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

        
    