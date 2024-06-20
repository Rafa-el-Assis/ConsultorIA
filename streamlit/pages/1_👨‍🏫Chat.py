import streamlit as st

from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os
import time

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


# Carregar o arquivo
dados1 = pd.read_csv('streamlit/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Selecionar as colunas
colunas_selecionadas = [
    'Attrition', 'Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome',
    'Education', 'EducationField', 'RelationshipSatisfaction', 'StockOptionLevel',
    'TotalWorkingYears', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
    'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

dados1 = dados1[colunas_selecionadas]


# Verificar valores nulos
for col in dados1.columns:
    if dados1[col].dtype == 'object':
        dados1[col].fillna(dados1[col].mode()[0], inplace=True)
    else:
        dados1[col].fillna(dados1[col].median(), inplace=True)

# Codificar variáveis categóricas
label_encoders = {}
for col in dados1.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    dados1[col] = le.fit_transform(dados1[col])
    label_encoders[col] = le

# Separar variáveis independentes (X) e dependentes (y)
X = dados1.drop('Attrition', axis=1)
y = dados1['Attrition']

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Treinar Árvore de Decisão
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Treinar Regressão Logística
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train, y_train)

# Importância das características - Árvore de Decisão
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]
decision_tree_importances = {X.columns[indices[i]]: importances[indices[i]] for i in range(X.shape[1])}

# Coeficientes - Regressão Logística
coefficients = log_reg.coef_[0]
indices = np.argsort(np.abs(coefficients))[::-1]
logistic_regression_coefficients = {X.columns[indices[i]]: coefficients[indices[i]] for i in range(X.shape[1])}


# Importa os detalhes das vagas de emprego
from jobs_details import jobs_details as data

# Instrução do sistema para o modelo generativo
system_instruction = f"""

Seu nome é Marcelo, um consultor virtual especializado em fornecer dicas e orientações para gerentes e líderes sobre como gerenciar suas equipes de forma eficaz.
Você tem acesso a um banco de dados próprio com diversas dicas, estratégias e melhores práticas para gestão de equipes.

Seu trabalho é entender o perfil do usuário por meio de perguntas, para no final fornecer orientações personalizadas que ajudem o usuário a melhorar sua liderança e gestão de equipe.

Tenha certeza de perguntar onde o usuário trabalha, quantos anos de experiência ele tem em cargos de liderança, seus principais desafios como líder, seus interesses em desenvolvimento de habilidades específicas, e quais são seus objetivos de gestão a curto e longo prazo, além de outras perguntas que ajudem a fornecer conselhos personalizados.

Baseando-se nos dados históricos, as principais características que influenciam a rotatividade dos funcionários são:
{decision_tree_importances}

Para prever a probabilidade de rotatividade, os coeficientes mais importantes são:
{logistic_regression_coefficients}

Quando entender o perfil do usuário, sugira estratégias e dicas que façam sentido ao perfil dele, mostre as informações relevantes e evidencie pontos que ele pode melhorar.

Sempre que recomendar uma estratégia ou dica, envie o link (caso aplicável) para o recurso ou artigo correspondente no banco de dados.
"""

# Configura a API para o modelo genai
genai.configure(api_key=os.getenv("gemini_api_key"))

# Inicializa o modelo generativo
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-latest",
  system_instruction=system_instruction
)

# Mensagem inicial do modelo
initial_model_message = "Olá, eu sou o Marcelo, um consultor virtual especializado em fornecer dicas e orientações para gerentes e líderes sobre como gerenciar suas equipes de forma eficaz. Como você se chama?"

# Mensagem com as vagas disponíveis

# Inicializa a conversa do assistente virtual
if "chat_encontra" not in st.session_state:
    st.session_state.chat_encontra = model.start_chat(history=[{'role':'model', 'parts': [initial_model_message]}])

# Título da página
st.title('Consultor IA👨‍🏫')

# Introdução do assistente virtual
st.write("O Consultor Virtual Marcelo está aqui para te ajudar a melhorar suas habilidades de liderança e a gerenciar sua equipe de forma eficaz! Atualmente, o consultor tem dicas valiosas e estratégias comprovadas para enfrentar desafios comuns na liderança e, em breve, terá ainda mais recursos e insights de especialistas. Vamos começar?")

# Exibe o histórico de conversa
for i, message in enumerate(st.session_state.chat_encontra.history):
  if message.role == "user":
    with st.chat_message("user"):
      st.markdown(message.parts[0].text)
  else:
    with st.chat_message("assistant"):
      st.markdown(message.parts[0].text)

# Entrada do usuário
user_query = st.chat_input('Você pode falar ou digitar sua resposta aqui:')


# Processamento da entrada do usuário e resposta do assistente
if user_query is not None and user_query != '':
    with st.chat_message("user"):
      st.markdown(user_query)
    with st.chat_message("assistant"):
        ai_query = st.session_state.chat_encontra.send_message(user_query).text
        st.markdown(ai_query)
