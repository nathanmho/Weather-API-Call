__author__ = 'Kai'

from pprint import pprint
import requests
import json
APIKey = "f5dfc4cfeadb862325cb3fe9fd4ad6e4"

def main():
    print(callWeatherAPI())



#Function to call the weather API and parse data.
def callWeatherAPI():
    #Basic call to openweather map. Need to extract temperature/blehbleh bleh take user input.
    #Change the params to take in user input later.
    weatherParams = {'APPID' : APIKey, 'q' : "London"}
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?', params = weatherParams)
    json_data = r.json()

    return json_data['main']['temp']





#Function to parse the user data.
def parseCallBackString():
    pass

main()








