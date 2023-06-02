import mysql.connector
import tkinter as tk

m = tk.Tk()
m.geometry("600x400")
m.title("Create New Database")
pwd_var = tk.StringVar(m)
dtb_var = tk.StringVar(m)

pwd_name = tk.Label(m, text = 'Enter root password:')
pwd_entry = tk.Entry(m, textvariable=pwd_var)

dtb_name = tk.Label(m, text ='Enter Database name:')
dtb_entry = tk.Entry(m, textvariable=dtb_var)

label = tk.Label(
    text="Create New Databse in MySQL Client",
    fg="black",
    bg="white",
    font=('Calibre',15, 'bold')
)

label.grid(row=1, column=1)
pwd_name.grid(row=2, column=0)
pwd_entry.grid(row=2, column=1)
dtb_name.grid(row=4, column=0)
dtb_entry.grid(row=4, column=1)

b2 = tk.Button(m, text="Close window", width=25, command=m.destroy)
b2.grid(row=5, column=1)

m.mainloop()
pwd = pwd_var.get()
dtb = dtb_var.get()

mydb1 = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd
)
print(pwd)
print(dtb)

mycursor = mydb1.cursor()

mycursor.execute("CREATE DATABASE "+dtb)