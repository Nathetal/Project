import googlemaps
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

api_key="AIzaSyDb40LgQ8lTk5A44CI7GGtjbabgPcfZJWM"

maps_client = googlemaps.Client(key=api_key)

City1 = str(raw_input("Enter Name of Origin City:"))
City2 = str(raw_input("Enter Name of Destination City:"))

dist_matrix = maps_client.distance_matrix(City1, City2)

print dist_matrix[u'rows'][0][u'elements'][0][u'distance'][u'text']

