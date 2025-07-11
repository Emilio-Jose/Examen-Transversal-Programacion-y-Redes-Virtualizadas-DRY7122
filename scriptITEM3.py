# scriptITEM3.py
# Sitio web básico que guarda y verifica usuarios con contraseñas seguras

import sqlite3
import hashlib
from flask import Flask, request

pagina = Flask(__name__)

# Crear base de datos y tabla si no existen
def base_datos():
    bd = sqlite3.connect("usuarios.db")
    bd.execute("CREATE TABLE IF NOT EXISTS datos (nombre TEXT, clave TEXT)")
    bd.commit()
    bd.close()

# Ruta para guardar usuario nuevo
@pagina.route("/guardar", methods=["POST"])
def guardar():
    try:
        print("Contenido recibido:", request.form)  # Línea de depuración
        nombre = request.form["nombre"]
        clave = request.form["clave"]
        clave_segura = hashlib.sha256(clave.encode()).hexdigest()
        bd = sqlite3.connect("usuarios.db")
        bd.execute("INSERT INTO datos (nombre, clave) VALUES (?, ?)", (nombre, clave_segura))
        bd.commit()
        bd.close()
        return "Usuario guardado"
    except Exception as error:
        return f"Error al guardar: {str(error)}", 400

# Ruta para verificar usuario
@pagina.route("/verificar", methods=["POST"])
def verificar():
    try:
        nombre = request.form["nombre"]
        clave = request.form["clave"]
        clave_segura = hashlib.sha256(clave.encode()).hexdigest()
        bd = sqlite3.connect("usuarios.db")
        r = bd.execute("SELECT * FROM datos WHERE nombre = ? AND clave = ?", (nombre, clave_segura))
        if r.fetchone():
            return "Correcto"
        else:
            return "Incorrecto"
    except Exception as error:
        return f"Error al verificar: {str(error)}", 400

# Iniciar la aplicación
if __name__ == "__main__":
    base_datos()
    pagina.run(host="0.0.0.0", port=5800)

