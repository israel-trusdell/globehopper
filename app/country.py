#Define all funtions related to country APIs

from flask import Flask,request,jsonify
import services

#Function to get all countries ans return as a JSON object
def getCountries():
    results = services.allCounties()
    return jsonify(results)