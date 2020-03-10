# -*- coding: utf-8 -*-
# This python script extracts reported cases of Covid in America and saves data to
# a .dat file
# output file column one is dates, column 2 is number of infected

import pandas as pd

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
data = pd.read_csv(url)

data.to_csv(r'output.csv')
