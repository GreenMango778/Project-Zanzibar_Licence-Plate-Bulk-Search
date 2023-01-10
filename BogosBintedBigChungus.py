import requests
from bs4 import BeautifulSoup
import traceback

def get_vin(license_plate):
    try:
        # Send a request to thatcar
        url = "https://thatcar.nz/c/" + license_plate
        response = requests.get(url)

        # parse website html
        soup = BeautifulSoup(response.text, "html.parser")

        # find the td element containing the VIN code
        td = soup.find("td", text="VIN").find_next_sibling("td")

        # If the element isnt found, print "Not found"
        if not td:
            return "Not found"

        # Extract the VIN code from the table element
        vin = td.text

        return vin
    except:
        # print error info
        print(traceback.format_exc())
        return "Error"

def main():
    while True:
        # Ask user for a license plate
        license_plate = input("Enter a license plate number: ")

        # Pull the VIN from the website
        vin = get_vin(license_plate)

        # Print VIN
        print("VIN:", vin)

        # Ask the user if they want to enter another license plate number
        response = input("Enter another license plate number? (y/n) ")
        if response == "n":
            break

if __name__ == "__main__":
    main()