import numpy as np
import pandas as pd
from interativo_tratamento_variaveis import InterativoTratamentoVariaveis
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import IncrementalPCA
import pickle
import constantes


class TratamentoVariaveis:
    def __init__(self):
        self.df = None
        self.alvo = None
        self.previsores = None
        self.previsores_scalonados = None
        self.pca_model = None
        self.variance_explained = None

    def capturaDados(self): 
        #skip_func = lambda x: x > 0 and np.random.rand() > 0.03
        #skiprows=skip_func
        self.df = pd.read_csv(constantes.variaveis_csv_file, sep=';')
        print("Dados caputurados")
        self.tratamentoVariaveis()

    def tratamentoVariaveis(self): 
        tratamento = InterativoTratamentoVariaveis(self.df)
        self.previsores, self.alvo = tratamento.processar()
        print(f' previsores retornados {self.previsores}')

        self.pca()
        self.escalonarPrevisores()

    def escalonarPrevisores(self):
        scaler = StandardScaler()
        self.previsores_scalonados = scaler.fit_transform(self.previsores)
        print("Variáveis escalonadas")

    def pca(self, variance_threshold=0.90, batch_size=None):
        n_components = 0
        variance_explained = 0

        while variance_explained < variance_threshold and n_components < self.previsores.shape[1]:
            n_components += 1
            ipca = IncrementalPCA(n_components=n_components, batch_size=batch_size)
            transformed_data = ipca.fit_transform(self.previsores)
            variance_explained = np.sum(ipca.explained_variance_ratio_)

        self.pca_model = ipca
        self.variance_explained = variance_explained
        self.pca_model = transformed_data
        print("Redução de dimensionalidade concluída")
        print(f'Fazendo o algoritimo {n_components} de {self.previsores.shape}')
        print(f'Variância de {variance_explained}')


    def salvarVariaveis(self):
        pickle_files = {
            constantes.alvo: pd.DataFrame(self.alvo),
            constantes.previsores: pd.DataFrame(self.previsores),
            constantes.previsores_scalonados: pd.DataFrame(self.previsores_scalonados),
            constantes.previsores_pca: self.pca_model,
            constantes.df: self.df
        }
       
        print(f'Previsores {self.previsores}')
        print(f'alvo scalonados {self.alvo}')
        totalizador_alvo = pd.DataFrame(self.alvo)
        totalizador_previsores= pd.DataFrame(self.previsores)
        print(f'isna previsores:  {totalizador_previsores.isna().sum()}')
        print(f'isna alvo {totalizador_alvo.isna().sum()}')
        for filename, data in pickle_files.items():
            with open(f'{constantes.variaveis_dir}{filename}', 'wb') as file:
                pickle.dump(data, file)
        print("Variáveis salvas.")
