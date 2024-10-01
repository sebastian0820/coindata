import requests

url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 250,  # Fetch 250 coins at a time
    'page': 1,  # Change page number to get more coins
    'sparkline': 'false'
}

response = requests.get(url, params=params)
data = response.json()
print(data[0])


import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import time
from matplotlib.animation import FuncAnimation

# Set the coin ID and the interval for fetching data
coin_id = 'bitcoin'
interval = 10  # Interval in seconds

# Prepare lists to store timestamps and prices
timestamps = []
prices = []

# Function to fetch the current price
def fetch_price():
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data[coin_id]['usd']
        return price
    elif response.status_code == 429:
        print("Too many requests. Waiting for 60 seconds...")
        time.sleep(60)  # Wait for a minute before trying again
        return fetch_price()  # Retry after waiting
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Function to update the graph
def update(frame):
    time.sleep(1)  # Add a delay to limit the request rate
    # Fetch the current price
    price = fetch_price()
    if price is not None:
        # Store the current timestamp and price
        timestamps.append(datetime.datetime.now())
        prices.append(price)

        # Clear the previous plot
        plt.clf()

        # Plot the updated data
        plt.plot(timestamps, prices, marker='o', color='orange', label='Bitcoin Price (USD)')
        plt.title('Real-Time Bitcoin Price')
        plt.xlabel('Timestamp')
        plt.ylabel('Price in USD')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()

# Create the plot
plt.figure(figsize=(12, 6))

# Set up the animation
ani = FuncAnimation(plt.gcf(), update, interval=interval * 1000)  # Interval in milliseconds

# Show the plot
plt.show()