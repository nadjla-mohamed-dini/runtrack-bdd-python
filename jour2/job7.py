import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "JamalMusiala42!",
    database = "entreprise"
)

cursor = mydb.cursor()
requete = "SELECT employe.nom, employe.prenom, employe.salaire, service.nom FROM employe JOIN service ON employe.id_service = service.id"
cursor.execute(requete)
employes_services = cursor.fetchall()
for employe_service in employes_services:
    print(employe_service)
cursor.close()
mydb.close()
