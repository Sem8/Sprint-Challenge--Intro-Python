# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv

filename = 'cities.csv'
cities = []


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        # self.cities = []

    def __repr__(self):
        return f'City: {self.name}, {self.lat}, {self.lon}'


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # cities = [row[1:] for row in csvreader]
        # print(csvreader[0])
        next(csvreader)

        for row in csvreader:
            cities.append(City(row[0], float(row[3]), float(row[4])))
        return cities
    # print(cities)
        # print(row)
        # for row in rows:
        # for col in row:
        #   cities.append(col)

        # print(cities)
        # return cities

    # return City(cities[0], cities[3], cities[4])
    # print(City(cities[0], cities[3], cities[4]))
    # print(cities)
# print(cityreader())

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
#     print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
# within will hold the cities that fall within the specified region
  within = []

# TODO Ensure that the lat and lon valuse are all floats
  temp_lat = 0
  temp_lon = 0

  lat1 = float(lat1)
  lat2 = float(lat2)
  lon1 = float(lon1)
  lon2 = float(lon2)

  # alway ensure lat1 is greater than lat2 and lon1 is greater than lon2
  if lat1 >= lat2:
    pass
  else:
    temp_lat = lat1
    lat1 = lat2
    lat2 = temp_lat

  if lon1 >= lon2:
    pass    
  else:
    temp_lon = lon1
    lon1 = lon2
    lon2 = temp_lon    

# Go through each city and check to see if it falls within
# the specified coordinates.

  for a_city in cities:
    if (a_city.lat <= lat1 and a_city.lat >= lat2 and a_city.lon >= lon2 and a_city.lon <= lon1):
      within.append(a_city)
  print(within)
  return within


while True:
    latlon_inp1 = input('Please input lat1, lon1: ').split(',')
    latlon_inp2 = input('Please input lat2, lon2: ').split(',')

    if latlon_inp1 == 'q' or latlon_inp2 == 'q':
      break

    if len(latlon_inp1) == 2 and len(latlon_inp2) == 2:
        cityreader_stretch(latlon_inp1[0], latlon_inp1[1], latlon_inp2[0], latlon_inp2[1], cities)
        exit()
    else:
      print('Invalid coordinates')
