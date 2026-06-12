from BD.obligatorio1.config.database import obtener_conexion

# ABM DE ESPACIOS DEPORTIVOS

# 1. Alta (registrar un nuevo espacio):
def registrar_espacio(nombre, ubicacion, capacidad):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        query = """
            INSERT INTO espacio (nombre, ubicacion, capacidad)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (nombre, ubicacion, capacidad))
        conexion.commit()
        print(f"Espacio '{nombre}' registrado con éxito.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al registrar espacio: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 2. Baja (eliminar un espacio por su ID):
def eliminar_espacio(id_espacio):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM espacio WHERE id_espacio = %s"
        cursor.execute(query, (id_espacio,))
        conexion.commit()
        print(f"Espacio con ID {id_espacio} eliminado correctamente.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al eliminar espacio: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 3. Modificar (actualizar datos de un espacio existente).
def modificar_espacio(id_espacio, nuevo_nombre, nueva_ubicacion, nueva_capacidad):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        query = """
            UPDATE espacio 
            SET nombre = %s, ubicacion = %s, capacidad = %s 
            WHERE id_espacio = %s
        """
        cursor.execute(query, (nuevo_nombre, nueva_ubicacion, nueva_capacidad, id_espacio))
        conexion.commit()
        print(f"Espacio con ID {id_espacio} modificado correctamente.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al modificar espacio: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 4. Listar (traer todos los espacios):
def listar_espacios():
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return []
    try:
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT id_espacio, nombre, ubicacion, capacidad FROM espacio"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al listar espacios: {e}")
        return []
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()