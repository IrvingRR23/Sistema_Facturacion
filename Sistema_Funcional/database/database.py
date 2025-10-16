import mysql.connector
from mysql.connector import Error

class DatabaseConnection:

    def __init__(self, host = "localhost", user="root",password = "", database="restaurante"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                if self.connection.is_connected():
                    print(f"Conectado a la base de datos '{self.database}' en {self.host}")
            except Error as e:
                print(f"Error al conectar con la base de datos: {e}")
        
    def cerrar(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexion cerrada correctamente.")
        
    def ejecutar_consulta(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error al ejecutar consulta {e}")
            return False
            
    def obtener_datos(self, query, params=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except Error as e:
            print(f"Error al obtener datos: {e}")
            return False


if __name__ == "__main__":
    # Cambia "darko" por tu contraseña real de MySQL
    db = DatabaseConnection(password="darko")  
    db.conectar()

    # Prueba rápida
    productos = db.obtener_datos("SELECT * FROM productos LIMIT 5;")
    for p in productos:
        print(f"{p['id']}: {p['nombre']} - {p['categoria']} - ${p['precio']:.2f}")

    db.cerrar()