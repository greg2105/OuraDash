import requests
import os
from dotenv import load_dotenv

load_dotenv()

OURA_API_KEY = os.getenv('OURA_API_KEY')

headers = {
    "Authorization": f"Bearer {OURA_API_KEY}"
}

endpoints = {
    "sleep": "https://api.ouraring.com/v2/usercollection/sleep",
    "activity": "https://api.ouraring.com/v2/usercollection/activity",
    "readiness": "https://api.ouraring.com/v2/usercollection/readiness",
    "heart_rate": "https://api.ouraring.com/v2/usercollection/heart_rate"
}

def fetch_data(endpoint):
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
for category, url in endpoints.items():
    print(f"Fetching {category} data...")
    data = fetch_data(url)
    if data:
        print(data)
