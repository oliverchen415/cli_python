import requests
import click
import os
import requests
from dotenv import load_dotenv
load_dotenv()

@click.command()
@click.argument('location', default='San Francisco, CA')
def current_weather(location, api_key=os.getenv('API_KEY')):
    url = 'https://api.openweathermap.org/data/2.5/forecast?'

    query_params = {
        'q': location,
        'appid': api_key,
        'units':'imperial'
    }

    response = requests.get(url, params=query_params)
    description = response.json()['list'][0]['weather'][0]['description']
    temp = response.json()['list'][0]['main']['temp']
    print(f'The current temperature in {location} is {temp}°F.')
    print(f'The current weather condition is: {description}.')

if __name__ == '__main__':
    current_weather()