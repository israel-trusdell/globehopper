#Define all services for Country and City
 
from flask import Flask, request, jsonify
import conn

#------------Country-------------
#Create a country record
def createcountry(data):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Table columns
    countryid = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL 
    mysql = "INSERT INTO country (CountryId, Name, Population, Continent) VALUES (%s,%s,%s,%s);"
    values = (countryid, name, population,continent)
    mycursor.execute(mysql,values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Get all records from country table using SQL
def allcountiesservices():

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

#update country by id
def updatecountry(data,country_id):
#Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Table columns
    
    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL 
    mysql = "UPDATE country SET Name = %s, Population = %s, Continent = %s WHERE CountryId = %s;"
    values = (name, population,continent,country_id)
    mycursor.execute(mysql,values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#delete country by country_id
def deletecountrybyid(country_id):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL 
    sql = "DELETE FROM country WHERE CountryId = %s"
    mycursor.execute(sql, (country_id,))

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Get all countries in a given continent
def countrybycontinentservices(continent_str):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL 
    mycursor.execute("SELECT * FROM country WHERE Continent = %s",(continent_str,))
    results = mycursor.fetchall()

    #Close connection
    mycursor.close()
    conn.myconn.close()
    return results

#------------City---------------

#Create a country record
def createcityservices(data):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Table columns
    cityid = data['CityId']
    name = data['Name']
    countryid = data['CountryId']
    capital = data['Capital']
    firstlandmark = data['FirstLandmark']
    secondlandmark = data['SecondLandmark']
    thirdlandmark = data['ThirdLandmark']
    

    #Execute the SQL 
    mysql = "INSERT INTO city (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (%s,%s,%s,%s,%s,%s,%s);"
    values = (cityid, name, countryid,capital,firstlandmark,secondlandmark,thirdlandmark)
    mycursor.execute(mysql,values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Get all records from city table using SQL
def allcitiesservices():

    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL 
    mycursor.execute("SELECT * FROM city")
    results = mycursor.fetchall()

    #Close connection
    mycursor.close()
    conn.myconn.close
    return results

#update city by id
def updatecityservices(data,city_id):
#Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Table columns
    name = data['Name']
    countryid = data['CountryId']
    capital = data['Capital']
    firstlandmark = data['FirstLandmark']
    secondlandmark = data['SecondLandmark']
    thirdlandmark = data['ThirdLandmark']

    #Execute the SQL 
    mysql = "UPDATE city SET Name = %s, CountryId = %s, Capital = %s, FirstLandmark = %s, SecondLandmark = %s, ThirdLandmark = %s WHERE CityId = %s;"
    values = (name, countryid,capital,firstlandmark,secondlandmark,thirdlandmark,city_id)
    mycursor.execute(mysql,values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#delete city by city_id
def deleteccitybyidservices(city_id):
    #Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL 
    sql = "DELETE FROM city WHERE CityId = %s"
    mycursor.execute(sql, (city_id,))

    #Close connection
    mycursor.close()
    conn.myconn.close()