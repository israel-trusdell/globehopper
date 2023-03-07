#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request,jsonify
import country

#Using Flask framwork
app = Flask(__name__)

#------APIs--------
#Read API
@app.get('/countries')
def getAllCountries():
    return country.getCountries()

#------------------

#Execute on the terminal
if __name__ == '__main__':
    app.run()
