from flask import render_template, jsonify, Blueprint
from database.db import conexion, cursor
from models.provincias_model import (
    obtener_provincia_por_nombre,
    obtener_eventos_por_provincia,
    obtener_gastronomia_por_provincia,
    obtener_turismo_por_provincia,
    obtener_info_provincia
)

provincias_bp = Blueprint(
    "provincias",
    __name__
)

@provincias_bp.route("/")
def home():
    return render_template("index.html")



@provincias_bp.route("/api/provincia/<nombre>")
def obtener_provincia(nombre):

    try:

        provincia = obtener_provincia_por_nombre(nombre)

        if provincia:

            eventos = obtener_eventos_por_provincia(
                provincia[0]
            )

            gastronomia = obtener_gastronomia_por_provincia(
                provincia[0]
            )

            turismo = obtener_turismo_por_provincia(
                provincia[0]
            )

            informacion = obtener_info_provincia(
                provincia[0]
            )

            return jsonify({
                "nombre": provincia[1],
                "informacion": informacion,
                "eventos": eventos,
                "gastronomia": gastronomia,
                "turismo": turismo
            })

        return jsonify({
            "error": "Provincia no encontrada"
        }), 404
    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 500

@provincias_bp.route("/api/provincias")
def obtener_provincias():
    cursor.execute("SELECT * FROM provincias")
    provincias_db = cursor.fetchall()
    resultado = []

    for provincia in provincias_db:
        resultado.append({
            "id": provincia[0],
            "nombre": provincia[1]
        })

    return jsonify(resultado)

@provincias_bp.route("/api/status")
def status():

    return jsonify({
        "status": "ok"
    })

print("RUTAS CARGADAS")