from BD.obligatorio1.config.database import obtener_conexion

# ABM DE ESTUDIANTES:

# 1. Alta (registrar un nuevo estudiante):
def registrar_estudiante(documento, nombre, apellido, email, carrera, facultad):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        query = """
            INSERT INTO estudiante (documento, nombre, apellido, email, carrera, facultad)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (documento, nombre, apellido, email, carrera, facultad))
        conexion.commit()
        print(f"Estudiante {nombre} {apellido} registrado con éxito.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        # Si la cédula o email, como son unique, ya existen, va a venir aquí directo.
        print(f"Error al registrar estudiante (puede que la cédula o email ya existan): {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 2. Baja (eliminar un estudiante por su ID):
def eliminar_estudiante(id_estudiante):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM estudiante WHERE id_estudiante = %s"
        cursor.execute(query, (id_estudiante,))
        conexion.commit()
        print(f"Estudiante con ID {id_estudiante} eliminado correctamente.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al eliminar estudiante: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 3. Modificar (actualizar datos de un estudiante existente):
def modificar_estudiante(id_estudiante, nuevo_documento, nuevo_nombre, nuevo_apellido, nuevo_email, nueva_carrera, nueva_facultad):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        # Modificamos los campos usando el id_estudiante en el WHERE.
        query = """
            UPDATE estudiante 
            SET documento = %s, nombre = %s, apellido = %s, email = %s, carrera = %s, facultad = %s 
            WHERE id_estudiante = %s
        """
        cursor.execute(query, (nuevo_documento, nuevo_nombre, nuevo_apellido, nuevo_email, nueva_carrera, nueva_facultad, id_estudiante))
        conexion.commit()
        print(f"Estudiante con ID {id_estudiante} modificado correctamente.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al modificar estudiante: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 4. Listar (traer todos los estudiantes en formato diccionario para el front):
def listar_estudiantes():
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return []
    try:
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT id_estudiante, documento, nombre, apellido, email, carrera, facultad FROM estudiante"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al listar estudiantes: {e}")
        return []
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()