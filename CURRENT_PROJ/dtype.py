def col_dtype(col_name, col_data):
    l = len(col_data)
    # char = 1
    # int = 2
    # float = 3
    dtype = 0  # 0 if all values are null

    for i in range(0, l):
        if str(type(col_data[i])) == "<class 'str'>":
            dtype = 1
        
        if str(type(col_data[i])) == "<class 'int'>":
            if dtype == 0:
                dtype = 2
        if str(type(col_data[i])) == "<class 'float'>":
            if dtype == 0 or dtype ==2: 
                dtype = 3

    return list((col_name, dtype))

# test cases
#print(col_dtype(1,"Test1", [3,4,5,2,4,7,3,5,7,2.08,5,7,7,"meow"]))