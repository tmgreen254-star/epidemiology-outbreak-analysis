import pandas as pd
  # John Hopkins dataset urls
  cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/refs/heads/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
  deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/refs/heads/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
 # Load datasets
  cases = pd.read_csv(cases_url)
  deaths = pd.read_csv(deaths_url)
  print("Cases dataset shape:", cases.shape)
  print("Deaths dataset shape:", deaths.shape)
  
