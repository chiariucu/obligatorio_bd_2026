import mysql.connector
from mysql.connector import Error #Para prevenir errores.

# CONFIGURACIÓN A MySQL.
DB_CONFIG = {
    "host": "localhost",
    "port": 3307,
    "user": "root",
    "password": "rootpassword",
    "database": "actividades_deportivas",
    "autocommit": False  # Lo dejamos en False para que no se guarden datos incompletos antes de tiempo.
}
# CONEXIÓN (contempla fallas).
def obtener_conexion():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None