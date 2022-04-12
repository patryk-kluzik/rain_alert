import requests

API_KEY = "a0468448a07475040abfad57749f4a33"
api_call = "https://api.openweathermap.org/data/2.5/onecall"
my_lat = 52.399137
my_lon = -1.520814
exclude = "current,minutely,daily"

will_rain = None

parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "exclude": exclude,
    "appid": API_KEY,
}

response = requests.get(url=api_call, params=parameters)
response.raise_for_status()
data = response.json()

hourly_data_12_hours = data["hourly"][:12]

weather_codes_for_12_hours = [codes["weather"][0] for codes in hourly_data_12_hours]

when_to_bring_umbrella = {}
for index, hour_data in enumerate(weather_codes_for_12_hours):
    if hour_data["id"] < 600:
        bring_umbrella = True
        when_to_bring_umbrella[index] = hour_data["id"]

if when_to_bring_umbrella:
    print("it's going raining")
    print(list(when_to_bring_umbrella.keys()))
else:
    print("it isn't going to rain")
