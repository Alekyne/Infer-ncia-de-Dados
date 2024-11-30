import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Carregar os dados do arquivo CSV (substitua 'caminho/do/arquivo.csv' pelo caminho correto do arquivo)
data = pd.read_csv('caminho/do/arquivo.csv')

# Selecionar as variáveis 'genhlth' e 'idade' do DataFrame
df = data[['genhlth', 'idade']].dropna()

# Função para calcular o intervalo de confiança
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_error = stats.sem(data)
    margin_error = std_error * stats.t.ppf((1 + confidence) / 2, n - 1)
    lower_bound = mean - margin_error
    upper_bound = mean + margin_error
    return lower_bound, upper_bound

# Dividir os dados em grupos com base na variável 'genhlth'
groups = df.groupby('genhlth')['idade']

# Calcular os intervalos de confiança para cada grupo
confidence_intervals = groups.apply(confidence_interval)

# Plotar o gráfico de intervalos de confiança
fig, ax = plt.subplots()

# Cores para os intervalos de confiança de cada categoria
colors = ['blue', 'green', 'orange', 'purple', 'red']

# Posições das barras no eixo x
positions = np.arange(len(confidence_intervals))

# Desenhar as barras dos intervalos de confiança
for i, (category, interval) in enumerate(confidence_intervals.iteritems()):
    ax.plot([i, i], interval, color=colors[i], linewidth=2)
    ax.plot([i - 0.1, i + 0.1], [interval[0], interval[0]], color=colors[i], linewidth=2)
    ax.plot([i - 0.1, i + 0.1], [interval[1], interval[1]], color=colors[i], linewidth=2)
    ax.scatter(i, df[df['genhlth'] == category]['idade'].mean(), color='black', zorder=10)

# Definir os rótulos e ticks do eixo x
ax.set_xticks(positions)
ax.set_xticklabels(confidence_intervals.index)

# Definir os rótulos dos eixos
ax.set_xlabel('Saúde Geral')
ax.set_ylabel('Idade')

# Exibir o gráfico
plt.show()