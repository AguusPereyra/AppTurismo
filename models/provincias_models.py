from database.db import conexion, cursor

def obtener_usuario_por_email(email):

    cursor.execute("""
    SELECT *
    FROM usuarios
    WHERE email = ?
    """, (email,))

    return cursor.fetchone()

def obtener_todas_las_provincias():

    cursor.execute("""
    SELECT id, nombre
    FROM provincias
    ORDER BY nombre
    """)

    return cursor.fetchall()

def obtener_info_provincia_admin(provincia_id):

    cursor.execute("""
    SELECT
        provincias.id,
        provincias.nombre,
        provincias.imagen,
        informacion_provincia.descripcion,
        informacion_provincia.capital,
        informacion_provincia.poblacion,
        informacion_provincia.superficie,
        informacion_provincia.region,
        informacion_provincia.dato_curioso
    FROM provincias

    JOIN informacion_provincia
    ON provincias.id =
       informacion_provincia.provincia_id

    WHERE provincias.id = ?
    """, (provincia_id,))

    return cursor.fetchone()

def actualizar_provincia(
    provincia_id,
    descripcion,
    capital,
    poblacion,
    superficie,
    region,
    dato_curioso
):

    cursor.execute("""
    UPDATE informacion_provincia

    SET
        descripcion = ?,
        capital = ?,
        poblacion = ?,
        superficie = ?,
        region = ?,
        dato_curioso = ?

    WHERE provincia_id = ?
    """, (
        descripcion,
        capital,
        poblacion,
        superficie,
        region,
        dato_curioso,
        provincia_id
    ))

    conexion.commit()

def obtener_provincia_por_nombre(nombre):
    cursor.execute("""
    SELECT *
    FROM provincias
    WHERE nombre = ?
    """, (nombre,))
    return cursor.fetchone()

def obtener_eventos_por_provincia(provincia_id):
    cursor.execute("""
    SELECT nombre, fecha, lugar, imagen
    FROM eventos
    WHERE provincia_id = ?
    """, (provincia_id,))
    eventos_db = cursor.fetchall()
    eventos = []

    for evento in eventos_db:

        eventos.append({
            "nombre": evento[0],
            "fecha": evento[1],
            "lugar": evento[2],
            "imagen": evento[3]
        })

    return eventos

def obtener_gastronomia_por_provincia(provincia_id):
    cursor.execute("""
    SELECT nombre
    FROM gastronomia
    WHERE provincia_id = ?
    """, (provincia_id,))
    gastronomia_db = cursor.fetchall()
    gastronomia = []

    for comida in gastronomia_db:

        gastronomia.append(comida[0])

    return gastronomia

def obtener_turismo_por_provincia(provincia_id):
    cursor.execute("""
    SELECT nombre
    FROM turismo
    WHERE provincia_id = ?
    """, (provincia_id,))
    turismo_db = cursor.fetchall()

    turismo = []

    for lugar in turismo_db:
        turismo.append(lugar[0])
    return turismo

def obtener_info_provincia(provincia_id):
    cursor.execute("""
    SELECT
        descripcion,
        capital,
        poblacion,
        superficie,
        region,
        dato_curioso
    FROM informacion_provincia
    WHERE provincia_id = ?
    """, (provincia_id,))

    return cursor.fetchone()

def actualizar_imagen_provincia(
    provincia_id,
    nombre_imagen
):

    cursor.execute("""
    UPDATE provincias
    SET imagen = ?
    WHERE id = ?
    """, (
        nombre_imagen,
        provincia_id
    ))

    conexion.commit()