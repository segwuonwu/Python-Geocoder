import geocoder
import requests
import unicodedata

destinations = ["The Space Needle",
  "Crater Lake",
  "The Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Aspen, Colorado",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspension Bridge"]

API_BASE_URL = "Enter your Dark Sky api key"

for point in destinations:
    # get the lat long from geocoder
    loc = geocoder.arcgis(point)
    #print(loc)

    # print out the result of the lat long formmated with lacation name
    print("{0} is located at ({1:.4f}, {2:.4f})".format(point, loc.latlng[0], loc.latlng[1]))

    full_api_url = API_BASE_URL + str(loc.latlng[0]) + "," + str(loc.latlng[1])
    result = requests.request('GET', full_api_url).json()
    deg = '\u00b0'
    print("At {0} right now, it's {1} with a temperature of {2:.1f}{3} F\n".format(point, result['currently']['summary'], result['currently']['temperature'], deg))

