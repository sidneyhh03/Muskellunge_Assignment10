# main.py
from catAPIClientPackage.cat_api_client import CatAPIClient

def main():
    # Create an instance of the Cat API client
    cat_client = CatAPIClient()
    
    # Fetch data from the API
    cat_client.fetch_data()
    
    # Print the data to the console
    cat_client.print_data()
    
    # Save the data to a CSV file
    cat_client.save_to_csv()

if __name__ == "__main__":
    main()
