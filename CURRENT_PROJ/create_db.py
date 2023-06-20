"""
Creating a Databse, if User wants to create new DB.
This is a module to be used in the main program
"""
import mysql.connector
def db_to_use(var, hostname, username, pwd, dtb):
    if var == 1:
        mydb1 = mysql.connector.connect(
        host=hostname,
        user=username,
        password=pwd
        )
        mycursor = mydb1.cursor()
        mycursor.execute("CREATE DATABASE "+dtb)
        return dtb
    elif var == 0:
        return dtb
       