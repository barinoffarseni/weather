
import os
from dotenv import load_dotenv 
import requests

load_dotenv()


city = os.getenv('CITY')
key = os.getenv('KEY')

url = 'http://api.weatherstack.com/current?query=' + city + '&access_key=' + key + '&units=m'

print(url)

res = requests.get(url)
print(res.text)
json = res.json()
print(json["current"]["observation_time"])
print(json["current"]["temperature"])
print(json["request"]["query"])
