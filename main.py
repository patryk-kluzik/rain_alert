import requests
import datetime
import os
from twilio.rest import Client

TWILIO_NUMBER = '+12183001930'
MY_NUMBER = os.environ.get("MY_NUMBER")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


API_KEY = os.environ.get("API_KEY_OWM")
api_call = "https://api.openweathermap.org/data/2.5/onecall"
my_lat = 52.399137
my_lon = -1.520814
exclude = "current,minutely,daily"

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

current_hour = datetime.datetime.now().hour
when_to_bring_umbrella = {}
for index, hour_data in enumerate(weather_codes_for_12_hours):
    if hour_data["id"] < 600:
        bring_umbrella = True
        when_to_bring_umbrella[str(index + current_hour) + ":00"] = hour_data["id"]

list_hours = list(when_to_bring_umbrella.keys())

hours_str = ', '.join(list_hours)

last_char_index = hours_str.rfind(",")
hours_str = hours_str[:last_char_index] + " and" + hours_str[last_char_index + 1:]

if when_to_bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"It's going to rain today between {hours_str}!☂️",
        from_=TWILIO_NUMBER,
        to=MY_NUMBER
    )
    print(message.status)
