# 🛰️ OrbitalWatch AI

Projeto desenvolvido para a disciplina **Generative AI For Engineering (GAIE)** da **Global Solution 2026 - FIAP**.

O **OrbitalWatch AI** usa dados do dataset **NASA FIRMS** do kaggle para classificar focos de calor detectados por satélite em níveis de risco. A ideia é apoiar o monitoramento ambiental, ajudando a priorizar ocorrências mais relevantes dentro da plataforma OrbitalWatch.
Link dos Datasets: https://www.kaggle.com/datasets/vijayveersingh/nasa-firms-active-fire-dataset-modisviirs/data

Obs. Não foi possível adicioanr os datasets no reposítório pelo tamanho
Link da aplicação: https://gs1-ia-bnnpakcgxg9pi2qywsgmac.streamlit.app/
---

## 📌 Objetivo

A NASA FIRMS já informa focos de calor detectados por satélite. O objetivo deste projeto é classificar esses registros em:

* **baixo**
* **medio**
* **alto**

Assim, a plataforma consegue destacar primeiro os focos com maior prioridade, considerando intensidade térmica, potência radiativa do fogo e confiança da detecção.

---

## 👥 Integrantes

Caíque Walter Silva - RM550693
Guilherme Nobre Bernardo - RM98604
Guilherme Monteiro Espim - RM99499
João Paulo Fonseca Zamperlini - RM99279
Matheus José de Lima Costa - RM551157

---

## 🛰️ Dados utilizados

Os datasets utilizados vêm da base **NASA FIRMS** e devem estar na pasta `datasets/`.

| Arquivo               | Descrição                                                               |
| --------------------- | ----------------------------------------------------------------------- |
| `fire_nrt_J1V-C2.csv` | Focos de calor detectados pelo sensor VIIRS do satélite NOAA-20/JPSS-1. |
| `fire_nrt_SV-C2.csv`  | Focos de calor detectados pelo sensor VIIRS do satélite Suomi NPP.      |
| `fire_nrt_M-C61.csv`  | Focos de calor detectados pelo sensor MODIS, usado como complemento.    |

Principais variáveis usadas: latitude, longitude, temperatura de brilho, `frp`, confiança da detecção, satélite, instrumento e período dia/noite.

---

## 🧠 Metodologia

O pipeline realiza:

1. carregamento dos CSVs;
2. padronização das colunas;
3. tratamento de variáveis textuais;
4. criação da variável-alvo `risco`;
5. separação treino/teste;
6. treinamento de modelos;
7. comparação de métricas;
8. interpretação com SHAP;
9. salvamento do modelo para uso no Streamlit.

Como a base NASA FIRMS não possui uma coluna oficial de risco, a variável `risco` foi criada com base em `frp`, temperatura de brilho e confiança da detecção.

---

## 🤖 Modelos

Foram comparados:

* **Regressão Logística**
* **Random Forest**

As métricas usadas foram acurácia, F1-score, relatório de classificação e matriz de confusão.

---

## 🔎 Interpretabilidade

Foi utilizado **SHAP** para entender quais variáveis mais influenciam as previsões do modelo, como `frp`, temperatura de brilho, confiança da detecção e localização.

---

## 📁 Estrutura

```text
.
├── app.py
├── OrbitalWatch_Pipeline.ipynb
├── orbitalwatch_model.joblib
├── requirements.txt
├── README.md
└── datasets/
    ├── fire_nrt_J1V-C2.csv
    ├── fire_nrt_SV-C2.csv
    └── fire_nrt_M-C61.csv
```

---

## 📦 Instalação

No terminal, dentro da pasta do projeto:

```bash
pip install -r requirements.txt
```

Caso tenha mais de uma versão do Python instalada:

```bash
py -3.12 -m pip install -r requirements.txt
```

---

## ▶️ Execução

Execute primeiro o notebook:

```text
OrbitalWatch_Pipeline.ipynb
```

Ao final, ele gera o arquivo:

```text
orbitalwatch_model.joblib
```

Depois rode a aplicação:

```bash
py -3.12 -m streamlit run app.py
```

A aplicação abre normalmente em:

```text
http://localhost:8501
```

---

## ✅ Conclusão

O **OrbitalWatch AI** cria uma camada de inteligência sobre dados orbitais de focos de calor.

A solução não prevê incêndios futuros. Ela classifica o risco de focos já detectados por satélite, permitindo que a plataforma organize os alertas e destaque ocorrências com maior prioridade.

Como evolução futura, o modelo poderia incluir dados de bioma, clima, vento, área queimada e proximidade de áreas urbanas.
