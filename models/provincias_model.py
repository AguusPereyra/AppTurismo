from database.db import cursor

def obtener_provincia_por_nombre(nombre):

    cursor.execute("""

    SELECT id, nombre

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