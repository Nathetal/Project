import googlemaps
import requests.packages.urllib3
import math
requests.packages.urllib3.disable_warnings()

api_key="AIzaSyDb40LgQ8lTk5A44CI7GGtjbabgPcfZJWM"

maps_client = googlemaps.Client(key=api_key)

def Absolute_Distance(a,b,c,d):
	rad_a = math.radians(a)
	rad_b = math.radians(b)
	rad_c = math.radians(c)
	rad_d = math.radians(d)
	latdiff = rad_b-rad_a
	longdiff = rad_d-rad_c
	haversine_a = ((math.sin(latdiff/2))**2) + math.cos(rad_a)*math.cos(rad_b)*((math.sin(longdiff/2))**2)
	haversine_c = 2*(math.atan2((math.sqrt(haversine_a)), (math.sqrt(1-haversine_a))))
	haversine_d = 6371 * haversine_c
	return haversine_d

Location1 = str(raw_input("Enter Name of Origin Location:"))
Location2 = str(raw_input("Enter Name of Destination Location:"))

dist_matrix = maps_client.distance_matrix(Location1, Location2)

print dist_matrix[u'rows'][0][u'elements'][0][u'distance'][u'text']

