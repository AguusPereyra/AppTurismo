import os

from werkzeug.utils import secure_filename

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    url_for
)

from models.provincias_models import (
    obtener_usuario_por_email,
    obtener_todas_las_provincias,
    obtener_info_provincia_admin,
    actualizar_provincia,
    actualizar_imagen_provincia
)

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        usuario = obtener_usuario_por_email(
            email
        )

        if usuario and usuario[3] == password:

            session["usuario"] = usuario[1]

            session["rol"] = usuario[4]

            return redirect(
                url_for("auth.admin")
            )

        return render_template(
            "login.html",
            error="Credenciales incorrectas"
        )

    return render_template(
        "login.html"
    )

@auth_bp.route("/admin")
def admin():

    if "usuario" not in session:

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "admin.html",
        usuario=session["usuario"]
    )

@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("auth.login")
    )

@auth_bp.route("/admin/provincias")
def admin_provincias():

    if "usuario" not in session:

        return redirect(
            url_for("auth.login")
        )

    provincias = obtener_todas_las_provincias()

    return render_template(
        "admin_provincias.html",
        provincias=provincias
    )

@auth_bp.route(
    "/admin/provincias/<int:provincia_id>/editar",
    methods=["GET", "POST"]
)
def editar_provincias(provincia_id):

    if "usuario" not in session:

        return redirect(url_for("auth.login"))

    if request.method == "POST":

        actualizar_provincia(
            provincia_id,
            request.form["descripcion"],
            request.form["capital"],
            request.form["poblacion"],
            request.form["superficie"],
            request.form["region"],
            request.form["dato_curioso"]
        )

        imagen = request.files.get(
            "imagen"
        )

        if imagen and imagen.filename:

            nombre_archivo = secure_filename(
                imagen.filename
            )

            ruta = os.path.join("static", "img", "provincias", nombre_archivo)

            imagen.save(ruta)

            print(request.files)
            print(request.files.get("imagen"))

            actualizar_imagen_provincia(provincia_id, nombre_archivo)

        return redirect(url_for("auth.admin_provincias"))

    provincia = obtener_info_provincia_admin(
        provincia_id
    )

    return render_template("editar_provincias.html", provincia=provincia)