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