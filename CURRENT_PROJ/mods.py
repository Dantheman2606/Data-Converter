"""
Contains all our functions
"""
import pandas as pd
import math

# dtype function
def col_dtype(col_data):
    l = len(col_data)
    # char = 1
    # int = 2
    # float = 3
    dtype = 0  # 0 if all values are null
    #print(col_data)
    for i in range(0, l):
        #print(type(col_data[i]))
        if str(type(col_data[i])) == "<class 'str'>":
            dtype = 1
        
        if str(type(col_data[i])) == "<class 'numpy.int64'>":
            if dtype == 0:
                dtype = 2
        if str(type(col_data[i])) == "<class 'numpy.float64'>":
            if dtype == 0 or dtype ==2: 
                dtype = 3

    return dtype

# test cases
#print(col_dtype(1,"Test1", [3,4,5,2,4,7,3,5,7,2.08,5,7,7,"meow"]))


# create table function
def create_table(table_name, iteration, col_name, dtype):
    # char = 1 or 0
    # int = 2
    # float = 3

    table_name = table_name.lower()
    table_name = table_name.replace(" ", "_")
    table_name = table_name.replace(".", "_")

    col_name = col_name.lower()
    col_name = col_name.replace(" ", "_")
    col_name = col_name.replace(".", "_")
    if iteration == 1:

        if dtype == 1 or dtype == 0:
            cmd_table = "CREATE TABLE " +table_name+ " (" + col_name + " VARCHAR(100))"

        if dtype == 2:
            cmd_table = "CREATE TABLE " +table_name+ " (" + col_name + " INT)"

        if dtype == 3:
            cmd_table = "CREATE TABLE " +table_name+ " (" + col_name + " FLOAT)"

    elif iteration > 1:
        if dtype == 1 or dtype == 0:
            cmd_table = "ALTER TABLE " + table_name + " ADD (" + col_name + " VARCHAR(100))"
        
        if dtype == 2:
            cmd_table = "ALTER TABLE " + table_name + " ADD (" + col_name + " INT)"

        if dtype == 3:
            cmd_table = "ALTER TABLE " + table_name + " ADD (" + col_name + " FLOAT)"
    
    return cmd_table

#testing
#print(create_table("first table", 4, "Col name", 3))
#hello hello hello

"""
Here data from the sheet is converted into a dataframe and returned to the main program.
"""

def create_dataframe(col, rows, sheet):
    cell_val = []
    temp_val = None
    temp_table = pd.DataFrame()
    for i in range (0, col):
        for j in range (1, rows):
            temp_val = sheet.cell_value(j, i)
            #convert to int if necessary
            if str(type(temp_val)) == "<class 'float'>":
                if temp_val == math.floor(temp_val):
                    temp_val = int(temp_val)

            cell_val.append(temp_val)
            #print(cell_val)
        temp_table[str(sheet.cell_value(0,i))] = cell_val
        #print(cell_val)
        cell_val = []
    #print(temp_table,"\n\n")
    return temp_table