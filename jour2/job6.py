import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "JamalMusiala42!",
    database = "LaPlateforme"
)

cursor = mydb.cursor()
requete = "SELECT SUM(capacite) AS capacite_total FROM salle"
cursor.execute(requete)
result = cursor.fetchone()
capacite_total = result[0]
print(f"La capacites de toutes les salles est de: {capacite_total}")