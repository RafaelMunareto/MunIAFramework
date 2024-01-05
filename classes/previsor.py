import pandas as pd
import pickle
import constantes 
import json

class Previsor:
    def __init__(self):
        self.modelo = None
        self.X = None

    def retornaResultado():
        with open(f'{constantes.algoritmos_dir}/{constantes.resultado_completo_df}', 'rb') as file:
            resultados_formatados = pickle.load(file)
        print(json.dumps(resultados_formatados, indent=4))

    def carregarModelo(self):
        self.retornaResultado()
        print("\nEscolha uma opção:")
        print("BM - Best Model")
        print("NB - Naive Bayes")
        print("ET - ExtraTrees")
        print("LR - Logistic Regression")
        print("KNN - KNeighbors")
        print("SGD - SGDClassifier")
        print("GD - GradientBoosting")
        print("AB - AdaBoost")
        print("DT - DecisionTree")
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
        elif modelo == 'sgd':
            return constantes.sgd
        elif modelo == 'gb':
            return constantes.gb
        elif modelo == 'ab':
            return constantes.ab
        elif modelo == 'dt':
            return constantes.dt
        elif modelo == 'rf':
            return constantes.rf
        elif modelo == 's':
            self.carregarModelo(self)
        else: 
            self.carregarModelo(self)
        self.modeloEscolhido(modelo)

        with open(modelo + '.pickle', 'rb') as file:
            self.modelo = pickle.load(file)
        print("Modelo Carregado")
        
    def prever(self, X):
        if self.modelo is None:
            raise ValueError("Nenhum modelo foi carregado.")
        return self.modelo.predict(X)

    def preverProba(self, X):
        """Calcula os scores das predições e retorna os resultados."""
        if self.modelo is None:
            raise ValueError("Nenhum modelo foi carregado.")
        print("Criação do Score conc'luída")
        return self.modelo.predict_proba(X)[:, 1]

    def adicionarPredicoesAoDataFrame(self, df, X):
        """Adiciona colunas de predições e scores ao DataFrame fornecido."""
        df[constantes.predicao] = self.prever(X)
        df[constantes.score] = self.preverProba(X)
        print("Criação do Score concluída")
        print(df)
        self.salvarDataFrame(df)
        return df
    
    def salvarDataFrame(df):
        nome = input('Qual o nome para o resultado? ')
        with open(constantes.resultado_dir + nome, 'wb') as file:
            pickle.dump(pd.DataFrame(df), file)
        print("DF salvo com score e predict")
        
        
    def modeloEscolhido(modelo):
        if modelo == 'nb':
            return constantes.nb
        elif modelo == 'et':
            return constantes.et
        elif modelo == 'lr':
            return constantes.lr
        elif modelo == 'knn':
            return constantes.knn
        elif modelo == 'sgd':
            return constantes.sgd
        elif modelo == 'gb':
            return constantes.gb
        elif modelo == 'ab':
            return constantes.ab
        elif modelo == 'dt':
            return constantes.dt
        elif modelo == 'rf':
            return constantes.rf
    