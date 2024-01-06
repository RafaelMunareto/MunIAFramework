import pickle
import numpy as np
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from datetime import datetime
import constantes 
from tqdm import tqdm
import json

class LoopingAlgoritmos:
    def __init__(self):
        self.alvo = None
        self.previsores = None
        self.modelos = {}
        self.resultados = {}

    
    def carregarDados(self):
        escolha = input('Qual previsor deseja escolher? Previsor (P), Scanolado (S) ou PCA (PCA)? ').lower()
        if escolha == 'p':
            constantes.previsor_utilizado = constantes.previsores
        elif escolha == 's':
            constantes.previsor_utilizado = constantes.previsores_scalonados
        elif escolha == 'pca':
            constantes.previsor_utilizado = constantes.previsores_pca
        tamanho = int(input('Tamanho Máximo do previsor e alvo? '))
        with open(f'{constantes.variaveis_dir}{constantes.alvo}', 'rb') as file:
            self.alvo = pickle.load(file)
            if tamanho < len(self.alvo): 
                self.alvo = self.alvo[:tamanho]
                constantes.tamanho = tamanho
        with open(f'{constantes.variaveis_dir}{constantes.previsor_utilizado}', 'rb') as file:
            self.previsores = pickle.load(file)
            if tamanho < len(self.previsores):  
                self.previsores = self.previsores[:tamanho]
            
        
    def treinarModelos(self):
        print(f'Previsor utilizado {constantes.previsor_utilizado}')
        inicio_treinamento = datetime.now()
        X_train, X_test, y_train, y_test = train_test_split(
            self.previsores, self.alvo, test_size=0.3, random_state=42
        )

        y_train = y_train.values.ravel()
        print("Número de linhas em X:", X_train.shape[0])
        print("Número de linhas em y:", y_train.shape[0])
        print("\n Terminou a divisão treino e teste \n")
        with open(f'{constantes.variaveis_dir}X_test.pickle', 'wb') as file:
            pickle.dump(X_test, file)
        with open(f'{constantes.variaveis_dir}Y_test.pickle', 'wb') as file:
            pickle.dump(y_test, file)
        with open(f'{constantes.variaveis_dir}X_train.pickle', 'wb') as file:
            pickle.dump(X_train, file)
        with open(f'{constantes.variaveis_dir}Y_train.pickle', 'wb') as file:
            pickle.dump(y_train, file)
        
        algoritmos = {
            constantes.nb: GaussianNB(),
            constantes.et: ExtraTreesClassifier(),
            constantes.lr: LogisticRegression(max_iter=1000),
            constantes.knn: KNeighborsClassifier(),
            constantes.gb: GradientBoostingClassifier(),
            constantes.ab: AdaBoostClassifier(),
            constantes.rf: RandomForestClassifier(),
        }

        resultados = {}

        for nome, modelo in tqdm(algoritmos.items(), desc="Progresso do Treinamento", unit="modelo"):
            cv_scores = cross_val_score(modelo, X_train, y_train, cv=constantes.cv)
            cv_accuracy = np.mean(cv_scores)
            cv_std = np.std(cv_scores)
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            print('\n')
            print(f'Fazendo o algoritimo {nome}...')
            self.modelos[nome] = modelo
            resultados[nome] = {
                "accuracy": acc,
                "cv_accuracy": cv_accuracy,
                "cv_std": cv_std
            }
            
            with open(f'{constantes.algoritimos_dir}{nome}.pickle', 'wb') as file:
                pickle.dump(modelo, file)
                
        fim_treinamento = datetime.now()
        
        resultados_completos = {
            "resultados": resultados,
            "inicio": inicio_treinamento.strftime('%Y-%m-%d %H:%M:%S'),
            "fim": fim_treinamento.strftime('%Y-%m-%d %H:%M:%S')
        }
        print(json.dumps(resultados_completos, indent=4))
        with open(f'{constantes.algoritimos_dir}{constantes.resultado_completo_df}', 'wb') as file:
            pickle.dump(resultados_completos, file)

        self.resultados = resultados_completos

        
    def obterResultados(self):
        return self.resultados
