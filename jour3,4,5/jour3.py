import mysql.connector
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox 

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

def add_product():
    """FUNCTION FOR ADD MORE PRODUCT"""
    def submit_product():
        name = entry_name.get()
        description = entry_description.get()
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())
        category_id = int(entry_category.get())
        mydb = mysql.connector.connect (
            host = "localhost",
            user = "root",
            password = "",
            database = "store"
        )
        cursor = mydb.cursor()
        requete = "INSERT INTO product (Name, Description, Price, Quantity, ID_Category) VALUES(%s, %s, %s, %s, %s)"
        cursor.execute(requete, (name, description, price, quantity, category_id))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Success", "Product added successfully!")
        top.destroy()
        refresh_tree()

    top = tk.Toplevel(root)
    top.title("Add Product")
#new window for entering the information of the product
    tk.Label(top, text="Name").grid(row=0, column=0)
    entry_name = tk.Entry(top)
    entry_name.grid(row=0, column=1)

    tk.Label(top, text="Description").grid(row=1, column=0)
    entry_description = tk.Entry(top)
    entry_description.grid(row=1, column=1)

    tk.Label(top, text="Price").grid(row=2, column=0)
    entry_price = tk.Entry(top)
    entry_price.grid(row=2, column=1)

    tk.Label(top, text="Quantity").grid(row=3, column=0)
    entry_quantity = tk.Entry(top)
    entry_quantity.grid(row=3, column=1)

    tk.Label(top, text="ID_Category").grid(row=4, column=0)
    entry_category = tk.Entry(top)
    entry_category.grid(row=4, column=1)

    tk.Button(top, text="Submit", command=submit_product).grid(row=5, column=0, columnspan=2)

def refresh_tree():
    for row in tree.get_children():
        tree.delete(row)
    for row in fetch_data():
        tree.insert("", "end", values=row)

def modify_product():
    """FUNCTION FOR MODIFY THE PRODUCT"""
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a product to modify.")
        return

    item_values = tree.item(selected_item)["values"]
    product_id = item_values[0]
    product_price = item_values[3]
    product_quantity = item_values[4]

    def submit_modification():
        new_price = float(entry_price.get())
        new_quantity = int(entry_quantity.get())
        mydb = mysql.connector.connect (
            host ="localhost",
            user = "root",
            password = "",
            database = "store"
        )
        cursor = mydb.cursor()
        requete = "UPDATE product SET Price = %s, Quantity = %s WHERE ID = %s"
        cursor.execute(requete, (new_price, new_quantity, product_id))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Success", "Product modified successfully!")
        top.destroy()
        refresh_tree()

    top = tk.Toplevel(root)
    top.title("Modify Product")

    tk.Label(top, text="Price").grid(row=0, column=0)
    entry_price = tk.Entry(top)
    entry_price.insert(0, product_price)
    entry_price.grid(row=0, column=1)

    tk.Label(top, text="Quantity").grid(row=1, column=0)
    entry_quantity = tk.Entry(top)
    entry_quantity.insert(0, product_quantity)
    entry_quantity.grid(row=1, column=1)

    tk.Button(top, text="Submit", command=submit_modification).grid(row=2, column=0, columnspan=2)

def delete_product():
    """FUNCTION FOR DELETE A PRODUCT"""
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a product to delete.")
        return

    item_values = tree.item(selected_item)["values"]
    product_id = item_values[0]

    def confirm_delete():
        mydb = mysql.connector.connect (
            host ="localhost",
            user = "root",
            password = "",
            database = "store"
        )
        cursor = mydb.cursor()
        requete = "DELETE FROM product WHERE ID = %s"
        cursor.execute(requete, (product_id,))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Success", "Product deleted successfully!")
        refresh_tree()

    if messagebox.askokcancel("Delete", "Are you sure you want to delete this product?"):
        confirm_delete()

root = tk.Tk()
root.geometry("750x500")
root.title("inventory management")

style = ttk.Style()
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
style.configure("Treeview", font=("Helvetica", 10))

frame = tk.Frame(root)
frame.pack(pady=10)

tree = ttk.Treeview(frame, columns=("ID", "Name", "Description", "Price", "Quantity", "ID_Category"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Description", text="Description")
tree.heading("Price", text="Price")
tree.heading("Quantity", text="Quantity")
tree.heading("ID_Category", text="ID_Category")

tree.column("ID", width=50)
tree.column("Name", width=150)
tree.column("Description", width=250)
tree.column("Price", width=100)
tree.column("Quantity", width=100)
tree.column("ID_Category", width=100)

for row in fetch_data():
    tree.insert("", "end", values=row)
tree.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)


button_add = tk.Button(button_frame, text="ADD", command=add_product, bg="green", fg="white", font=("Helvetica", 10, "bold"))
button_modify = tk.Button(button_frame, text="MODIFY", command=modify_product, bg="blue", fg="white", font=("Helvetica", 10, "bold"))
button_delete = tk.Button(button_frame, text="DELETE", command=delete_product, bg="red", fg="white", font=("Helvetica", 10, "bold"))

button_add.grid(row=0, column=0, padx=10)
button_modify.grid(row=0, column=1, padx=10)
button_delete.grid(row=0, column=2, padx=10)

root.mainloop()
