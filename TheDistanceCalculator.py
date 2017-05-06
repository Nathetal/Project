import googlemaps									
import math 										
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()		#work-around to prevent warning from showing up when the program is run

api_key="AIzaSyDb40LgQ8lTk5A44CI7GGtjbabgPcfZJWM"	

maps_client = googlemaps.Client(key=api_key)

#defining the function Absolute_Distance, which uses the Haversine formula in order to calculate distance based on latitude and longitude
def Absolute_Distance(a,b,c,d):						
	rad_a = math.radians(a)
	rad_b = math.radians(b)
	rad_c = math.radians(c)
	rad_d = math.radians(d)							 
	latdiff = rad_b-rad_a							
	longdiff = rad_d-rad_c							
	haversine_a = ((math.sin(latdiff/2))**2) + math.cos(rad_a)*math.cos(rad_b)*((math.sin(longdiff/2))**2)
	haversine_c = 2*(math.atan2((math.sqrt(haversine_a)), (math.sqrt(1-haversine_a))))
	haversine_d = 6371 * haversine_c				# 6371 is the approximate length of the Earth radius
	return haversine_d

print "This application will help you find the distance between 2 locations (using the Googlemaps api)"

Location1 = str(raw_input("Enter Name of Origin Location:"))				
Location2 = str(raw_input("Enter Name of Destination Location:"))

			
if Location1 != ""  and Location2 != "": 									#Values can only be computed if user enters some input 
	try:
		dist_matrix = maps_client.distance_matrix(Location1, Location2)			#using the googlemaps client to source distance from googlemaps api

		try: 
			if dist_matrix[u'rows'][0][u'elements'][0][u'status'] == "ZERO_RESULTS":		#Two locations cannot be travelled between by land, so dist_matrix will not work
				lat_long1 = maps_client.geocode(Location1)									
				lat_long2 = maps_client.geocode(Location2)									#uses the geocode api in order to source the latitude longitude information 
				latitude_loc1 = lat_long1[0][u'geometry'][u'location'][u'lat']
				longitude_loc1 = lat_long1[0][u'geometry'][u'location'][u'lng']
				latitude_loc2 = lat_long2[0][u'geometry'][u'location'][u'lat']
				longitude_loc2 = lat_long2[0][u'geometry'][u'location'][u'lng']				#index to the exact location where the relevant information is
				print "The cities in your query do not have a direct land route. However, the approximate as-the-crow-flies distance between these locations is:" + " " + str('%0.2f'%Absolute_Distance(latitude_loc1,latitude_loc2,longitude_loc1,longitude_loc2))	+ "km"
			else:
				print "The Distance between the entered locations is" + " " + str(dist_matrix[u'rows'][0][u'elements'][0][u'distance'][u'text'])			#indexing the exact location to print the result of distance between two locations
		except IndexError: 
			print "At least one search query could not be found. Please check the names for cities you have entered and try again."
		except KeyError: 
			print "At least one search query could not be found. Please check the names for cities you have entered and try again."		#completes the code by preventing it from throwing up errors arising from incorrect inputs from userwhich do not return a result in google maps
	except googlemaps.exceptions.TransportError:
		print "Check your Internet Connection"
else:
	print "Please enter location names" 		
