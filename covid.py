import pandas as pd

# Load the dataset from OWID
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Check the first few rows
print(df.head())

# Check basic info
print(df.info())
