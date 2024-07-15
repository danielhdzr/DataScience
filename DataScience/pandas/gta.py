import sqlite3
import os

# Directorio del script
script_directory = os.path.dirname(os.path.abspath(__file__))
# Guardo archivo en directorio del script
db_file = os.path.join(script_directory, "gta.db")

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

#Para crear la tabla desde cero /year, name, city/ columnas
cursor.execute("CREATE TABLE gta (year INTEGER, name TEXT, city TEXT)")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]  
#"?" placeholder para los datos de la lista
cursor.executemany("INSERT INTO gta VALUES (?,?,?)", release_list)

# Print data base rows
for row in cursor.execute("SELECT * FROM gta"):
    print(row)
print("**********")
# Imprime el row donde la columna city == "c" = Liberty City
cursor.execute("SELECT * FROM gta WHERE city = :c", {"c": "Liberty City"})
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
# Reemplazo Liberty city con New York
# Si el valor en cities_search[0][0], reemplazarlo con cities_search[0][1]
for i in gta_search:
    adjusted = [cities_search[0][1] if value == cities_search[0][0] else value for value in i]
    print(adjusted)


connection.commit()

connection.close()