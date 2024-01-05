import pandas as pd
import pickle
import constantes 
import json

class Previsor:
    def __init__(self):
        self.modelo = None
        self.X = None
        self.df = None


    def carregarModelo(self):
        with open(f'{constantes.algoritimos_dir}/{constantes.resultado_completo_df}', 'rb') as file:
            resultados_formatados = pickle.load(file)
        print(json.dumps(resultados_formatados, indent=4))
        
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
            self.carregarModelo()
        else: 
            self.carregarModelo()
        self.modeloEscolhido(modelo)
        with open(modelo + '.pickle', 'rb') as file:
            self.modelo = pickle.load(file)
        print("Modelo Carregado")

        with open(constantes.variaveis_dir +  constantes.x, 'rb') as file:
            self.x = pickle.load(file)
        print("Teste Carregado")

        with open(constantes.variaveis_dir + constantes.df, 'rb') as file:
            self.x = pickle.load(file)
        print("DF Carregado")
        self.prever(self)
        
    def prever(self):
        if self.modelo is None:
            raise ValueError("Nenhum modelo foi carregado.")
        self.preverProba()
        return self.modelo.predict(self.x)

    def preverProba(self):
        """Calcula os scores das predições e retorna os resultados."""
        if self.modelo is None:
            raise ValueError("Nenhum modelo foi carregado.")
        print("Criação do Score conc'luída")
        self.adicionarPredicoesAoDataFrame()
        return self.modelo.predict_proba(self.x)[:, 1]

    def adicionarPredicoesAoDataFrame(self):
        """Adiciona colunas de predições e scores ao DataFrame fornecido."""
        self.df[constantes.predicao] = self.prever(self.x)
        self.df[constantes.score] = self.preverProba(self.x)
        print("Criação do Score concluída")
        print(json.dumps(self.df, indent=4))
        self.salvarDataFrame(self.df)
    
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
    