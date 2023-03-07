#Connect to ySQL Database
#python -m pip install mysql-connector-python

import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="ally",
    password="ALLY123$",
    database="globehopperapp"
)