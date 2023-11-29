# 1. IMPORTS

# packages
from dotenv import load_dotenv
import requests
from plotly.express import line
from app.alpha import API_KEY
from app.email_service import send_email

#modules
import json
from pprint import pprint
from statistics import mean

# 2. ENVIRONMENT VARIABLES AND CONSTANTS
load_dotenv() #go look in the .env file for any env vars


# pauses execution of program wherever it is in the code, so u can more specifically investigate bugs
# breakpoint()

# 3. FUNCTIONS

def format_pct(my_number):
    """
    Formats a percentage number like 3.6555554 as percent, rounded to two decimal places.

    Param my_number (float) like 3.6555554

    Returns (str) like '3.66%'
    """
    return f"{my_number:.2f}%"

def fetch_data():
    request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)
    print(type(parsed_response))
    print(parsed_response.keys())
    #print(parsed_response)

    data = parsed_response["data"]
    return data

#main conditional
if __name__ == "__main__":

    # 4. WORKING CODE
    data = fetch_data()

    # Challenge A
    #
    # What is the most recent unemployment rate? And the corresponding date?
    # Display the unemployment rate using a percent sign.

    print("-------------------------")
    print("LATEST UNEMPLOYMENT RATE:")
    #print(data[0])

    latest_rate = data[0]['value']
    latest_date = data[0]["date"]

    print(f"{latest_rate}%","as of", latest_date)

    # Challenge B
    #
    # What is the average unemployment rate for all months during this calendar year?
    # ... How many months does this cover?

    this_year = [d for d in data if "2023-" in d["date"]]

    rates_this_year = [float(d["value"]) for d in this_year]
    #print(rates_this_year)

    print("-------------------------")
    print("AVG UNEMPLOYMENT THIS YEAR:", f"{round(mean(rates_this_year), 2)}%")
    print("NO MONTHS:", len(this_year))

    # Challenge C
    #
    # Plot a line chart of unemployment rates over time.


    dates = [d["date"] for d in data]
    rates = [float(d["value"]) for d in data]

    fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
    fig.show()

