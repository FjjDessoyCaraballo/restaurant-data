import pandas as pd

def filterFirstPurchase(df: pd.DataFrame):
	"""
	Function to find the difference between registration date and 
	the day of the first purchase.

	:Parameters:
	df
		Pandas dataframe containing csv file provided previously
	"""
	firstPurchase = df['FIRST_PURCHASE_DAY'].str[:10]
	registry = df['REGISTRATION_DATE'].str[:10]

	daysToPurchase = (firstPurchase - registry).dt.date

	df['DAYS_TO_FIRST_PURCHASE'] = daysToPurchase

	return df

def firstPurchasePlotCountry(df: pd.DataFrame, country: str):
	"""
	Uses same logic from `firstPurchasePlot()` function, but filters
	by country.

	:Parameters:
	df
		Pandas dataframe containing a new column `DAYS_TO_FIRST_PURCHASE`
	:Parameters:
	country
		string defining specific country to plot
	"""

def firstPurchasePlot(df: pd.DataFrame):
	"""
	Function to plot to visualize how long users that between registration
	and first purchase.

	:Parameters:
	df
		Pandas dataframe containing a new column `DAYS_TO_FIRST_PURCHASE`
	"""

	return

def firstPurchase(df: pd.DataFrame):
	"""
	Staging area to filter and plot our dataframe. Here we want to
	understand if there is some pattern to the day of the registry
	date and day of first purchase across users devices.

	:Parameters:
	df
		Pandas dataframe containing csv file provided previously
	"""
	filteredData: pd.DataFrame = filterFirstPurchase(df)
	firstPurchasePlot(filteredData)
	return