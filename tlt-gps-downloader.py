import requests
import time
from datetime import datetime

url = "https://transport.tallinn.ee/gps.txt"

while True:
    # Get current timedate for timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
    filename = f"gps-{timestamp}.txt"

    # Download data
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        data = response.text

        # Save the data to file
        with open(filename, "w") as file:
            file.write(data)
        
        print(f"Data saved to {filename}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

    # Wait 30 seconds to not get blocked
    time.sleep(30)