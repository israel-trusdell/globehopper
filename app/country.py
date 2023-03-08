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

#Finctions to update cuntry by id
def updatecountry(data,country_id):
    services.updatecountry(data,country_id)
    return jsonify({'message' : 'Data updated successfully'})

#Function to delete a country
def deletecountry(country_id):
    services.deletecountrybyid(country_id)
    return jsonify({'message' : 'Data successfully deleted'})