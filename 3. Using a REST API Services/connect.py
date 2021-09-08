import requests
import pprint
import os

# we have stored the api key in env varibale 
api_key = os.environ.get('TMDB_API_KEY')

api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"

# First we use this to search movie
endpoint_path = f"/search/movie"
movie_name = input("enter a movie name:: ")
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={movie_name}"
# print(endpoint)

# send a get request to grab the json 
r = requests.get(endpoint)
json_data = r.json()

# it seems thje json has a vital key 'results' that stores the main content 
json_data_results = json_data['results']
# pprint.pprint(json_data['results'])

# loop through each results
for movie_details in json_data_results:
	# pprint.pprint(movie_details['id'])

	# grab the id of each movie to query further 
	movie_details_endpoint_path = f"/movie/{movie_details['id']}"
	# generate the endpoint that we are going to send a 'GET' request
	movie_details_endpoint = f"{api_base_url}{movie_details_endpoint_path}?api_key={api_key}&language=en-US"
	
	# print(movie_details_endpoint)
	res = requests.get(movie_details_endpoint)
	
	# we print the results 
	pprint.pprint(res.json())
