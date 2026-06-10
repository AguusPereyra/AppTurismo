from database.db import conexion, cursor

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    rol TEXT NOT NULL
)
""")

conexion.commit()

cursor.execute("""
SELECT * FROM usuarios
WHERE email = ?
""", ("admin@appturismo.com",))

admin_existente = cursor.fetchone()

if not admin_existente:

    cursor.execute("""
    INSERT INTO usuarios(
        nombre,
        email,
        password,
        rol
    )
    VALUES(
        ?, ?, ?, ?
    )
    """, (
        "Administrador",
        "admin@appturismo.com",
        "123456",
        "ADMIN"
    ))

    conexion.commit()
















cursor.execute("""
CREATE TABLE IF NOT EXISTS provincias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    imagen TEXT
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
    INSERT INTO provincias(nombre, imagen)
    VALUES(?, ?)
    """, ("Cordoba", "cordoba.jpg"))
    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Mendoza",))
provincia_existente = cursor.fetchone()
if not provincia_existente:
    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Mendoza", "mendoza.jpg"))
    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Salta",))
provincia_existente = cursor.fetchone()
if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Salta", "salta.jpg"))

    conexion.commit()  

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Jujuy",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Jujuy", "jujuy.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Buenos Aires",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Buenos Aires", "buenos_aires.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Santa Fe",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Santa Fe", "santa_fe.jpg"))

    conexion.commit()  

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Rio Negro",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Rio Negro", "rio_negro.jpg"))

    conexion.commit()  

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Neuquen",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Neuquen", "neuquen.jpg"))

    conexion.commit()       

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Misiones",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Misiones", "misiones.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Chaco",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Chaco", "chaco.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Corrientes",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Corrientes", "corrientes.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Entre Rios",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Entre Rios", "entre_rios.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Formosa",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Formosa", "formosa.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("La Pampa",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("La Pampa", "la_pampa.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("La Rioja",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("La Rioja", "la_rioja.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("San Juan",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("San Juan", "san_juan.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("San Luis",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("San Luis", "san_luis.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Catamarca",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Catamarca", "catamarca.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Santiago del Estero",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Santiago del Estero", "santiago_del_estero.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Tucuman",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Tucuman", "tucuman.jpg"))

    conexion.commit()    

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Chubut",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Chubut", "chubut.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Santa Cruz",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Santa Cruz", "santa_cruz.jpg"))

    conexion.commit()

cursor.execute("""
SELECT * FROM provincias
WHERE nombre = ?
""", ("Tierra del Fuego",))

provincia_existente = cursor.fetchone()

if not provincia_existente:

    cursor.execute("""
    INSERT INTO provincias(
        nombre,
        imagen
    )
    VALUES(?, ?)
    """, ("Tierra del Fuego", "tierra_del_fuego.jpg"))

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

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (2,))

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
        2,
        'Mendoza es una provincia reconocida mundialmente por la producción de vinos y por sus paisajes cordilleranos.',
        'Mendoza',
        '2.014.533 habitantes',
        '148.827 km²',
        'Región de Cuyo',
        'En Mendoza se encuentra el Aconcagua, la montaña más alta de América con 6.961 metros de altura.'
    )
    """)

    conexion.commit()   

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (3,))

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
        3,
        'Salta es una provincia del noroeste argentino conocida por sus paisajes montañosos, su cultura andina y su arquitectura colonial.',
        'Salta',
        '1.440.672 habitantes',
        '155.488 km²',
        'Noroeste Argentino',
        'El famoso Tren a las Nubes alcanza más de 4.200 metros sobre el nivel del mar.'
    )
    """)

    conexion.commit()  

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (4,))

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
        4,
        'Jujuy se destaca por sus paisajes andinos, la Quebrada de Humahuaca y una fuerte herencia cultural indígena.',
        'San Salvador de Jujuy',
        '811.611 habitantes',
        '53.219 km²',
        'Noroeste Argentino',
        'La Quebrada de Humahuaca fue declarada Patrimonio de la Humanidad por la UNESCO.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (5,))

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
        5,
        'Buenos Aires es la provincia más poblada del país y concentra una gran diversidad de ciudades, industrias y destinos turísticos.',
        'La Plata',
        '17.569.053 habitantes',
        '307.571 km²',
        'Región Pampeana',
        'La Plata fue una de las primeras ciudades planificadas de América del Sur.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (6,))

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
        6,
        'Santa Fe es una de las provincias más importantes del país por su actividad agroindustrial y sus grandes ciudades.',
        'Santa Fe',
        '3.556.522 habitantes',
        '133.007 km²',
        'Región Centro',
        'En Rosario nació la bandera argentina, creada por Manuel Belgrano.'
    )
    """)

    conexion.commit()  

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (7,))

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
        7,
        'Río Negro combina la cordillera andina, lagos, valles productivos y la costa atlántica patagónica.',
        'Viedma',
        '762.067 habitantes',
        '203.013 km²',
        'Patagonia',
        'San Carlos de Bariloche es uno de los destinos turísticos más visitados de Argentina.'
    )
    """)

    conexion.commit()  

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (8,))

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
        8,
        'Neuquén es una provincia patagónica reconocida por sus paisajes naturales, el turismo y la producción energética.',
        'Neuquén',
        '726.590 habitantes',
        '94.078 km²',
        'Patagonia',
        'Vaca Muerta es una de las mayores reservas de petróleo y gas no convencional del mundo.'
    )
    """)

    conexion.commit()        

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (9,))

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
        9,
        'Misiones es famosa por sus selvas subtropicales, biodiversidad y las Cataratas del Iguazú.',
        'Posadas',
        '1.280.960 habitantes',
        '29.801 km²',
        'Mesopotamia',
        'Las Cataratas del Iguazú fueron elegidas como una de las Siete Maravillas Naturales del Mundo.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (10,))

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
        10,
        'Chaco es una provincia del norte argentino conocida por sus extensos bosques, parques nacionales y riqueza cultural.',
        'Resistencia',
        '1.142.963 habitantes',
        '99.633 km²',
        'Noreste Argentino',
        'Resistencia es conocida como la Ciudad de las Esculturas.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (11,))

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
        11,
        'Corrientes es una provincia del noreste argentino reconocida por sus tradiciones, el chamamé y los Esteros del Iberá.',
        'Corrientes',
        '1.197.553 habitantes',
        '88.199 km²',
        'Mesopotamia',
        'Los Esteros del Iberá son uno de los humedales más grandes del mundo.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (12,))

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
        12,
        'Entre Ríos se caracteriza por sus ríos, termas, paisajes naturales y una importante producción agropecuaria.',
        'Paraná',
        '1.426.426 habitantes',
        '78.781 km²',
        'Mesopotamia',
        'Posee más de 800 km de costa sobre los ríos Paraná y Uruguay.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (13,))

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
        13,
        'Formosa es una provincia del norte argentino con una gran biodiversidad y extensas áreas naturales protegidas.',
        'Formosa',
        '607.419 habitantes',
        '72.066 km²',
        'Noreste Argentino',
        'El Bañado La Estrella es uno de los mayores humedales de Sudamérica.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (14,))

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
        14,
        'La Pampa es una provincia de extensas llanuras, destacada por la actividad ganadera y agrícola.',
        'Santa Rosa',
        '366.022 habitantes',
        '143.440 km²',
        'Pampeana',
        'Es una de las provincias con menor densidad poblacional del país.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (15,))

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
        15,
        'La Rioja combina montañas, valles y sitios históricos, siendo una de las provincias más representativas del noroeste argentino.',
        'La Rioja',
        '393.531 habitantes',
        '89.680 km²',
        'Noroeste Argentino',
        'El Parque Nacional Talampaya es Patrimonio de la Humanidad.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (16,))

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
        16,
        'San Juan es conocida por sus paisajes cordilleranos, la producción vitivinícola y el turismo de aventura.',
        'San Juan',
        '818.234 habitantes',
        '89.651 km²',
        'Cuyo',
        'Es una de las principales provincias productoras de vino.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (17,))

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
        17,
        'San Luis destaca por sus sierras, embalses, espacios verdes y una infraestructura moderna.',
        'San Luis',
        '540.905 habitantes',
        '76.748 km²',
        'Cuyo',
        'Es reconocida por sus modernas autopistas y espacios verdes.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (18,))

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
        18,
        'Catamarca es una provincia montañosa famosa por sus paisajes naturales, volcanes y riqueza minera.',
        'San Fernando del Valle de Catamarca',
        '429.562 habitantes',
        '102.602 km²',
        'Noroeste Argentino',
        'Posee algunos de los volcanes más altos del planeta.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (19,))

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
        19,
        'Santiago del Estero es una de las provincias con mayor historia del país y una fuerte identidad cultural.',
        'Santiago del Estero',
        '1.054.028 habitantes',
        '136.351 km²',
        'Norte Grande',
        'Es considerada la ciudad más antigua fundada por españoles en Argentina.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (20,))

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
        20,
        'Tucumán es la provincia más pequeña de Argentina y un lugar clave en la historia de la independencia nacional.',
        'San Miguel de Tucumán',
        '1.703.186 habitantes',
        '22.524 km²',
        'Noroeste Argentino',
        'Allí se declaró la Independencia Argentina en 1816.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (21,))

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
        21,
        'Chubut ofrece paisajes patagónicos únicos, fauna marina y algunos de los destinos naturales más importantes del país.',
        'Rawson',
        '618.994 habitantes',
        '224.686 km²',
        'Patagonia',
        'Península Valdés es uno de los mejores lugares del mundo para observar ballenas.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (22,))

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
        22,
        'Santa Cruz es una provincia patagónica de grandes extensiones, glaciares y paisajes de enorme valor natural.',
        'Río Gallegos',
        '337.226 habitantes',
        '243.943 km²',
        'Patagonia',
        'El Glaciar Perito Moreno es uno de sus mayores atractivos turísticos.'
    )
    """)

    conexion.commit()

cursor.execute("""
SELECT * FROM informacion_provincia
WHERE provincia_id = ?
""", (23,))

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
        23,
        'Tierra del Fuego es la provincia más austral de Argentina, famosa por sus montañas, bosques y canales fueguinos.',
        'Ushuaia',
        '190.641 habitantes',
        '21.571 km²',
        'Patagonia',
        'Ushuaia es considerada la ciudad más austral del mundo.'
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

cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())

cursor.execute("""
SELECT dato_curioso
FROM informacion_provincia
WHERE provincia_id = 1
""")

print(cursor.fetchone())