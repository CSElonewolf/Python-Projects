import os 
import pprint
import json
from datetime import datetime,date 
from math import ceil

import requests
from PIL import Image, ImageFont, ImageDraw 


# openweatherapi_key 
api_key = os.environ.get('WEATHER_API_KEY')

# list of countries 
country_list = ["India","USA","UK"]


for i,country in enumerate(country_list):
    # nested list of all cities of the respective country 
    city_list = [["Kolkata","Delhi","Chennai","Mumbai","Jaipur"],["New York","Los Angeles","Chicago","San Diego","San Francisco"],["London","Cambridge","Oxford","Manchester","Liverpool"]]
    
    image = Image.open("post.png")
    image_editable = ImageDraw.Draw(image)

    # Heading
    font = ImageFont.truetype('inter.ttf', size = 50)
    header_text = f"{country} Weather Forecast"
    header_color = (255,255,255)
    image_editable.text((53,50), header_text, header_color , font=font)

    # Date 
    font = ImageFont.truetype('inter.ttf', size = 30)
    now = datetime.now()
    date_text =  now.strftime("%A - %B %d, %Y ")
    date_text_color = (255,255,255)
    image_editable.text((53,150), date_text, date_text_color , font=font)

    content_height = 300

    for city in city_list[i]:
        # making a get request 
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = json.loads(response.text)

        # grab the info from the json
        temp = str(ceil(data['main']['temp'])) + u"\u2103"
        humidity = str(data['main']['humidity'])

        # write on the image 
        font = ImageFont.truetype('inter.ttf', size = 45)
        image_editable.text((126,content_height), city, (0,0,0) , font=font)
        image_editable.text((600,content_height), temp, (255,255,255), font=font)
        image_editable.text((800,content_height), humidity,(255,255,255), font=font)

        content_height+=130
    # save it in .png and .pdf form
    image.save(str(date.today())+country+".png")
    image_pdf = image.convert('RGB')
    image_pdf.save(str(date.today())+country+".pdf")



