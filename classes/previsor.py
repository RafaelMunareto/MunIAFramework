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

        modelo_escolhido = self.pergunta()
        if(modelo_escolhido == ''):
            modelo_escolhido = self.pergunta()
        print(constantes.algoritimos_dir + modelo_escolhido + '.pickle')
        with open(constantes.algoritimos_dir + modelo_escolhido + '.pickle', 'rb') as file:
            self.modelo = pickle.load(file)
        print("Modelo Carregado")
        
        self.X = pd.read_csv(constantes.teste, sep=',')

        if 'Unnamed: 0' in self.X.columns:
            self.X.drop('Unnamed: 0', axis=1, inplace=True)

        print(json.dumps(self.X.head().to_dict(), indent=4)) 
        print("Teste Carregado")
        self.adicionarPredicoesAoDataFrame()

        
    def prever(self):
        if self.modelo is None:
            raise ValueError("Nenhum modelo foi carregado.")
        return self.modelo.predict(self.X.values)  # Convertendo para NumPy array

    def preverProba(self):
        if self.modelo is None:
            raise ValueError("Nenhum modelo foi carregado.")
        print("Criação do Score concluída")
        return self.modelo.predict_proba(self.X.values)[:, 1]

    def adicionarPredicoesAoDataFrame(self):
        """Adiciona colunas de predições e scores ao DataFrame fornecido."""
        predicoes = self.prever()
        scores = self.preverProba()
        self.X[constantes.predicao] = predicoes
        self.X[constantes.score] = scores
        print(json.dumps(self.X.head().to_dict(), indent=4)) 
        self.salvarDataFrame(self.df)
    
    @staticmethod
    def salvarDataFrame(df):
        nome = input('Qual o nome para o resultado? ')
        caminho_completo = constantes.resultado_dir + nome + '.pickle' 
        df2 = pd.DataFrame(df)
        df2.to_csv(caminho_completo)
        with open(caminho_completo, 'wb') as file:
            pickle.dump(df, file)  

        print(f"DataFrame salvo com sucesso em {caminho_completo}")
        
    @staticmethod
    def pergunta():
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
        elif modelo == 'bm':
            return constantes.bm
        
    