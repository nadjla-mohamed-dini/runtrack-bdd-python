import mysql.connector
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox 

def fetch_data():
    mydb = mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "JamalMusiala42!",
        database = "store"
    )
    cursor = mydb.cursor()
    requete = "SELECT * FROM product"
    cursor.execute(requete)
    rows = cursor.fetchall()
    mydb.close()
    return rows

def add_product():
    def submit_product():
        name = entry_name.get()
        description = entry_description.get()
        price = float(entry_price.get())
        quantity = int (entry_quantity.get())
        category_id = int(entry_category.get())
        mydb = mysql.connector.connect (
            host = "localhost",
            user = "root",
            password = "JamalMusiala42!",
            database = "store"
        )
        cursor = mydb.cursor()
        requete = "INSERT INTO product (Name, Description, Price, Quantity, ID_Category) VALUES(%s, %s, %s, %s, %s)"
        cursor.execute(requete, (name, description, price, quantity, category_id))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Succes", "product added successfullly")
        top.destroy()
        refresh_tree()
    top = tk.Toplevel(root)
    top.title("Add Product")

    tk.Label(top,text="Name").grid(row=1, column=0)
    entry_name = tk.Entry(top)
    entry_name.grid(row=0, column = 1)

    tk.Label(top,text="Description").grid(row=1, column=0)
    entry_description = tk.Entry(top)
    entry_description.grid(row=1, column=1)

    tk.Label(top,text="Price").grid(row=2, column=0)
    entry_price = tk.Entry(top)
    entry_price.grid(row=2, column=1)

    tk.Label(top, text="Quantity").grid(row=3, column=0)
    entry_quantity = tk.Entry(top)
    entry_quantity.grid(row=3, column=1)

    tk.Label(top,text="ID_Category").grid(row=4, column=0)
    entry_category = tk.Entry(top)
    entry_category.grid(row=4, column=1)

    tk.Button(top, text="Submit", command=submit_product).grid(row=5, column=0, columnspan=2)

def refresh_tree():
    for row in tree.get_children():
        tree.delete(row)
    for row in fetch_data():
        tree.insert("", "end", values=row)


root = tk.Tk()
root.geometry("750x500")
root.title("gestion des stocks")

tree = ttk.Treeview(root, columns=("ID","Name","Description","Price","Quantity","ID_Category"), show="headings")

tree.heading("ID",text="ID")
tree.heading("Name", text="Name")
tree.heading("Description",text="Description")
tree.heading("Price",text="Price")
tree.heading("Quantity",text="Quantity")
tree.heading("ID_Category",text="ID_Category")
for row in fetch_data():
    tree.insert("","end",values=row)
tree.pack()

button_add = tk.Button(root, text="ADD", command= add_product)
button_modify = tk.Button(root, text="MODIFY")
button_delete = tk.Button(root, text="DELETE")
button_add.place(x= 10, y= 350)
button_modify.place(x= 180, y=350)
button_delete.place(x=250, y= 350)

root.mainloop()