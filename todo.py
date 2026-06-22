import streamlit as st

st.title("LISTA DE TAREFAS")

if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

if "feitas" not in st.session_state:
        st.session_state.feitas = []

aba1, aba2, aba3, aba4 = st.tabs(
    ["Cadastrar Tarefas", "Ver Tarefas", "Tarefas Feitas", "Estatísticas"]
)

with aba1:
    st.write("Cadastrar Tarefas")
    tarefa = st.text_input("Digite a Tarefa")
    if st.button("Salvar Tarefa"):
        if tarefa:
            st.session_state.tarefas.append(tarefa)
            st.success("Tarefa adicionada!")
        else:
            st.warning("Digite uma tarefa.")

with aba2:
    st.write("Ver Tarefas")
    if len(st.session_state.tarefas) == 0:
        st.info("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(st.session_state.tarefas):
            #st.write(f"{i+1}. {tarefa}")
            col1, col2 = st.columns([2,1])
            with col1:
                st.write(tarefa)
            with col2:
                if st.button("❌", key=i):
                    feito = st.session_state.tarefas.pop(i)
                    st.session_state.feitas.append(feito)
                    st.rerun()

with aba3:
    st.write("Tarefas Feitas")
    for fez in st.session_state.feitas:
        st.write(f"{fez}")

with aba4:
    st.write("Estatísticas")
    fazer = len(st.session_state.tarefas)
    concluida = len(st.session_state.feitas)
    total = fazer + concluida
    pendente = total - concluida

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total", total)

    with col2:
        st.metric("Concluídas", concluida)

    with col3:
        st.metric("Pendentes", pendente)