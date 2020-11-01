import requests
import json

weather_service_url = "http://api.openweathermap.org/data/2.5/weather?q=harsefeld,de&units=metric&lang=de&appid={}"
api_key = ""

def get_json_weather_data():
    global api_key
    if not api_key:
        print("Trying to read openweathermap api key from file")
        with open('./beebox/weather_secret', 'r') as secret_file:
            api_key = secret_file.read()
        
    response = requests.get(weather_service_url.format(api_key))
    if (response.status_code == 200):
        return json.loads(response.content)
    else:
        print(response.status_code)
        print(response.reason)

def get_description():
    # example response:
    # {"coord":{"lon":9.5,"lat":53.45},"weather":[{"id":804,"main":"Clouds","description":"Bedeckt","icon":"04d"}],"base":"stations","main":{"temp":11.39,"feels_like":8.03,"temp_min":11.11,"temp_max":12,"pressure":1011,"humidity":87},"visibility":10000,"wind":{"speed":4.6,"deg":190},"clouds":{"all":100},"dt":1604221415,"sys":{"type":1,"id":1292,"country":"DE","sunrise":1604211688,"sunset":1604245774},"timezone":3600,"id":2910280,"name":"Harsefeld","cod":200}
    data = get_json_weather_data()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    temp_max = data["main"]["temp_max"]
    weather_descr = data["weather"][0]["description"]

    return "Die aktuelle Temperatur liegt bei {} Grad, gefühlt wie {} Grad. Das Wetter ist heute {} bei einer Tageshöchsttemperatur von {} Grad.".format(round(temp), round(feels_like), weather_descr, round(temp_max))



if __name__ == '__main__':
    description = get_description()
    print(description)