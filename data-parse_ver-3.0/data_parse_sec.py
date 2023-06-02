import xlrd
import mysql.connector
from tkinter.filedialog import askopenfilename
import tkinter as tk

# location of file
# loc = "C:\\Users\\mathe\\Desktop\\student.xls"

# loc = "C:\\Rachel\\Consolidated Prize SS person added.xls"

# loc = input("Enter file directory\n")
# loc = loc[1:-1]

loc = None


def choose():
    filename = askopenfilename()
    # show an "Open" dialog box and return the path to the selected file
    # print(filename)
    global loc
    loc = filename


m = tk.Tk()
m.geometry("600x400")
pwd_var = tk.StringVar(m)
dtb_var = tk.StringVar(m)

m.title("Excel to MySQL")
# button = tk.Button(m, text = "click me!")
# button.pack()

# To print
label = tk.Label(
    text="Choose your excel file",
    fg="black",
    bg="white",
    font=('Calibre', 20, 'bold')
)
label.grid(row=1, column=1)
button = tk.Button(m, text="Choose file", width=25, command=choose)
button.grid(row=2, column=1)

pwd_name = tk.Label(m, text='Enter root password:')
pwd_entry = tk.Entry(m, textvariable=pwd_var)

dtb_name = tk.Label(m, text='Enter Database name:')
dtb_entry = tk.Entry(m, textvariable=dtb_var)

# dtb = ndb_var.get()
# print(ndb_var)

pwd_name.grid(row=5, column=0)
pwd_entry.grid(row=5, column=1)
dtb_name.grid(row=6, column=0)
dtb_entry.grid(row=6, column=1)

b2 = tk.Button(m, text="Close window", width=15, command=m.destroy)
b2.grid(row=5, column=2)
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)


m.mainloop()
pwd = pwd_var.get()
dtb = dtb_var.get()

# print(loc)
# print(pwd)
# print(dtb)

# connecting to sql database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pwd,
    database=dtb
)

mycursor = mydb.cursor()

# to open workbook
wb = xlrd.open_workbook(loc)
sheet_num = wb.nsheets
m = 0
for m in range(0, sheet_num):

    sheet = wb.sheet_by_index(m)

    col = sheet.ncols
    rows = sheet.nrows

    # To retrieve sheet name
    sheet_n = str(sheet)
    print(sheet_n)
    print(col, " columns,")
    print(rows, " rows.")
    sheet_n = sheet_n.lower()
    sheet_n = sheet_n.replace(" ", "_")
    sheet_n = sheet_n[10:-1]

    # To create table with only first column in it, other columns to be altered in later
    f_name = str(sheet.cell_value(0, 0))
    f_name = f_name.replace(" ", "_")
    f_name = f_name.replace(".", "_")
    cmd_table = "CREATE TABLE " + sheet_n + " (" + f_name + " VARCHAR(100))"
    # print(cmd_table)
    mycursor.execute(cmd_table)

    # To add the rest of the columns
    i = 1
    for i in range(1, col):
        f_name = str(sheet.cell_value(0, i))
        f_name = f_name.replace(" ", "_")
        f_name = f_name.replace(".", "_")
        cmd_table = "ALTER TABLE " + sheet_n + " ADD (" + f_name + " VARCHAR(100))"
        # print(cmd_table)
        mycursor.execute(cmd_table)
    print("Created Table " + sheet_n)
    # To create a string that has all the columns
    str1 = ""
    i = 0
    for i in range(0, col):
        cell = str(sheet.cell_value(0, i))
        cell = cell.replace(" ", "_")
        cell = cell.replace(".", "_")
        if i == (col - 1):
            str1 = str1 + cell
        else:
            str1 = str1 + cell + ", "

    # To add data into the rows
    i = 1
    val = ""
    temp = ""
    j = 0
    for i in range(1, rows):
        for j in range(0, col):
            if sheet.cell_value(i, j) == "":
                temp = "NULL"
            else:
                temp = "\"" + str(sheet.cell_value(i, j)) + "\""
            if j == (col - 1):
                val = val + temp
            else:
                val = val + temp + ", "
        j = 0
        cmd_f_table = "INSERT INTO " + sheet_n + " (" + str1 + ") VALUES (" + val + ")"
        # print(cmd_f_table)
        mycursor.execute(cmd_f_table)
        mydb.commit()
        # print("1 record inserted, ID:", mycursor.lastrowid)
        val = ""
    print(i, " records inserted in table " + sheet_n)

done = input("Program has finished running successfully!!\n Hit any key to exit...\n")
