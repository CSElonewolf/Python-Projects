import os
import datetime 

import requests
from requests_html import HTML
import pandas as pd 


BASE_DIR = os.path.dirname(__file__)


# function to scarp the html of the passed url 
def url_to_file(url):
	r = requests.get(url)
	if r.status_code == 200:
		return r.text
	return None


def parse_and_extract(url,name=f'{datetime.datetime.now()}'):
	html_text = url_to_file(url)

	if html_text != None:

		# finding the data that contains the 'table'
		r_html = HTML(html = html_text)
		r_table = r_html.find('.mojo-body-table')

		table_data = []

		if len(r_table) == 1:
			parsed_table = r_table[0]
			rows = parsed_table.find("tr")

			# grabbing the header row 
			header_row = rows[0]
			header_names = [x.text for x in header_row.find("th")]

			# iterating through each row other than header row 
			for row in rows[1:]:
				cols= row.find("td")
				each_row_data = []

				# collecting the data from each columns 
				for index,col in enumerate(cols):
					each_row_data.append(col.text)

				table_data.append(each_row_data)

			# making a folder to store the csv files 
			path = os.path.join(BASE_DIR,'CSV_FILES')
			os.makedirs(path,exist_ok = True)
			filepath = os.path.join('CSV_FILES',f'{name}.csv')

			# writing the table_data into a csv file using pandas library 
			df = pd.DataFrame(table_data,columns= header_names)
			df.to_csv(filepath,index=False)
		return True

		# print(table_data)
	else:
		return False


url = 'https://www.boxofficemojo.com/year/world/'

# Driver Method
def run(start_year = None, count=10):
	# set current year as start_year in case no argument is passed 
	if start_year == None:
		now = datetime.datetime.now()
		start_year = now.year 

	assert isinstance(start_year,int)
	assert len(str(start_year)) == 4

	# check if the start year is within the range 
	if start_year > datetime.datetime.now().year:
		print(f"Start Year Must not exceed {datetime.datetime.now().year}")
		return

	assert isinstance(count,int)

	# Scarping the data year after year
	for i in range(0,count+1):
		url = f'https://www.boxofficemojo.com/year/world/{start_year}'
		if parse_and_extract(url,name = start_year):
			print(f"Finished {start_year}")
		else:
			print("Oops pls check the start_year")
			return
		start_year -= 1
	print("Scraping Completed!!")



if __name__ == '__main__':
	# Dynamically taking input 
	start_year = int(input("Enter a year to begin scarpping:"))
	count = int(input("How long back would you like to scrap:"))

	run(start_year=start_year,count=count)