import xlrd
import mysql.connector
import pandas as pd
import mods


def dtc(loc, hostname, username, pwd, dtb):
    # location of the file
    # loc = None


    display_text = ""

    try:
        '''
        hostname = None     #all these variables are required to connect to the mysql server
        username = None
        pwd = None
        dtb = None
        '''
        """

        Here should be GUI functions for retrieving filepath from user and assinging to variable 'loc' 
        Also retrieve the host, user, pwd and dtb (important for mysql connection)

        """
        # testing with values
        # pwd = "Dana2606"   #use your password when testing on your machine
        # dtb = "testing"

        mydb = mysql.connector.connect(
                host=hostname,  # for testing use host as "localhost"
                # host = "localhost", #for test
                user=username,  # for testing use user as "root"
                # user = "root",
                password=pwd,
                database=dtb
            )

        mycursor = mydb.cursor()

        # to open workbook
        wb = xlrd.open_workbook(loc)     # wb is file object
        # wb = xlrd.open_workbook('/Volumes/Data/Daniel/Data Converter/CURRENT_PROJ/test_wb.xls')      #for testing, change as per your local machine

        sheet_num = wb.nsheets              # sheet_num is number of sheets in excel file
        sheet_names = wb.sheet_names()      # sheet_n stores names of the sheets
        # print(sheet_n)

        m = 0       # variable used for iterating through the sheets in excel file
        i = 0       # variable used for iterating through column names
        dtype = 0   # variable used for determining column datatype
        ite = 1     # variable used for iteration control

        temp_table = pd.DataFrame()     # for temporarily holding the table in a dataframe
        cell_val = []                   # for temporarily holding the cell value
        cmd_table = None  # to store the sql command
        col_str = None                  # to store string of column names
        row_val = None                  # to store row strings

        for m in range(0, sheet_num):  # for iterating through all the sheets

            # 'sheet' will hold the sheet in that iteration
            sheet = wb.sheet_by_index(m)

            col = sheet.ncols       # stores number of columns in the sheet
            rows = sheet.nrows      # stores number of rows in the sheet

            sheet_n = str(sheet_names[m])       # To retrieve sheet name

            # print("\n\n\n",sheet_n)      # sheet_n is the table name
            # print(col, " columns,")
            # print((rows-1), " rows.")

            # To make the table name safe for mysql
            sheet_n = sheet_n.lower()
            # replaces whitespace with underscore
            sheet_n = sheet_n.replace(" ", "_")
            # replaces period with underscore
            sheet_n = sheet_n.replace(".", "_")
            # print(sheet_n)

            """
            Create a dataframe with all the table data
            """
            temp_table = mods.create_dataframe(col, rows, sheet)   # now temp_table holds a dataframe like the sheet in excel file
            # print(temp_table.columns.values.tolist())
            i = 0  # to iterate through columns and rows
            ite = 1  # to iterate create table function

            # CREATING TABLES
            # the list is a list of all column names in the temp_table dataframe
            for i in (temp_table.columns.values.tolist()):
                # checks the datatype of the column
                dtype = mods.col_dtype(temp_table[i])
                # print(i, dtype)
                # create the table creation commands
                cmd_table = mods.create_table(sheet_n, ite, i, dtype)
                # print(cmd_table)
                ite += 1
                # executes the table creation commands
                mycursor.execute(cmd_table)
                mydb.commit()
            # print("Created table:", sheet_n)

            # Now create a string of column names in the table
            col_str = ""
            for i in (temp_table.columns.values.tolist()):
                col_str = col_str + i+ str(", ")
                #print(col_str)
            col_str = col_str[0:-2]     # string of all columns

            # Now insert data from each row into table
            cmd_cell_table = None       # temporarily hold insert into statement for sql
            row_val = None              # temporarily hold row data
            for i in range(0, rows-1):
                row_val = mods.row_values_to_string(temp_table.iloc[i])
                cmd_cell_table = "INSERT INTO " + sheet_n + " (" + col_str + ") VALUES (" + row_val + ")"
                mycursor.execute(cmd_cell_table)
                mydb.commit()
                # print(cmd_cell_table)

            display_text = display_text+"\nCreated Table: " +str(sheet_n)+", "+str(rows-1)+" rows, "+str(col)+" columns."

        display_text = display_text+"\n\nData transferred succesfully."
        return display_text, ("Verdana", 9)
    except:
        display_text = "An Error occured. Please restart the program"
        return display_text, ("Verdana", 15)
