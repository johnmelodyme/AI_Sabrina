# usr/bin/env python 
# Developed By  JOHN MELODY MELISSA ESKHOL
#        Artificial Intelligence Name :  Sabrina 
#       Version : 1.1.0 
#       Supported  Language :  "en-US" 
#       File type :    `Location.Detection`

# pip install geolocation-python
from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient

#address = “New York City Wall Street 12”

google_maps = GoogleMaps(api_key=’your_google_maps_key’)

location = google_maps.search(location=address) # sends search to Google Maps.

print(location.all()) # returns all locations.

my_location = location.first() # returns only first location.

print(my_location.city) print(my_location.route) print(my_location.street_number) print(my_location.postal_code)

rint(my_location.country) print(my_location.country_shortcut)

print(my_location.formatted_address)

print(my_location.lat) print(my_location.lng)

# reverse geocode

lat = 40.7060008 lng = -74.0088189

my_location = google_maps.search(lat=lat, lng=lng).first()