from BD.obligatorio1.config.database import obtener_conexion

# ABM DE ACTIVIDADES DEPORTIVAS:

# 1. Alta (insertar actividades deportivas):
def registrar_actividad(nombre_actividad, id_disciplina, id_espacio, cupo_max, dia, horario, estado):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        query = """
            INSERT INTO actividad (nombre_actividad, id_disciplina, id_espacio, cupo_max, dia, horario, estado) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre_actividad, id_disciplina, id_espacio, cupo_max, dia, horario, estado))
        conexion.commit()
        print(f"Actividad '{nombre_actividad}' registrada con éxito en la BD.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al insertar la actividad: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 2. Baja (elimina actividad):
def eliminar_actividad(id_actividad):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM actividad WHERE id_actividad = %s"
        cursor.execute(query, (id_actividad,))
        conexion.commit()
        print(f"Actividad con ID {id_actividad} eliminada correctamente.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al eliminar: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()


# 3. Modificar (actualiza datos de una actividad existente).
def modificar_actividad(id_actividad, nuevo_nombre_actividad, nuevo_id_disciplina, nuevo_id_espacio, nuevo_cupo, nuevo_dia,
                        nuevo_horario, nuevo_estado):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        query = """
            UPDATE actividad 
            SET nombre_actividad = %s, id_disciplina = %s, id_espacio = %s, cupo_max = %s, dia = %s, horario = %s, estado = %s 
            WHERE id_actividad = %s
        """
        cursor.execute(query, (nuevo_nombre_actividad, nuevo_id_disciplina, nuevo_id_espacio, nuevo_cupo, nuevo_dia, nuevo_horario,
                               nuevo_estado, id_actividad))
        conexion.commit()
        print(f"Actividad con ID {id_actividad} modificada correctamente.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al modificar: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 4. Extra: función para listar (ayuda a frontend a mostrar actividades).
def listar_actividades():
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return []
    try:
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT id_actividad, nombre_actividad, id_disciplina, id_espacio, cupo_max, dia, horario, estado FROM actividad"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al listar: {e}")
        return []
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()