from BD.obligatorio1.config.database import obtener_conexion

# ABM DE DISCIPLINAS DEPORTIVAS:

# 1. Alta (insertar una disciplina):
# Recibe el nombre de una disciplina desde el frontend y la inserta en la BD.
def registrar_disciplina(nombre):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()

        # Consulta (previendo posibles ataque de SQL injection).
        query = "INSERT INTO DISCIPLINA (nombre) VALUES (%s)"
        cursor.execute(query, (nombre,))
        query = "INSERT INTO disciplina (nombre) VALUES (%s)"
        cursor.execute(query, (nombre_disciplina,))
        conexion.commit()

        print(f"Disciplina '{nombre}' registrada con éxito en la BD.")
        return True
    except Exception as e:
        conexion.rollback()
        print(f"Error al insertar la disciplina: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 2. Baja (eliminar una disciplina deportiva po ID):
def eliminar_disciplina(id_disciplina):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM DISCIPLINA WHERE id_disciplina = %s"
        cursor.execute(query, (id_disciplina,))
        conexion.commit()
        print(f"Disciplina con ID {id_disciplina} eliminada correctamente.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al eliminar la disciplina: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 3. Modificar (actualizar nombre por ID):
def modificar_disciplina(id_disciplina, nuevo_nombre):
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()
        query = "UPDATE DISCIPLINA SET nombre = %s WHERE id_disciplina = %s"
        cursor.execute(query, (nuevo_nombre, id_disciplina))
        conexion.commit()
        print(f"Disciplina con ID {id_disciplina} actualizada a '{nuevo_nombre}'.")
        return True
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error al modificar la disciplina: {e}")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

# 4. Extra: función para listar (ayuda al frontend para mostrar al usuario qué puede llegar a manipular).
def listar_disciplinas():
    conexion = obtener_conexion()
    cursor = None
    if conexion is None:
        print("No hay conexión con la BD.")
        return []
    try:
        cursor = conexion.cursor(dictionary=True) # dictionary=True nos devuelve los datos ordenados con los nombres de las columnas
        query = "SELECT id_disciplina, nombre FROM DISCIPLINA"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al listar las disciplinas: {e}")
        return []
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()