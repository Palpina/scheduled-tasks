import os
import requests
from twilio.rest import Client

OW_ENDPOINT= "https://api.openweathermap.org/data/2.5/forecast"
OW_API = os.getenviron.get("OPEN_WEATHER_API")
HB_LONG = 8.807982
HB_LAT = 53.075250
TW_ACC_SID = os.getenviron.get("TWILIO_SID")
TW_AUTH = os.getenviron.get("TWILIO_AUTH")
TO_NUMBER = os.getenviron.get("WA_RECIPIENT")
FROM_NUMBER = os.environ.get("WA_SENDER")


parameters = {
    "lat": HB_LAT,
    "lon": HB_LONG,
    "appid": OW_API,
    "units": "metric",
    "cnt": 4,
}


weather_response = requests.get(OW_ENDPOINT, params=parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()

will_rain = False
for forecast in weather_data["list"]:
    if forecast["weather"][0]["id"] < 700:
        will_rain = True        
if will_rain:
    tw_client = Client(TW_ACC_SID, TW_AUTH)
    whatsapp = tw_client.messages.create(body="Prepare: Rain today", to=f"whatsapp:{WA_RECIPIENT}", from_=f"whatsapp:{WA_SENDER}")
