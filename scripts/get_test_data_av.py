import csv
import json
import requests
from dotenv import load_dotenv

load_dotenv()  # Make sure there is a .env with a ALPHA_VANTAGE_API_KEY before this is run

response = requests.get(  # Response returns in CSV format https://www.alphavantage.co/documentation/#intraday-extended
    'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey={ALPHA_VANTAGE_API_KEY}')

csv_list = list(csv.reader(response.text.splitlines(), delimiter=','))

with open('src/lib/assets/alpha_vantage_IBM_time_series.json', 'w', encoding='utf-8') as f:
    json.dump(csv_list, f, ensure_ascii=False, indent=4)
