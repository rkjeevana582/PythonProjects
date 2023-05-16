# from geopy.geocoders import ArcGIS
# nom = ArcGIS()
# nom.geocode('ternekal')
# try:
#     location = nom.geocode('ternekal')
#     print(location)
# except:
#     print('Geocoding error')
# from geopy.geocoders import ArcGIS
#
# nom = ArcGIS()
# location = nom.geocode('ternekal')
#
# if location:
#     latitude = location.latitude
#     longitude = location.longitude
#     print(f"Location: {location}")
#     print(f"Latitude: {latitude}")
#     print(f"Longitude: {longitude}")
# else:
#     print('Location not found')
import tkinter as tk
import requests
import json
from geopy.geocoders import ArcGIS

# create a tkinter window
root = tk.Tk()
root.geometry('400x300')
root.title('Geocoder App')

# create a label widget for the input field
label = tk.Label(root, text='Enter location:')
label.pack()

# create an entry widget for the user input
entry = tk.Entry(root)
entry.pack()

# create a function to geocode the input location
def geocode_location():
    location = entry.get()
    nom = ArcGIS()
    response = nom.geocode(location)
    if response:
        latitude = response.latitude
        longitude = response.longitude
        address = response.address
        pincode = response.raw['address']['Postal']
        data = {
            'location': location,
            'latitude': latitude,
            'longitude': longitude,
            'address': address,
            'pincode': pincode
        }
        # convert the data dictionary to JSON format
        json_data = json.dumps(data, indent=4)
        # create a label widget to display the JSON data
        result_label = tk.Label(root, text=json_data)
        result_label.pack()
    else:
        error_label = tk.Label(root, text='Location not found')
        error_label.pack()

# create a button to trigger the geocoding
button = tk.Button(root, text='Geocode', command=geocode_location)
button.pack()

# start the tkinter event loop
root.mainloop()
