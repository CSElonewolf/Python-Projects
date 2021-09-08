from fastapi import FastAPI
from scrape import run as scrape_runner

app = FastAPI()

# Home Page 
@app.get('/')
def default_page():
	return "Hit '/box-office-mojo-scrapper' endpoint to scrape"

# Hitting this endpont will run the scrapper or the job given 
@app.get('/box-office-mojo-scrapper')
def box__office_scraper_view():
	scrape_runner()
	return "Completed Scrapping"
