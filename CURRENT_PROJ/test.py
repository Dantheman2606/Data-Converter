import xlrd
import mysql.connector
import pandas as pd
import mods
import create_db
import customtkinter as ctk
from tkinter.filedialog import askopenfilename

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")



#location of the file
loc = None

#testing with values
#pwd = "Dana2606"   #use your password when testing on your machine
#dtb = "testing"

root = ctk.CTk()
root.geometry("800x800")
root.title("Excel to MySQL")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

loc = None
hstn_var = ctk.StringVar(root)
usrn_var = ctk.StringVar(root)
pwd_var = ctk.StringVar(root)
dtb_var = ctk.StringVar(root)

def choose():
    filename = askopenfilename()
    # show an "Open" dialog box and return the path to the selected file
    # print(filename)
    global loc
    loc = filename
    display_file = ctk.CTkLabel(master=frame, text=loc)
    display_file.pack(padx=10, pady=10)

label1 = ctk.CTkLabel(master=frame, 
                    text="Data Transfer from Excel to MySQL", 
                    font=("Roboto", 26))
label1.pack(pady=12, padx=10)

file_choose = ctk.CTkButton(master=frame, 
                            text="Choose File", 
                            command=choose).pack()

label2 = ctk.CTkLabel(master=frame, 
                    text="MySQL Login", 
                    font=("Roboto", 20))
label2.pack(pady=12, padx=10)

label3 = ctk.CTkLabel(master=frame, 
                    text="Enter Hostname:", 
                    font=("Verdana", 16), 
                    text_color="grey")
label3.pack()
hostname = ctk.CTkEntry(master=frame, 
                        width=300, 
                        placeholder_text="Hostname", 
                        textvariable=hstn_var, 
                        font=("Verdana", 15))
hostname.pack(pady=12, padx=10)

label4 = ctk.CTkLabel(master=frame, 
                    text="Enter Username:", 
                    font=("Verdana", 16), 
                    text_color="grey")
label4.pack()
username = ctk.CTkEntry(master=frame, 
                        width=300, 
                        placeholder_text="Username", 
                        textvariable=usrn_var, 
                        font=("Verdana", 15))
username.pack(pady=12, padx=10)

label5 = ctk.CTkLabel(master=frame, 
                    text="Enter Database name:", 
                    font=("Verdana", 16), 
                    text_color="grey")
label5.pack()
database = ctk.CTkEntry(master=frame, 
                        width=300, 
                        placeholder_text="Database name", 
                        textvariable=dtb_var, 
                        font=("Verdana", 15))
database.pack(pady=12, padx=10)

label6 = ctk.CTkLabel(master=frame, 
                    text="Enter Password:", 
                    font=("Verdana", 16), 
                    text_color="grey")
label6.pack()
password = ctk.CTkEntry(master=frame, 
                        width=300, 
                        placeholder_text="Password", 
                        show = "*", 
                        textvariable=pwd_var, 
                        font=("Verdana", 15))
password.pack(pady=12, padx=10)

var = ctk.IntVar()
checkbox = ctk.CTkCheckBox(master=frame, text="Create New Database", variable=var)
checkbox.pack(pady=12, padx=10)

close = ctk.CTkButton(root, text="Close Window", width=10, command= root.destroy)
close.pack(padx=5, pady=5)

root.mainloop()

dtb = create_db.db_to_use(var.get(), 
                          hstn_var.get(), 
                          usrn_var.get(), 
                          pwd_var.get(), 
                          dtb_var.get())

mydb = mysql.connector.connect(
    host = hstn_var.get(),                    #for testing use host as "localhost"
    #host = "localhost", #for test
    user= usrn_var.get(),                     #for testing use user as "root"
    #user = "root",
    password=pwd_var.get(),
    database=dtb
)

mycursor = mydb.cursor()

# to open workbook
wb = xlrd.open_workbook(loc)     # wb is file object 
#wb = xlrd.open_workbook('/Volumes/Data/Daniel/Data Converter/CURRENT_PROJ/test_wb.xls')      #for testing, change as per your local machine

sheet_num = wb.nsheets              # sheet_num is number of sheets in excel file
sheet_names = wb.sheet_names()      # sheet_n stores names of the sheets
#print(sheet_n)

m = 0       # variable used for iterating through the sheets in excel file
i = 0       # variable used for iterating through column names
dtype = 0   # variable used for determining column datatype
ite = 1     # variable used for iteration control

temp_table = pd.DataFrame()     # for temporarily holding the table in a dataframe
cell_val = []                   # for temporarily holding the cell value
cmd_table = None                #to store the sql command
col_str = None                  # to store string of column names
row_val = None                  # to store row strings

for m in range(0, sheet_num):       #for iterating through all the sheets

    sheet = wb.sheet_by_index(m)        # 'sheet' will hold the sheet in that iteration

    col = sheet.ncols       # stores number of columns in the sheet
    rows = sheet.nrows      # stores number of rows in the sheet

    sheet_n = str(sheet_names[m])       # To retrieve sheet name
    '''
    print("\n\n\n",sheet_n)      # sheet_n is the table name
    print(col, " columns,")
    print((rows-1), " rows.")
    '''

    sheet_n = sheet_n.lower()                   # To make the table name safe for mysql
    sheet_n = sheet_n.replace(" ", "_")         # replaces whitespace with underscore
    sheet_n = sheet_n.replace(".", "_")         # replaces period with underscore
    #print(sheet_n)

    """
    Create a dataframe with all the table data
    """
    temp_table = mods.create_dataframe(col, rows, sheet)   # now temp_table holds a dataframe like the sheet in excel file
    #print(temp_table.columns.values.tolist())
    i = 0 # to iterate through columns and rows
    ite = 1 # to iterate create table function

    for i in (temp_table.columns.values.tolist()):    # the list is a list of all column names in the temp_table dataframe
        dtype = mods.col_dtype(temp_table[i])         # checks the datatype of the column
        #print(i, dtype)
        cmd_table = mods.create_table(sheet_n, ite, i, dtype)   # create the table creation commands
        #print(cmd_table)
        ite += 1
        mycursor.execute(cmd_table)                   # executes the table creation commands
        mydb.commit()
    #print("Created table:", sheet_n)

    # Now create a string of column names in the table
    col_str = ""
    for i in (temp_table.columns.values.tolist()):
        col_str = col_str+i+", "
    col_str = col_str[0:-2]     # string of all columns
    #print(col_str)

    # Now insert data from each row into table
    cmd_cell_table = None       # temporarily hold insert into statement for sql
    row_val = None              # temporarily hold row data
    for i in range(0, rows-1):
        row_val = mods.row_values_to_string(temp_table.iloc[i])
        cmd_cell_table = "INSERT INTO " + sheet_n + " (" + col_str + ") VALUES (" + row_val + ")"
        mycursor.execute(cmd_cell_table)
        mydb.commit()
        #print(cmd_cell_table)
        
#root.mainloop()
print("Data transferred succesfully.")
