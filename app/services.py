#Define all services for Country and City
 
from flask import Flask, request, jsonify
import conn



#Get all records from country table using SQL
def allCounties():

    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL 
    mycursor.execute("SELECT * FROM Country")
    results = mycursor.fetchall()

    #Close connection
    mycursor.close()
    conn.myconn.close()
    return results