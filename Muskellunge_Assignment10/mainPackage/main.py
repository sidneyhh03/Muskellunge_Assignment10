
# Name: Denise Huynh and Sidney Huschart
# email:  huynhd2@mail.uc.edu and huschash@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   11/14/2024
# Course #/Section:   IS4010-001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Execute API calls with collaboration from github

# Brief Description of what this module does:   Entry point from the project
# Citations:
# Anything else that's relevant:

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
