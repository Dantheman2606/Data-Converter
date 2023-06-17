import xlrd
import mysql.connector
import pandas as pd
import create_table
import dtype
import create_dataframe

#location of the file
loc = None

hostname = None
username = None
pwd = None
dtb = None

"""

Here should be GUI functions for retrieving filepath from user and assinging to variable 'loc' 
Also retrieve the host, user, pwd and dtb (important for mysql connection)

"""
#testing with values
pwd = "Dana2606"   #use your password when testing on your machine
dtb = None
'''
mydb = mysql.connector.connect(
    #host = hostname,                    #for testing use host as "localhost"
    host = "localhost", #for test
    #user= username,                     #for testing use user as "root"
    user = "root",
    password=pwd,
    database=dtb
)

mycursor = mydb.cursor()
'''


# to open workbook
#wb = xlrd.open_workbook(loc)     # wb is file object 
wb = xlrd.open_workbook('/Volumes/Data/Daniel/Data Converter/CURRENT_PROJ/test_wb.xls')      #for testing, change as per your local machine

sheet_num = wb.nsheets          # sheet_num is number of sheets in excel file
sheet_names = wb.sheet_names()      # sheet_n stores names of the sheets
#print(sheet_n)

m = 0       #variable used for iterating through the sheets in excel file

temp_table = pd.DataFrame()    # for temporarily holding the table in a dataframe
cell_val = []      # for temporarily holding the 


for m in range(0, sheet_num):       #for iterating through all the sheets

    sheet = wb.sheet_by_index(m)        # 'sheet' will hold the sheet in that iteration

    col = sheet.ncols       # stores number of columns in the sheet
    rows = sheet.nrows      # stores number of rows in the sheet

    sheet_n = str(sheet_names[m])       # To retrieve sheet name

    print(sheet_n)
    print(col, " columns,")
    print((rows-1), " rows.")

    sheet_n = sheet_n.lower()                   # To make the table name safe for mysql
    sheet_n = sheet_n.replace(" ", "_")         # replaces whitespace with underscore
    sheet_n = sheet_n.replace(".", "_")         # replaces period with underscore
    #print(sheet_n)

    """
    Create a dataframe with all the table data
    """
    temp_table = create_dataframe.create_dataframe(col, rows, sheet)


    #this bottom part is now shifted to create_dataframe.py
    """
    for i in range (0, col):
        for j in range (1, rows):
            cell_val.append(sheet.cell_value(j, i))
            print(cell_val)
        temp_table[str(sheet.cell_value(0,i))] = cell_val
        print(cell_val)
        cell_val = []
    print(temp_table)

    temp_table = None
    temp_table = pd.DataFrame()
    """


    """
    Now we need to create a list of all column names.
    Then create a list of all data stored in that column
    """
  
    