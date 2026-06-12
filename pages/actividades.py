import streamlit as st

from controllers.actividad import listar_actividades, registrar_actividad, eliminar_actividad
from controllers.disciplina import listar_disciplinas

st.title('Actividades')
def obtener_disciplinas_para_selecionar():
    disciplinas = listar_disciplinas()
    if disciplinas:
        return {disciplina["nombre"]: disciplina["id_disciplina"] for disciplina in disciplinas}
    return {}


if st.button("Cargar actividades"):
    actividades = listar_actividades()

    st.write("Resultado recibido del backend:")

    if actividades:
        st.success(f"✅ Se encontraron {len(actividades)} actividades")

        # Mostrar cada actividad de forma sencilla
        for act in actividades:
            with st.container():
                st.markdown(f"### {act['nombre_actividad']}")
                st.write(f"**ID:** {act['id_actividad']}")
                st.write(f"**Disciplina ID:** {act['id_disciplina']}")
                st.write(f"**Espacio ID:** {act['id_espacio']}")
                st.write(f"**Cupo máximo:** {act['cupo_max']}")
                st.write(f"**Día:** {act['dia']}")
                st.write(f"**Horario:** {act['horario']}")
                st.write(f"**Estado:** {act['estado']}")
                st.divider()
    else:
        st.error("❌ No se encontraron actividades")