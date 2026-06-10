from BD.obligatorio1.config.database import obtener_conexion

# GESTIÓN DE ASISTENCIAS:

#Función que registra la asistencia de los estudiantes con inscripción confirmada.
def registrar_asistencia(id_inscripcion, fecha, asistio):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor(dictionary=True)
        # Regla 5: solo se registra la asistencia de estudiantes con la inscripción confirmada.
        query_inscripcion = "SELECT estado_inscripcion FROM inscripcion WHERE id_inscripcion = %s"
        cursor.execute(query_inscripcion, (id_inscripcion,))
        inscripcion = cursor.fetchone()
        if not inscripcion:
            print("Error: no existe inscripción.")
            return False
        if inscripcion['estado_inscripcion'].lower() != 'confirmada':
            print(
                f"Error: No se puede registrar asistencia.")
            return False
        # Caso de que sí se puede registrar la asistencia.
        query_insert = """ 
            INSERT INTO asistencia (id_inscripcion, fecha, asistio)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query_insert, (id_inscripcion, fecha, asistio))
        conexion.commit()
        print(f"Asistencia registrada correctamente.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al registrar la asistencia: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()