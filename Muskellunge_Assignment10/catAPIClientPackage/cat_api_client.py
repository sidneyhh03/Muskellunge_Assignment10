# cat_api_client.py
import requests
import csv
import json

class CatAPIClient:
    def __init__(self):
        # Initialize API URL and key
        self.api_url = "https://api.thecatapi.com/v1/breeds"
        self.api_key = "live_z0aXW5WFBDMbm1oMgjmx39zVPLVp1RgGlukDiWGDiRK855zzsWfl50a26OybJXpJ"
        self.headers = {"x-api-key": self.api_key}
        self.data = []

    def fetch_data(self):
        # Send a GET request to the Cat API
        response = requests.get(self.api_url, headers=self.headers)
        
        # Check if the response is successful
        if response.status_code == 200:
            self.data = response.json()  # Parse JSON response
        else:
            print(f"Failed to fetch data: {response.status_code}")

    def print_data(self):
        # Print some interesting data in a readable format
        print("Cat Breeds Information:")
        for cat in self.data[:5]:  # Print the first 5 breeds for brevity
            print(f"Breed: {cat['name']}")
            print(f"Origin: {cat['origin']}")
            print(f"Description: {cat['description']}")
            print(f"Temperament: {cat['temperament']}\n")

    def save_to_csv(self):
        # Save the data to a CSV file
        with open('cat_breeds.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "origin", "description", "temperament"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write rows
            for cat in self.data:
                writer.writerow({
                    "name": cat.get("name", "N/A"),
                    "origin": cat.get("origin", "N/A"),
                    "description": cat.get("description", "N/A"),
                    "temperament": cat.get("temperament", "N/A")
                })
        print("Data has been saved to cat_breeds.csv")
