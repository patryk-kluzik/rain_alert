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

codes_to_bring_umbrella = [code["id"] for code in weather_codes_for_12_hours if code["id"] < 600]

if not codes_to_bring_umbrella:
    print("not raining")
else:
    print("its raining")