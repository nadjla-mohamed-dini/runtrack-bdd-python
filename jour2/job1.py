import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "JamalMusiala42!",
    database = "LaPlateforme"
)

cursor = mydb.cursor()
requete = "SELECT * FROM etudiant"
cursor.execute(requete)
etudiants = cursor.fetchall()
for etudiant in etudiants:
    print(etudiant)
cursor.close()
mydb.close()

