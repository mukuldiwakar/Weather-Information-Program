import requests
#api key to get data 
api_key = "7819563d4185fb76940a00568d57c251"
#website url
url = 'http://api.openweathermap.org/data/2.5/weather'
#input for city
city_name = input("Enter city: ")
#settinng parameter in dict
parameters = {'q': city_name, 'appid': api_key}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    data = response.json()

    # Extracting relevant weather information
    weather_description = data['weather'][0]['description']
    
    feels_like = data['main']['feels_like']
    feels_like_cel =round(feels_like-273.15)
    
    temperature = data['main']['temp']
    temperature_cel=round(temperature-273.15)
    
    humidity = data['main']['humidity']

    # Displaying the weather information
    print(f"City: {city_name}")
    print(f"Weather Description: {weather_description}")
    print(f"Feels Like: {feels_like_cel} C°")
    print(f"Temperature: {temperature_cel} C°")
    print(f"Humidity: {humidity}%")
else:
    print(f"Request failed with status code: {response.status_code}")
