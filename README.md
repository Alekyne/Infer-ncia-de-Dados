Veículos
📋 Informações do Projeto
Nome: Relatório de Análise de Regressão
Autor: Maverick Alekyne de Sousa Ribeiro
Professora: Elisângela Rodrigues
Semestre: 4°
📖 Introdução
Este projeto realiza uma análise de regressão em um conjunto de dados de veículos para investigar como diferentes variáveis explicativas, como quilometragem, tipo de combustível e potência, influenciam no preço final dos automóveis. A análise inclui pré-processamento dos dados, verificação de normalidade e transformações para otimização do modelo.

🗂️ Conjunto de Dados
O dataset utilizado contém informações de veículos, como:

Variáveis Categóricas: Nome do veículo, tipo de combustível, tipo de transmissão, etc.
Variáveis Numéricas: Preço, quilometragem, potência, capacidade do motor, etc.
Estrutura das Colunas
Nome da Coluna	Descrição
Name	Nome do modelo do veículo
Year	Ano de fabricação
Kilometers_Driven	Quilômetros rodados
Fuel_Type	Tipo de combustível (Diesel, Gasolina, etc.)
Transmission	Tipo de transmissão (Manual ou Automático)
Mileage	Quilometragem (kmpl)
Engine	Capacidade do motor (CC)
Power	Potência do motor (bhp)
Seats	Número de assentos disponíveis
Price	Preço final do veículo (resposta do modelo)
🛠️ Ferramentas Utilizadas
Linguagem: Python
Bibliotecas:
pandas
matplotlib
seaborn
scikit-learn
scipy
🧹 Pré-Processamento
Tratamento de Valores Ausentes:
Valores ausentes em colunas como Mileage, Engine, e Power foram preenchidos usando a mediana.
Linhas com valores ausentes em New_Price foram descartadas devido à alta taxa de dados ausentes.

Transformação de Dados:

Extração de valores numéricos de colunas como Mileage, Engine, e Power.
Aplicação de transformação logarítmica na variável Engine para aproximar uma distribuição normal.
📊 Visualizações
Distribuições das Variáveis:
Histogramas e gráficos KDE foram criados para inspecionar as distribuições de Mileage, Engine, e Price.

Testes de Normalidade:
Testes de Shapiro-Wilk foram realizados para verificar a normalidade de variáveis explicativas e de resposta.

Transformações e Verificações:
Após a transformação logarítmica, foi analisada a melhoria na normalidade da variável Engine.

🔬 Resultados
Teste de Normalidade (Shapiro-Wilk):

Variáveis como Price, Mileage, e Engine apresentaram distribuições não normais inicialmente.
A transformação logarítmica na variável Engine melhorou a aproximação à normalidade.
Gráficos:
Foram gerados gráficos de probabilidade para reforçar as análises estatísticas e observar o comportamento das variáveis.

🏁 Como Executar
Clone este repositório:
bash
Copiar código
git clone 
cd Analise-Regressao-Veiculos
Instale as dependências:
bash
Copiar código
pip install -r requirements.txt
Execute o script principal:
bash
Copiar código
python analise_regressao.py
📚 Conclusão
Este projeto demonstrou a importância do pré-processamento e da verificação de normalidade em análises de regressão. A transformação logarítmica foi essencial para melhorar a qualidade das variáveis explicativas, resultando em análises mais robustas.

📝 Licença
Este projeto é livre para uso educacional.
