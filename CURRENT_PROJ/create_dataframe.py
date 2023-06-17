import pandas as pd

"""
Here data from the sheet is converted into a dataframe and returned to the main program.
"""

def create_dataframe(col, rows, sheet):
    cell_val = []
    temp_table = pd.DataFrame()
    for i in range (0, col):
        for j in range (1, rows):
            cell_val.append(sheet.cell_value(j, i))
            #print(cell_val)
        temp_table[str(sheet.cell_value(0,i))] = cell_val
        #print(cell_val)
        cell_val = []
    print(temp_table)
    return temp_table