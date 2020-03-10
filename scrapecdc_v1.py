# -*- coding: utf-8 -*-
# This python script extracts reported cases of Covid in America and saves data to
# a .dat file
# output file column one is dates, column 2 is number of infected

# requests will access the webpage
import requests
# beautiful soup parses the webpage
from bs4 import BeautifulSoup
# json turn the bs object into json
import json
# date time
from datetime import datetime

# here is the URL for the data. I found it by inspecting the table on the cdc webpage 
# https://www.cdc.gov/coronavirus/2019-ncov/cases-in-us.html
# I see the data for the graphic comes from this .json page
# I appended the /coronavirus/2019-ncov/us-cases-epi-chart.json to the cdc website
# and it worked!
URL = 'https://www.cdc.gov/coronavirus/2019-ncov/us-cases-epi-chart.json'
page = requests.get(URL)

# turn the requests object in bs object
soup = BeautifulSoup(page.content,'html.parser')

# convert to string for json
soup_str = str(soup)

# pars into json
soup_dict = json.loads(soup_str)

# get to the data lines
data_dict = soup_dict['data']

# just get the olumn lines
columns = data_dict['columns']

# preprocessed data
date_p = columns[0]
Ninfected_p = columns[1]

# fix the hanging element in front of list
date_l = date_p[1:len(date_p)]
Ninfected_l = Ninfected_p[1:len(Ninfected_p)]

# convert list to float
Ninfected = []
for item in Ninfected_l:
    Ninfected.append(float(item))
    
# save data   
File = open('output.dat','w')
for x in range(len(date_l)):
    File.write(date_l[x] + ', ' + str(Ninfected[x]) + '\n')
File.close()    

print('Data scraped from cdc.gov/coronavirus/2019-ncov.us-cases-epi-chart.json ') 
print('at ' + str(datetime.now()))
print(' ')
