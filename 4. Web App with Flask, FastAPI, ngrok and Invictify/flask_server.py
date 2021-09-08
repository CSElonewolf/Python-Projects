from flask import Flask
from scrape import run as scrape_runner 


app = Flask(__name__)

# Home Page 
@app.route('/', methods = ['GET'])
def default_page():
	return "Hit '/box-office-mojo-scrapper' endpoint to scrape"

# Hitting this endpont will run the scrapper or the job given 
@app.route('/box-office-mojo-scrapper', methods = ['GET'])
def box__office_scraper_view():
	scrape_runner()
	return "Completed Scrapping"
