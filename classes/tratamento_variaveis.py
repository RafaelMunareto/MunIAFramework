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
        base  = input("Qual base vc quer utilizar - digite o nome completo com a extensão? ")
        separado = input('É separado por , ou ; o arquivo ? ')
        try:
            self.df = pd.read_csv(constantes.base_dir +  base, sep=separado)
        except:
            print('Base não encontrada ou diretório inexistente')
        print("Dados caputurados")
        self.tratamentoVariaveis()
    

    def tratamentoVariaveis(self): 
        tratamento = InterativoTratamentoVariaveis(self.df)
        self.previsores, self.alvo = tratamento.processar()
        print(f' previsores retornados \n {self.previsores}')

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
       
        print(f'Previsores \n {self.previsores}')
        print(f'alvo scalonados \n {self.alvo}')
        totalizador_alvo = pd.DataFrame(self.alvo)
        totalizador_previsores= pd.DataFrame(self.previsores)
        print(f'isna previsores:  {totalizador_previsores.isna().sum()}')
        print(f'isna alvo {totalizador_alvo.isna().sum()}')
        for filename, data in pickle_files.items():
            with open(f'{constantes.variaveis_dir}{filename}', 'wb') as file:
                pickle.dump(data, file)
        print("Variáveis salvas.")

    def salvarVariaveisBaseUtilizacao(self):
        pickle_files = {
            constantes.previsores: pd.DataFrame(self.previsores),
            constantes.previsores_scalonados: pd.DataFrame(self.previsores_scalonados),
            constantes.previsores_pca: self.pca_model,
        }
       
        print(f'Previsores \n {self.previsores}')
        totalizador_previsores= pd.DataFrame(self.previsores)
        print(f'isna previsores:  {totalizador_previsores.isna().sum()}')
        for filename, data in pickle_files.items():
            with open(f'{constantes.teste}{filename}', 'wb') as file:
                pickle.dump(data, file)
        print("Variáveis salvas.")