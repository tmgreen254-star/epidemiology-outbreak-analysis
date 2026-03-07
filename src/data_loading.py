import pandas as pd
import matplotlib.pyplot as plt
# John Hopkins dataset urls
cases_url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
deaths_url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
# Load datasets
cases=pd.read_csv(cases_url)
deaths=pd.read_csv(deaths_url)
print("Cases dataset shape:", cases.shape)
print("Deaths dataset shape:", deaths.shape)
# Sort by country
cases_country=cases.groupby("Country/Region").sum().drop(columns=["Lat","Long"])
deaths_country=deaths.groupby("Country/Region").sum().drop(columns=["Lat","Long"])
# Convert the dates into rows
cases_country=cases_country.T
cases_country.index=pd.to_datetime(cases_country.index)
# Plot
cases_country["US"].plot(figsize=(10,5))
plt.title("COVID-19 Cases Over Time (US)")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.show()
