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
# Keep only country name + date columns
cases = cases.drop(columns=["Province/State", "Lat", "Long"])
deaths = deaths.drop(columns=["Province/State", "Lat", "Long"])
# Group by country
cases_country = cases.groupby("Country/Region").sum()
deaths_country = deaths.groupby("Country/Region").sum()
# Convert dates into rows
cases_country = cases_country.T
deaths_country = deaths_country.T
cases_country.index = pd.to_datetime(cases_country.index)
deaths_country.index = pd.to_datetime(deaths_country.index)
# Calculate daily new cases
daily_cases = cases_country.diff()
# 7-day rolling average
daily_cases_7day = daily_cases.rolling(7).mean()
# Plot daily cases
daily_cases_7day["US"].plot(figsize=(10, 5))
plt.title("Daily COVID-19 Cases (7-day average, US)")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.tight_layout()
plt.savefig("us_daily_cases.png")
plt.show()
