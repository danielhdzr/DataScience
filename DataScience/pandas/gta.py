import sqlite3
import os

# Directorio del script
script_directory = os.path.dirname(os.path.abspath(__file__))
# Guardo archivo en directorio del script
db_file = os.path.join(script_directory, "gta.db")
# Conecto a mi nuevo archivo
connection = sqlite3.connect(db_file)
# Creo mi cursor
cursor = connection.cursor()

#Para crear la tabla desde cero /year, name, city/ columnas
cursor.execute("CREATE TABLE gta (year INTEGER, name TEXT, city TEXT)") # (col. Type)
# lista con tres columnas de values
release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]  
#"?" placeholder para los datos de la lista (un ? por cada columna)
cursor.executemany("INSERT INTO gta VALUES (?,?,?)", release_list)

# Print data base rows
for row in cursor.execute("SELECT * FROM gta"): # selecciona todos los rows
    print(row)
print("**********")
# Imprime el row donde la columna city == al valor de 'c' = Liberty City
cursor.execute("SELECT * FROM gta WHERE city = :c", {"c": "Liberty City"}) # Se define 'c' aqui mismo
# Toma todas las coincidencias
gta_search = cursor.fetchall()
print(gta_search)
print("**********")

cursor.execute("CREATE TABLE cities (gta_city TEXT, real_city TEXT)")
# En los placeholder pones los datos o variables que quieras. Aqui son datos
cursor.execute("INSERT INTO cities VALUES (?,?)",("Liberty City", "New York"))
cursor.execute("SELECT * FROM cities WHERE gta_city = :c", {"c": "Liberty City"})
cities_search = cursor.fetchall()
print(cities_search)
print("**********")
# Accedo a los datos guardados en la variable
# Si imprimo me puedo ver que Liberty city esta en la fila 0, col. 0. y New York en fila 0, col. 1
# Reemplazo Liberty city (fila 0, col. 0) con New York (fila 0, col. 1)
# Si el valor encontrado en ([row], [col.]) es liberty city, se reemplaza con new york
for i in gta_search:
    adjusted = [cities_search[0][1] if value == cities_search[0][0] else value for value in i]
    print(adjusted)


connection.commit()

connection.close()