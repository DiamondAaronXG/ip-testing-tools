import requests
import json

# Declares variable, asks and scans for user input

x = input("Enter IP's Seperated by a space: ")

# Loops through each IP address

for each in x.split(" "):

    # Sends API request for each IP
    
    req = requests.get(f"http://ip-api.com/json/{each}").content

    # Converts the JSON response into a python dictionary
    
    reqjson = json.loads(req)

    # Extrcts location details
    
    city = reqjson["city"]
    regionName = reqjson["regionName"]
    lat = reqjson["lat"]
    long_ = reqjson["lon"]

    # Prints results
    
    print(f"IP: {each}\nCity: {city}\nRegion Name: {regionName}\nLatitude: {lat}\nLongitude: {long_}\n\n")
