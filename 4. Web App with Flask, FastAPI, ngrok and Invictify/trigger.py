import requests


ngrok_link = 'https://c7f2-45-249-73-97.ngrok.io'
endpoint = f'{ngrok_link}/box-office-mojo-scrapper'

# this hits a post request on the above mentioned endpoint
r = requests.get(endpoint,json={})
if r.status_code in range(200,299):
	print("Scrapped")