import os 
import pandas as pd 
from fastapi import FastAPI


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CACHE_DIR = os.path.join(BASE_DIR,'cache')
dataset = os.path.join(CACHE_DIR,'movies-box-office-dataset-cleaned.csv')


app = FastAPI()

@app.get('/')
def home_page():
	return {'Hit':'/box-office'}

@app.get("/box-office")
def read_box_office():
	df = pd.read_csv(dataset)
	return df.to_dict("Rank")

