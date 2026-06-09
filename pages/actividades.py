import streamlit as st

from controllers.actividad import listar_actividades, registrar_actividad, eliminar_actividad
from controllers.disciplina import listar_disciplinas

st.title('Actividades')
def obtener_disciplinas_para_selecionar():
    disciplinas = listar_disciplinas()
    if disciplinas:
        return {disciplina["nombre"]: disciplina["id_disciplina"] for disciplina in disciplinas}
    return {}
