from pprint import pprint
import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{os.getenv('SHEETY_ID')}/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.bearer_headers = {"Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.bearer_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data, headers=self.bearer_headers
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_PRICES_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
