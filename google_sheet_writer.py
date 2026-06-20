import json
import gspread
from google.oauth2.service_account import Credentials

def google_sheet_writer():

   SCOPES = [
       "https://www.googleapis.com/auth/spreadsheets",
       "https://www.googleapis.com/auth/drive"
   ]
   
   creds = Credentials.from_service_account_file(
       "credentials.json",
       scopes=SCOPES
   )
   
   client = gspread.authorize(creds)
   
   sheet = client.open("leads").sheet1
   
   with open(
       "data/business.json",
       "r",
       encoding="utf-8"
   ) as file:
       businesses = json.load(file)
   
   for business in businesses:
   
       sheet.append_row([
           business.get("business_name", ""),
           business.get("address", ""),
           business.get("phone", ""),
           business.get("website", ""),
           business.get("rating", ""),
           business.get("reviews", "")
       ])
   
   print(f"{len(businesses)} rows inserted")