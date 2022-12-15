import pandas as pd # required pip + panda + requests
import requests
import json

#christmas farms

df = pd.read_csv("christmasfarms.csv") #input should be your csv name
#print(df.head()) <--- prints as a table 

i = 0 # count the loops to check accuracy
#recall the api and get the data for the missing variables
for i, row in df.iterrows():
	apiAddress = str(df.at[i, 'address'])
	#print(apiAddress) = loop and print the addresses to double check if they're accurate
	i += 1
	parameters = {
	"key" : "elGnZBl9t7GNUsKHl4bj8lE3v0*****", #limit of 15k transaction
	"location" : apiAddress
	}
	response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
	data = json.loads(response.text)['results'] #json format - makes it more organized

	lat = data[0]['locations'][0]['latLng']['lat']
	lng = data[0]['locations'][0]['latLng']['lng']
	print(lat, lng, i)

	df.at[i, 'lat'] = lat
	df.at[i, 'lng'] = lng

#save data and replace
df.to_csv('christmasfarms.csv')
