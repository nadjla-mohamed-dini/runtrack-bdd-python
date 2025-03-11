import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "JamalMusiala42!",
    database = "LaPlateforme"
)

cursor = mydb.cursor()
requete = "SELECT SUM(superficie) AS superficie_total FROM etage"
cursor.execute(requete)
result = cursor.fetchone()
superficie_total = result[0]
print(f"La superficie de La Plateforme est de {superficie_total} m² ")