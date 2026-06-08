# Traemos la función puente que se encuentra dentro de la carpeta config.
from config.database import obtener_conexion

def probar_conexion_inicial():
    print("Iniciando prueba del puente de conexión.")

    # Llamamos a la función para abrir el puente.
    conexion = obtener_conexion()

    # Verificamos si fue una conexión exitosa o no.
    if conexion is not None:
        print("Conexión exitosa.")

        # Cerramos la conexión.
        conexion.close()
        print("Conexión cerrada.")
    else:
        print("Error de conexión.")


if __name__ == "__main__":
    probar_conexion_inicial()