#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request,jsonify
import country
import city


#Using Flask framwork
app = Flask(__name__)

#------APIs--------
#Create - POST API
@app.post('/countries')
def createCountry():
    data = request.json
    return country.createCountry(data)

#Read API
@app.get('/countries')
def getAllCountries():
    return country.getCountries()

#Put API
@app.put('/countries/<int:country_id>')
def updatecountry(country_id):
    data = request.json
    return country.updatecountry(data,country_id)

#Delete API
@app.delete('/countries/<int:country_id>') #Query string parameter
def deletecountry(country_id):
    return country.deletecountry(country_id)

#Get Cites
#Read API
@app.get('/city')
def getallcities():
    return city.getcities()
#Post Cities
#Create City- POST API
@app.post('/city')
def createcity():
    data = request.json
    return city.createcity(data)
#Put Cities
#Delete Citie

#------------------

#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)
