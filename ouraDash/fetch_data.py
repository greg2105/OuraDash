import requests
import os
from dotenv import load_dotenv

load_dotenv()

OURA_API_KEY = os.getenv('OURA_API_KEY')