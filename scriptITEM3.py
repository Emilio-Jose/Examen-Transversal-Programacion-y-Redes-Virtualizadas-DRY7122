import sqlite3
import hashlib
from flask import Flask, request

sitio = Flask(__name__)


def crear_base():
    conexion = sqlite3.connect("personas.db")
    conexion.execute("CREATE TABLE IF NOT EXISTS personas (nombre TEXT, clave TEXT)")
    conexion.commit()
    conexion.close()


@sitio.route("/registrar", methods=["POST"])
def registrar():
    try:
        datos = request.form
        print("Datos recibidos:", datos)

        nombre = datos["nombre"]
        clave_plana = datos["clave"]
        clave_cifrada = hashlib.sha256(clave_plana.encode()).hexdigest()

        conexion = sqlite3.connect("personas.db")
        conexion.execute("INSERT INTO personas (nombre, clave) VALUES (?, ?)", (nombre, clave_cifrada))
        conexion.commit()
        conexion.close()

        return "Persona registrada correctamente"
    except Exception as error:
        return f"Error al registrar: {str(error)}", 400


@sitio.route("/verificar", methods=["POST"])
def verificar():
    try:
        datos = request.form
        nombre = datos["nombre"]
        clave_plana = datos["clave"]
        clave_cifrada = hashlib.sha256(clave_plana.encode()).hexdigest()

        conexion = sqlite3.connect("personas.db")
        consulta = conexion.execute("SELECT * FROM personas WHERE nombre = ? AND clave = ?", (nombre, clave_cifrada))
        persona = consulta.fetchone()
        conexion.close()

        if persona:
            return "Ingreso correcto"
        else:
            return "Nombre o clave incorrecta"
    except Exception as error:
        return f"Error al verificar: {str(error)}", 400


if __name__ == "__main__":
    crear_base()
    sitio.run(host="0.0.0.0", port=5800, ssl_context='adhoc')
