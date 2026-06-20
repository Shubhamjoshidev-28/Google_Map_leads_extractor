import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("SERP_API")

def extractor(q):
  params = {
      "engine": "google_maps",
      "q": q,
      "api_key": API_KEY
  }
  
  response = requests.get(
      "https://serpapi.com/search.json",
      params=params
  )
  
  data = response.json()
  
  with open("data/raw_data.json", "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4)
  
  return "JSON saved"