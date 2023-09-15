import requests
# from forex_python.converter import CurrencyRates
from datetime import datetime

# Define the URL of the JSON API
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# Send an HTTP GET request to the API
response = requests.get(url)

df = []

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Create a dictionary to store the extracted data
    extracted_data = {}

    # Parse the JSON data from the response
    data = response.json()

    # Get specific column and store in extracted_data
    disclaimer = data["disclaimer"]
    chart_name =  data["chartName"]
    time_updated_1 = data["time"]["updated"]
    time_updated_iso_1 = data["time"]["updatedISO"]
    bpi_usd_code = data["bpi"]["USD"]["code"]
    bpi_usd_description = data["bpi"]["USD"]["description"]
    bpi_usd_rate_float = data["bpi"]["USD"]["rate_float"]
    bpi_gbp_code = data["bpi"]["GBP"]["code"]
    bpi_gbp_description = data["bpi"]["GBP"]["description"]
    bpi_gbp_rate_float = data["bpi"]["GBP"]["rate_float"]
    bpi_eur_code = data["bpi"]["EUR"]["code"]
    bpi_eur_description = data["bpi"]["EUR"]["description"]
    bpi_eur_rate_float = data["bpi"]["EUR"]["rate_float"]
 
else:
    # Handle the error if the request was not successful
    print(f"Error: Status code {response.status_code}")

# Add column bpi_idr_rate_float using forex_python library
# cr = CurrencyRates()
# bpi_idr_rate_float = cr.convert("USD", "IDR", df["bpi_usd_rate_float"])
bpi_idr_rate_float = bpi_usd_rate_float*15000

# Convert column type datetime
time_updated_datetime = datetime.strptime(time_updated_1, "%b %d, %Y %H:%M:%S UTC")
time_updated = time_updated_datetime.strftime("%Y-%m-%d %H:%M:%S")

time_updated_iso_datetime = datetime.strptime(time_updated_iso_1, "%Y-%m-%dT%H:%M:%S%z")
time_updated_iso = time_updated_iso_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Add last_update column
last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data_final = (disclaimer,chart_name,time_updated,time_updated_iso,bpi_usd_code,
              bpi_usd_description,bpi_usd_rate_float,bpi_gbp_code,bpi_gbp_description,
              bpi_gbp_rate_float,bpi_eur_code,bpi_eur_description,bpi_eur_rate_float,
              bpi_idr_rate_float,last_update)

# print(data_final)