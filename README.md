## Consultor IA

**Projeto criado para exemplificar o uso de Árvores de Decisão com banco de dados e Regressão Logística na prática. **


**O que é o Consultor IA?**

O consultor IA é um assistente virtual que auxilia com sua vida empresarial.

**Contexto do problema 😢**

Liderança de equipes e entender o sentimento dos seus funcionarios é uma tarefa complexa.

1. A maioria das pessoas não sabe como lidar no ambiente corporativo, seja como empregado ou até mesmo empregador.

2. Seu currículo é a primeira impressão que você passa para o recrutador. É importante que ele esteja bem estruturado e adequado para a vaga à qual você está se candidatando, mas a maioria das pessoas acaba usando o mesmo currículo para vagas diferentes.

**Soluções 🚀**

* **1_👨‍🏫Chat.py:** Esse assistente virtual usa um banco de dados exemplificando as possíveis causas de pedido de demissão ou falta de interesse no trabalho. Esse assistente pode te ajudar a evitar a perda de funcionários.


* **ProducaoCurriculo📄:** Analisa seu currículo e a vaga de interesse, fornecendo feedback construtivo para que você o aperfeiçoe e aumente suas chances de ser chamado para uma entrevista.


### Cosultor IA está online!

Fiz o deploy por meio da Streamlit Cloud.
Para acessar o aplicativo ConsultorIA, clique no link abaixo:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://iaconsultor.streamlit.app/)


**Arquivos do Projeto:**

* **🏠Home.py** Página Home explica sobre os assistentes
* **1_👨‍🏫Chat.py:** Código do assistente virtual ConsultorIA.
* **3_📄ProducaoCurriculo.py:** Código do assistente virtual ProducaoCurriculo.

**Tecnologias utilizadas:**

* Python
* Streamlit
* Google Generative AI


**Como rodar o projeto na sua máquina:**

1. Clonar o repositório:
2. Acessar a pasta do projeto /streamlit
3. Instalar as dependências:
```bash
pip install -r requirements.txt
```
4. Criar um arquivo .env e adicionar a chave da API do Google Generative AI:
```bash
gemini_api_key = ""
```
4. Rodar o arquivo 🏠Home.py:
```bash
streamlit run 🏠Home.py
```



