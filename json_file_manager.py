import json
import os

def json_file_manager():
   RAW_FILE = "data/raw_data.json"
   BUSINESS_FILE = "data/business.json"
   
   MASTER_RAW_FILE = "data/all_raw_data.json"
   MASTER_BUSINESS_FILE = "data/all_businesses.json"
   
   
   def load_json(path, default):
       if not os.path.exists(path):
           return default
   
       with open(path, "r", encoding="utf-8") as file:
           return json.load(file)
   
   
   def save_json(path, data):
       with open(path, "w", encoding="utf-8") as file:
           json.dump(
               data,
               file,
               indent=4,
               ensure_ascii=False
           )
   
   
   # ------------------------
   # RAW DATA
   # ------------------------
   
   current_raw = load_json(RAW_FILE, {})
   master_raw = load_json(MASTER_RAW_FILE, [])
   
   master_raw.append(current_raw)
   
   save_json(
       MASTER_RAW_FILE,
       master_raw
   )
   
   
   # ------------------------
   # BUSINESSES
   # ------------------------
   
   current_businesses = load_json(
       BUSINESS_FILE,
       []
   )
   
   master_businesses = load_json(
       MASTER_BUSINESS_FILE,
       []
   )
   
   existing_keys = {
       (
           business.get("name", ""),
           business.get("phone", "")
       )
       for business in master_businesses
   }
   
   new_count = 0
   
   for business in current_businesses:
   
       key = (
           business.get("name", ""),
           business.get("phone", "")
       )
   
       if key not in existing_keys:
           master_businesses.append(business)
           existing_keys.add(key)
           new_count += 1
   
   save_json(
       MASTER_BUSINESS_FILE,
       master_businesses
   )
   
   
   # ------------------------
   # CLEANUP
   # ------------------------
   
   if os.path.exists(RAW_FILE):
       os.remove(RAW_FILE)
   
   if os.path.exists(BUSINESS_FILE):
       os.remove(BUSINESS_FILE)
   
   print(f"Added {new_count} new businesses")
   print("Temporary files deleted")