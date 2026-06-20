import json 

def required_data():
  
  with open("data/raw_data.json", "r", encoding="utf-8") as file:
      data = json.load(file)
  
  local_results = data.get("local_results", [])
  
  business_results = []
  
  for business in local_results:
      business_info ={
          "business_name":business.get("title"),
          "address":business.get("address"),
          "phone":business.get("phone"),
          "website":business.get("website"),
          "rating":business.get("rating"),
          "reviews":business.get("reviews")
      }
  
      business_results.append(business_info)
  
  with open("data/business.json","w",encoding="utf-8") as file:
      json.dump(
          business_results,
          file,
          indent=4,
          ensure_ascii=False
      )
   
  print(f"{len(business_results)} business_saved")
