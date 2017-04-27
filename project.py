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

if dist_matrix[u'rows'][0][u'elements'][0][u'status'] == "ZERO_RESULTS":
	lat_long1 = maps_client.geocode(Location1)
	lat_long2 = maps_client.geocode(Location2)
	latitude_loc1 = lat_long1[0][u'geometry'][u'location'][u'lat']
	longitude_loc1 = lat_long1[0][u'geometry'][u'location'][u'lng']
	latitude_loc2 = lat_long2[0][u'geometry'][u'location'][u'lat']
	longitude_loc2 = lat_long2[0][u'geometry'][u'location'][u'lng']
	print "The cities in your query do not have a direct land route. However, the approximate as-the-crow-flies distance between these locations is:" + " " + str('%0.2f'%Absolute_Distance(latitude_loc1,latitude_loc2,longitude_loc1,longitude_loc2))	+ "km"
else:
	print dist_matrix[u'rows'][0][u'elements'][0][u'distance'][u'text']
	

