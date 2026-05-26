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