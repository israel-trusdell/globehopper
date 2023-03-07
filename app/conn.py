#Connect to mySQL Database

import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="ally",
    password="ALLY123$",
    db = "globehopperapp"
)