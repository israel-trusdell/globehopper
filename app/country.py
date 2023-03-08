#Define all funtions related to country APIs

from flask import Flask,request,jsonify
import services

#
def createCountry(data):
    services.createCountry(data)
    return jsonify({'message' : 'Data insterted successfully'})

#Get all countires
def getCountries():
    results = services.allCounties()

    #Using a for loop to jsonify the list/dict
    data = []
    for row in results:
        data.append({
            "CountryId" : row[0],
            "Name" : row[1],
            "Population" : row[2],
            "Continent" : row[3]
        })
    return jsonify(data)

#Finciton to get all counties in a continent 
def getContinent():
    return