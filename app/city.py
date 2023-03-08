#Define all funtions related to city APIs

from flask import Flask,request,jsonify
import services

#Create citiy record
def createcity(data):
    services.createcityservices(data)
    return jsonify({'message' : 'City - Data insterted successfully'})

#Get all cities
def getcities():
    results = services.allcitiesservices()
    #Using a for loop to jsonify the list/dict
    data = []
    for row in results:
        data.append({
            "CityId" : row[0],
            "Name" : row[1],
            "CountryId" : row[2],
            "Capital" : row[3],
            "FirstLandmark" : row[4],
            "SecondLandmark" : row[5],
            "ThirdLandmark" : row [6]
        })
    return jsonify(data)

#Function to update city by id
def updatcity(data, city_id):
    services.updatecityservices(data,city_id)
    return jsonify({'message' : 'City - Data updated successfully'})