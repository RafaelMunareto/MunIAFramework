import json
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import constantes 

class ScoreBestModel:
    def __init__(self):
        self.df = None
        self.modelo = None
        self.results = None
        self.bm = None

    def juntarComBesModel(self):
        print('Qual modelo quer juntar com a previsao do BestModel para melhorar o score ?')
        with open(f'{constantes.algoritimos_dir}/{constantes.resultado_completo_df}', 'rb') as file:
            resultados_formatados = pickle.load(file)
        print(json.dumps(resultados_formatados, indent=4))
        self.modelo = self.pergunta()
        try:
            self.results = pd.read_csv(constantes.resultado_dir + self.modelo + '.csv', sep=';')
        except:
            print('Esse modelo não possui resultado')
            self.juntarComBesModel()

        try:
            self.bm = pd.read_csv(constantes.resultado_dir + constantes.bm + '.csv', sep=';')
        except:
            print('BestModel não possui resultado')
            self.juntarComBesModel()
        print("BasesCarregadas")
        self.refazerScoreComBestModel()

    def refazerScoreComBestModel(self):
        # Juntando os DataFrames baseado em um índice comum (ajuste conforme necessário)
        combined_df = pd.merge(self.results, self.bm, on='indice_comum', how='left')

        # Ajustando os scores
        for i, row in combined_df.iterrows():
            # Aumentar o score se o Best Model prever 1 e o score atual for menor que 70%
            if row['predicao_bm'] == 1 and row['score_results'] < 70:
                aumento = row['score_results'] * 0.10  # 10% do score atual
                combined_df.at[i, 'score_results'] += aumento

        # Salvar ou trabalhar com o DataFrame ajustado
        self.df = combined_df

        # Exibir os primeiros registros do DataFrame ajustado
        print(self.df.head())
        self.SalvarBestModel()


    def SalvarBestModel(self):
        self.df.to_csv(constantes.resultado_dir + 'resultado_final.csv')

    
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
            modelo = input('Qual o modelo a ser usado para juntar com o BestModel? ' ).lower()
            if modelo == 'nb':
                return constantes.nb
            elif modelo == 'et':
                return constantes.et
            elif modelo == 'lr':
                return constantes.lr
            elif modelo == 'knn':
                return constantes.knn
            elif modelo == 'gb':
                return constantes.gb
            elif modelo == 'ab':
                return constantes.ab
            elif modelo == 'rf':
                return constantes.rf
            elif modelo == 'bm':
                return constantes.bm
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")


