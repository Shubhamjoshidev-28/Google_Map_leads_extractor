from extract import extractor
from required_data_extractor import required_data
from google_sheet_writer import google_sheet_writer
from json_file_manager import json_file_manager


extractor("resturants in usa")
required_data()
google_sheet_writer()
json_file_manager()
