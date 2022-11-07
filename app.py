import requests
from flask import Flask, jsonify

EXCHANGE_URL = 'https://openexchangerates.org/api/latest.json?app_id=faef362592bf429cb11b3854acdd93e5'
EXCHANGE_PARAMS =  {'symbols':'ZAR,EUR,CAD'}

WEATHER_URL = 'http://api.weatherstack.com/current?access_key=e2c68d60db15956928648503cc99aca9'
WEATHER_PARAMS = {'query':'Cape Town'}

app = Flask(__name__) 

@app.route('/') # Create main page of web-application
def index():
    return "Welcome to my API!" # Display text on main page


@app.route('/get',methods=['GET']) # Add an endpoint to access our API
def get():
    exchange_data = requests.get(EXCHANGE_URL, EXCHANGE_PARAMS)  
    weather = requests.get(WEATHER_URL,params=WEATHER_PARAMS) 

    return jsonify({
        'usd_rates': exchange_data.json()['rates'],
        'curr_temp': weather.json()['current']['temperature']
    })


if __name__ == '__main__':
    app.run() # Run the application
