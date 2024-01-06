import json
import pickle
import pandas as pd
import constantes 

class ScoreBestModel:
    def __init__(self):
        self.df = None
        self.modelo = None
        self.results = None
        self.bm = None

    def juntarComBestModel(self):
        print('Qual modelo quer juntar com a previsao do BestModel para melhorar o score?')
        with open(f'{constantes.algoritimos_dir}/{constantes.resultado_completo_df}', 'rb') as file:
            resultados_formatados = pickle.load(file)
        print(json.dumps(resultados_formatados, indent=4))

        self.modelo = self.pergunta()

        try:
            self.results = pd.read_csv(constantes.resultado_dir + self.modelo + '.csv', sep=',')
        except FileNotFoundError:
            print(f'Erro: arquivo de resultados do modelo {self.modelo} não encontrado.')
            return  # Encerra a execução da função

        try:
            self.bm = pd.read_csv(constantes.resultado_dir + constantes.bm + '.csv', sep=',')
        except FileNotFoundError:
            print('Erro: arquivo de resultados do BestModel não encontrado.')
            return  # Encerra a execução da função

        print("Bases carregadas")
        self.refazerScoreComBestModel()

    def refazerScoreComBestModel(self):
        # Verificações das colunas
        if 'predicao' not in self.results.columns:
            raise ValueError(f"Coluna 'predicao' não encontrada no DataFrame 'results' do modelo {self.modelo}.")
        if 'predicao' not in self.bm.columns:
            raise ValueError("Coluna 'predicao' não encontrada no DataFrame 'bm' do BestModel.")

        # Renomear colunas para evitar conflitos
        self.results.rename(columns={'predicao': 'predicao_results', 'score': 'score_results'}, inplace=True)
        self.bm.rename(columns={'predicao': 'predicao_bm', 'score': 'score_bm'}, inplace=True)

        # Juntar DataFrames
        combined_df = pd.merge(self.results, self.bm, left_index=True, right_index=True, how='left')

        # Ajustar scores
        for i, row in combined_df.iterrows():
            if row['predicao_bm'] == 1 and row['score_results'] < 70:
                aumento = row['score_results'] * 0.10  # Aumento de 10% do score atual
                novo_score = min(100, row['score_results'] + aumento)  # Garantir que o score não ultrapasse 100%
                combined_df.at[i, 'score_results'] = novo_score

        # Selecionar todas as colunas do DataFrame 'results' e adicionar o score ajustado
        self.df = self.results.copy()
        self.df['score_ajustado'] = combined_df['score_results'].apply(lambda x: min(100, x * 100))
        self.df.drop(columns='Unnamed: 0', inplace=True)
        print(self.df.head())
        print(f'10 Score > 70 \n {self.df.query('score_ajustado > 70').sort_values('score_ajustado', ascending=True)}')
        self.salvarBestModel()

    def salvarBestModel(self):
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
            print("GB - GradientBoosting")
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


