class Town:
    def __init__(self, town_name):
        self.town_name = town_name
        self.latitude = '0°N'
        self.longitude = '0°E'
    
    def set_latitude(self, latitude):
        self.latitude = latitude
    
    def set_longitude(self, longitude):
        self.longitude = longitude
    
    def __repr__(self):
        result = f'Town {self.town_name} | Latitude: {self.latitude} | Longitude: {self.longitude}'

        return result
        
town = Town('Sofia')
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)