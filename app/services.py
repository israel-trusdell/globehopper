#Define all services for Country and City
 
from flask import Flask, request, jsonify
import conn

#Create a country record
def createCountry(data):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Table columns
    countryId = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL 
    mysql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s,%s,%s,%s);"
    values = (countryId, name, population,continent)
    mycursor.execute(mysql,values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

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

