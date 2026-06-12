from BD.obligatorio1.config.database import obtener_conexion

# GESTIÓN DE INSCRIPCIONES:

# Función para registrar las inscripciones.
def registrar_inscripcion(id_estudiante, id_actividad):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor(dictionary=True)
        # Regla 4 del negocio: un estudiante no puede inscribirse dos veces en la misma actividad.
        query_duplicado = "SELECT id_inscripcion FROM inscripcion WHERE id_estudiante = %s AND id_actividad = %s"
        cursor.execute(query_duplicado, (id_estudiante, id_actividad))
        if cursor.fetchone():
            print("Error: el estudiante ya se encuentra inscrito en esta actividad.")
            return False
        # Regla 1 y 6: solo se aceptan inscripciones a actividades abiertas.
        query_actividad = "SELECT estado, cupo_max FROM actividad WHERE id_actividad = %s"
        cursor.execute(query_actividad, (id_actividad,))
        actividad = cursor.fetchone()
        if not actividad:
            print("Error: la actividad no existe.")
            return False
        if actividad['estado'].lower() != 'abierta': # Si el estado no es abierta, no permite inscripción.
            print(f"Error: No se permiten inscripciones.")
            return False
        # Regla 2 y 3: si no hay cupo, la inscripción queda en lista de espera. No se supera la cantidad máxima de cupos.
        cupo_maximo = actividad['cupo_max']
        query_contar = "SELECT COUNT(*) as total FROM inscripcion WHERE id_actividad = %s AND estado_inscripcion = 'Confirmada'" # Contamos las inscripciones que ya están 'confirmada'.
        cursor.execute(query_contar, (id_actividad,))
        actuales = cursor.fetchone()
        inscritos_actuales = actuales['total']
        if inscritos_actuales < cupo_maximo:
            nuevo_estado = "Confirmada"
            mensaje = "Inscripción ralizada con éxito."
        else:
            nuevo_estado = "Lista de espera"
            mensaje = "Cupo lleno. Registrado en lista de espera."
        query_insert = """
            INSERT INTO inscripcion (id_estudiante, id_actividad, estado_inscripcion, fecha_inscripcion)
            VALUES (%s, %s, %s, CURDATE())
        """
        cursor.execute(query_insert, (id_estudiante, id_actividad, nuevo_estado))
        conexion.commit()
        print(f"{mensaje}")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al procesar la inscripción: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# Función para listar las inscripciones hechas (para frontend).
def listar_inscripciones():
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return []
    try:
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT id_inscripcion, id_estudiante, id_actividad, estado_inscripcion, fecha_inscripcion FROM inscripcion"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al listar inscripciones: {e}")
        return []
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()