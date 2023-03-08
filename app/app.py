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
def createcountryapp():
    data = request.json
    return country.createcountry(data)

#Read API
@app.get('/countries')
def getallcountriesapp():
    return country.getcountries()

#Put API
@app.put('/countries/<int:country_id>')
def updatecountryapp(country_id):
    data = request.json
    return country.updatecountry(data,country_id)

#Delete API
@app.delete('/countries/<int:country_id>') #Query string parameter
def deletecountryapp(country_id):
    return country.deletecountry(country_id)

#Get Cites
#Read API
@app.get('/city')
def getallcitiesapp():
    return city.getcities()
#Post Cities
#Create City- POST API
@app.post('/city')
def createcityapp():
    data = request.json
    return city.createcity(data)
#Put Cities
@app.put('/city/<int:city_id>')
def updatecityapp(city_id):
    data = request.json
    return city.updatcity(data,city_id)
#Delete Citie

#------------------

#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)
