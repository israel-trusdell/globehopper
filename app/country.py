#Define all funtions related to country APIs

from flask import Flask,request,jsonify
import services

#Creating country record
def createcountry(data):
    services.createcountry(data)
    return jsonify({'message' : 'Country - Data insterted successfully'})

#Get all countires
def getcountries():
    results = services.allcountiesservices()

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

#Functions to update cuntry by id
def updatecountry(data,country_id):
    services.updatecountry(data,country_id)
    return jsonify({'message' : 'Country - Data updated successfully'})

#Function to delete a country
def deletecountry(country_id):
    services.deletecountrybyid(country_id)
    return jsonify({'message' : 'Country - Data successfully deleted'})

#Function to get a country by continent
def getcountrybycontinent(continent):
    results = services.countrybycontinentservices(continent)

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

#Get City info with Country name
def getcitybycapitalname(country_str,captial):
    results = services.getcapitalcitybycountryservices(country_str,captial)
    #Using a for loop to jsonify the list/dict
    data = []
    for row in results:
        data.append({
            "Country" : row[0],
            "Capital" : row[1],
            "FirstLandmark" : row[2],
            "SecondLandmark" : row[3],
            "ThirdLandmark" : row[4]
        })
    return jsonify(data)
