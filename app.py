import streamlit as st

#Texto
st.title("Meu Primeiro App") #título
st.header("Sistema Python") #cabeeçalho
st.subheader("Lista To-do") #subcabeçalho
st.write("Escreva a sua lista") #texto qualquer

#Entrada
tarefa = st.text_input("Digite a Tarefa")
prio = st.number_input("Ordem de prioridade")
prazo = st.date_input("Data de prazo")
comentario = st.text_area("Comentários sobre a tarefa")
hora = st.time_input("Horário")

#Botões e Mensagens
if st.button("Clique Aqui"):
    #st.write("Botão pressionado!")
    st.success("Cadastro realizado!")

if st.button("Exemplo Erro"):
    st.error("Erro ao salvar!")

if st.button("Exemplo Warning"):
    st.warning("Atenção!")

    
opcao = st.radio(
    "Escolha uma linguagem:",
    ["Python", "Java", "C++"]
)
st.write(opcao)

cidade = st.selectbox(
    "Cidade",
    ["Teresina", "Fortaleza", "Recife"]
)

disciplinas = st.multiselect(
    "Disciplinas",
    ["Python", "SQL", "Redes", "IA"]
)

nota = st.slider(
    "Nota",
    0,
    10
)

#Sidebar
st.sidebar.title("Menu")

opcao = st.sidebar.selectbox(
    "Escolha",
    ["Cadastro", "Relatórios"]
)

#Tabs
aba1, aba2 = st.tabs(
    ["Cadastro", "Relatórios"]
)

with aba1:
    st.write("Tela de cadastro")

with aba2:
    st.write("Tela de Imagem")
    #Imagem
    st.image("logo_pit.png")


#Estrutura e Gráficos
#st.write([1, 2, 3, 4])
dados = {
    "Vendas": [10, 20, 30, 40]
}
st.write(dados)
st.bar_chart(dados)
st.line_chart(dados)
st.area_chart(dados)
