import sqlite3

conexion = sqlite3.connect(
    "base.db",
    check_same_thread=False
)

cursor = conexion.cursor()