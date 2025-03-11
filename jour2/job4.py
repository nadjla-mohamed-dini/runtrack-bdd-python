import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "JamalMusiala42!",
    database = "LaPlateforme"
)

cursor = mydb.cursor()
requete = "SELECT capacite, nom FROM salle"
cursor.execute(requete)
salle_nom = cursor.fetchall()
for salle in salle_nom:
    print(salle)
cursor.close()
mydb.close()