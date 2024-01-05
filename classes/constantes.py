

# Diretórios de arquivos
base_dir = 'base/'
resultado_dir = 'resultado/'
algoritimos_dir = 'algoritimos/'
variaveis_dir = 'variaveis'
variaveis_csv_file = base_dir + 'IA_TUDO_EM_DIA_CONTROLE.txt'
max_alvo_previsor = ':'

#variaveis 
alvo = 'alvo.pickle'
previsores = 'previsores.pickle'
previsores_scalonados = 'previsores_scalonados.pickle'
previsores_pca = 'previsores_pca.pickle'
df = 'df.pickle'
df_com_previsao = './algoritmos/df_com_previsao.pickle'
resultado_completo_df = 'resultado_completos_metrica_algoritimos.pickle'
results_df = resultado_dir + 'df_com_previsao.pickle'
respostas_tratamento_base = 'respostas_tratamento_base.pickle'

#colunas previsores 
predicao = 'predicao'
score = 'score'
#alvo = 'alvo'
faixa_score = 'Faixa_Score'

#modelos de treinos
rf =  "RandomForest"
lr = "LogisticRegression"
knn = "KNeighbors"
nb = "GaussianNB"
sgd = "SGDClassifier"
gb = "GradientBoosting"
ab =  "AdaBoost"
dt = "DecisionTree"
et = "ExtraTrees"
ct = "CatBoost"
bm = "BestModel"

#previsor_utilizado e modelo utilizado
previsor_utilizado = previsores_scalonados
cv = 10
x = 'X_test.pickle'
modelo_aplicado = algoritimos_dir + bm + ".pickle" 


