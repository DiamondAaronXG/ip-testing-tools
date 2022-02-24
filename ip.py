import requests
import json

x = input("Enter IP's Seperated by a space: ")
for each in x.split(" "):
    req = requests.get(f"http://ip-api.com/json/{each}").content
    reqjson = json.loads(req)
    city = reqjson["city"]
    regionName = reqjson["regionName"]
    lat = reqjson["lat"]
    long_ = reqjson["lon"]
    print(f"IP: {each}\nCity: {city}\nRegion Name: {regionName}\nLatitude: {lat}\nLongitude: {long_}\n\n")
