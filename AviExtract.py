import os
from dotenv import load_dotenv 
import requests
import json 
import pandas as pd


load_dotenv()

api_key = os.getenv("AVIATIONSTACK_API_KEY")

print("API is loaded: ",api_key is not None)

url = "http://api.aviationstack.com/v1/flights"

limit = 100
offset =  0
target_records  = 500

flight_data = []

while len(flight_data)<target_records:

    response = requests.get(url, params= {"access_key" : api_key , "limit": limit, "offset": offset})
    response.raise_for_status()
    data =  response.json()

    flights = data["data"]

    for flight in flights:

        record = {

        "flight_date": flight["flight_date"],
        "flight_status" : flight["flight_status"],
        "airline_name": flight["airline"]["name"],
        "departure" : flight["departure"]["iata"],
        "arrival": flight["arrival"]["iata"],
        "flight_iata": flight["flight"]["iata"]
        } 

        flight_data.append(record)

    offset += limit

    with open("flights.json", "w") as file:
        json.dump(flight_data,file,indent=4)

print("data extracted successfully and savedcl")
print("Data extracted successfully and saved.")
print("Total records saved:", len(flight_data))