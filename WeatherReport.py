import requests
#import json

# Class
class City:
    def __init__(self, name , lat , lon, units = "metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}6&lon={self.lon}&appid=<API_Key>")
        except:
            print("No Internet access:( ")

        response_json = response.json()
        self.temp = response_json["main"]["temp"]
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]

    def temp_print(self):
        print(f"Today Bangalore temparature is {self.temp}° C")
        print(f"Today Bangalore minimum temparature is {self.temp_min}° C")
        print(f"Today Bangalore maximum temparature is {self.temp_max}° C")   


bangalore = City("Bangalore", 12.9716, 77.5946)
bangalore.temp_print()


    
