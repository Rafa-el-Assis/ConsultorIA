import streamlit as st


# Adicionando título 
st.title('Consultor IA 🖥️')

# Adicionando descrição do projeto
st.write("Aprimorar suas habilidades de liderança e gestão é um processo contínuo que exige dedicação e as orientações certas. O Consultor IA é uma plataforma com dois assistentes virtuais que te ajudam em todas as etapas desse desenvolvimento.")

# Adicionando as etapas do projeto
etapas = [
    {
        "nome": "Chat",
        "icone": "👨‍🏫",
        "descricao": "Receba dicas e orientações personalizadas para aprimorar suas habilidades de liderança e gestão, com base nas suas experiências e objetivos.",
    },

    {
        "nome": "Produzir Currículo",
        "icone": "📄",
        "descricao": "Envie seu currículo para receber feedback personalizado com sugestões de melhoria e insights valiosos",
    }
]

# Adicionando as etapas como seções
for etapa in etapas:
    st.header(f"{etapa['icone']} {etapa['nome']}")
    st.write(etapa['descricao'])
    if 'pagina' in etapa:
        st.markdown(f"**Página da solução:** {etapa['pagina']}")
