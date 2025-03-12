import mysql.connector

import tkinter as tk 

from tkinter import ttk

def fetch_data():
    mydb = mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "",
        database = "store"
    )
    cursor = mydb.cursor()
    requete = "SELECT * FROM product"
    cursor.execute(requete)
    rows = cursor.fetchall()
    mydb.close()
    return rows

root = tk.Tk()
root.title("gestion des stocks")

tree = ttk.Treeview(root, columns=("ID","Name","Description","Price","Quantity","ID Category"), show="headings")

tree.heading("ID",text="ID")
tree.heading("Name", text="Name")
tree.heading("Description",text="Description")
tree.heading("Price",text="Price")
tree.heading("Quantity",text="Quantity")
tree.heading("ID Category",text="ID Category")
bouton = tk.Button(root, text="ADD")
for row in fetch_data():
    tree.insert("","end",values=row)
tree.pack()
root.mainloop()