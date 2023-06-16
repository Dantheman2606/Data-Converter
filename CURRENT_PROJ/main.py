import xlrd
import mysql.connector
import pandas as pd

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
pwd = "Dana2606"
dtb = None

mydb = mysql.connector.connect(
    #host = hostname,                    #for testing use host as "localhost"
    host = "localhost", #for test
    #user= username,                     #for testing use user as "root"
    user = "root",
    password=pwd,
    database=dtb
)

mycursor = mydb.cursor()