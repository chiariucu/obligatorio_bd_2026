from config.database import obtener_conexion

# Recibe el nombre de una disciplina desde el frontend y la inserta en la BD.
def registrar_disciplina(nombre_disciplina):
    conexion = obtener_conexion()
    if conexion is None:
        print("No hay conexión con la BD.")
        return False
    try:
        cursor = conexion.cursor()

        # Consulta (previendo posibles ataque de SQL injection).
        query = "INSERT INTO DISCIPLINA (nombre) VALUES (%s)"
        cursor.execute(query, (nombre_disciplina,))
        conexion.commit()

        print(f"Disciplina '{nombre_disciplina}' registrada con éxito en la BD.")
        return True
    except Exception as e:
        conexion.rollback()
        print(f"Error al insertar la disciplina: {e}")
        return False
    finally:
        cursor.close()
        conexion.close()