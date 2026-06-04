from database.db import conexion, cursor

cursor.execute("""
CREATE TABLE IF NOT EXISTS provincias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS eventos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provincia_id INTEGER,
    nombre TEXT,
    fecha TEXT,
    lugar TEXT,
    imagen TEXT
)
""")
conexion.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS gastronomia(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provincia_id INTEGER,
    nombre TEXT
)
""")
conexion.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS turismo(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provincia_id INTEGER,
    nombre TEXT
)
""")
conexion.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS informacion_provincia(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provincia_id INTEGER,
    descripcion TEXT,
    capital TEXT,
    poblacion TEXT,
    superficie TEXT,
    region TEXT,
    dato_curioso TEXT
)
""")
conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Cordoba",))
provincia_existente = cursor.fetchone()
if not provincia_existente:
    cursor.execute("""
    INSERT INTO provincias(nombre)
    VALUES(?)
    """, ("Cordoba",))
    conexion.commit()

cursor.execute("""
SELECT * FROM eventos
WHERE nombre = ?
""", ("Cosquín Rock",))
evento_existente = cursor.fetchone()
if not evento_existente:
    cursor.execute("""
    INSERT INTO eventos(
        provincia_id,
        nombre,
        fecha,
        lugar,
        imagen
    )
    VALUES(
        1,
        "Cosquín Rock",
        "15 Febrero",
        "Santa María de Punilla",
        "cosquin.jpg"
    )
    """)
    conexion.commit()

cursor.execute("""
SELECT * FROM gastronomia
WHERE nombre = ?
""", ("Fernet",))
gastronomia_existente = cursor.fetchone()
if not gastronomia_existente:
    cursor.execute("""
    INSERT INTO gastronomia(
        provincia_id,
        nombre
    )
    VALUES(
        1,
        "Fernet"
    )
    """)
    conexion.commit()

cursor.execute("""
SELECT * FROM turismo
WHERE nombre = ?
""", ("Carlos Paz",))
turismo_existente = cursor.fetchone()
if not turismo_existente:
    cursor.execute("""
    INSERT INTO turismo(
        provincia_id,
        nombre
    )
    VALUES(
        1,
        "Carlos Paz"
    )
    """)
    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (1,))

info_existente = cursor.fetchone()

if not info_existente:

    cursor.execute("""
    INSERT INTO informacion_provincia(
        provincia_id,
        descripcion,
        capital,
        poblacion,
        superficie,
        region,
        dato_curioso
    )
    VALUES(
        1,
        'Córdoba es una de las provincias más importantes de Argentina, reconocida por sus sierras, su historia y su vida universitaria.',
        'Córdoba',
        '3.978.984 habitantes',
        '165.321 km²',
        'Región Centro',
        'La Universidad Nacional de Córdoba fue fundada en 1613 y es una de las más antiguas de América.'
    )
    """)

    conexion.commit()

cursor.execute("SELECT * FROM turismo")
print(cursor.fetchall())

cursor.execute("SELECT * FROM gastronomia")
print(cursor.fetchall())

cursor.execute("SELECT * FROM eventos")
resultado_eventos = cursor.fetchall()
print(resultado_eventos)

cursor.execute("SELECT * FROM provincias")
resultado = cursor.fetchall()
print(resultado)

cursor.execute("""
SELECT * FROM informacion_provincia
""")
print(cursor.fetchall())