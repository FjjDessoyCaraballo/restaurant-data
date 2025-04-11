import pandas as pd
import matplotlib.pyplot as plt

# make buckets of days
bins = [0, 1, 7, 14, 30, 60, 90, 180, 365, float('inf')]
labels = ['Same day', '1-7 days', '8-14 days', '15-30 days', '31-60 days',
	   '61-90 days', '91-180 days', '181-365 days', '365+ days']

def filterFirstPurchase(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Function to find the difference between registration date and 
	the day of the first purchase.

	:Parameters:
	df
		Pandas dataframe containing csv file provided previously

	:Returns:
	df
		New dataframe containing a new column `DAYS_TO_FIRST_PURCHASE`
	"""
	firstPurchase = pd.to_datetime(df['FIRST_PURCHASE_DAY'].str[:10])
	registry = pd.to_datetime(df['REGISTRATION_DATE'].str[:10])

	daysToPurchase = (firstPurchase - registry).dt.days

	df['DAYS_TO_FIRST_PURCHASE'] = daysToPurchase

	return df

def createBuckets(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Function to plot to visualize how long users take between registration
	and first purchase across different devices.

	:Parameters:
	df
		Pandas dataframe containing a new column `DAYS_TO_FIRST_PURCHASE`

	:Returns:
	percentageResult
		New dataframe that filters `DAYS_TO_FIRST_PURCHASE` into new 
		columns in buckets `PURCHASE_TIME_BUCKET`
	"""
	# copy sliced dataframe
	dfCopy = df.copy()
	
	# cut `DAYS_TO_FIRST_PURCHASE` into the buckets
	dfCopy['PURCHASE_TIME_BUCKET'] = pd.cut(dfCopy['DAYS_TO_FIRST_PURCHASE'], bins=bins, labels=labels, right=False)


	# Group by days to first purchase and count devices
	result = dfCopy.groupby('PURCHASE_TIME_BUCKET', observed=True).agg(
		web=('PREFERRED_DEVICE', lambda x: (x == "web").sum()),
		ios=('PREFERRED_DEVICE', lambda x: (x == "ios").sum()),
		android=('PREFERRED_DEVICE', lambda x: (x == "android").sum())
	)

	# percentage columns
	columnTotals = result.sum()
	percentageResult = pd.DataFrame(result.div(columnTotals).multiply(100).round(2))

	return percentageResult

def visualizeFirstPurchase(df: pd.DataFrame, country: str) -> None:
	"""
	Function that generates a table for visualizing how long a client takes
	between their registration and first purchase. It can take a second parameter
	string that defines which country the user wants to observe.

	:Parameters:
	df
		Pandas dataframe containing csv file provided previously
	
	:Parameters:
	country
		String that defines which country will be visualized.
		Input either FIN, DNK, GRC, or ALL
	"""
	fig, ax = plt.subplots(figsize=(5,1))

	plt.title(f"Time to first purchase: {country} (%)", pad=90)

	ax.axis("tight")
	ax.axis("off")

	# Create table
	table = ax.table(
		cellText=df.values,
		colLabels=df.columns,
		rowLabels=df.index,
		cellLoc="center",
		loc="center"
	)

	# set font size manually
	table.auto_set_font_size(False)
	table.set_fontsize(12)
	
	# set scale of table
	table.scale(0.7, 1.8)

	# output visualization
	plt.show()

def firstPurchase(df: pd.DataFrame, country: str):
	"""
	Staging area to filter and plot our dataframe. Here we want to
	understand if there is some pattern to the day of the registry
	date and day of first purchase across users devices.

	:Parameters:
	df
		Pandas dataframe containing csv file provided previously

	:Parameters:
	country
		String that should inform which country one desires to see data
		from. Options are: FIN, DNK, GRC, and ALL.
	"""

	# insert new column `DAYS_TO_FIRST_PURCHASE`
	newDfAddedColumn: pd.DataFrame = filterFirstPurchase(df)

	# filter by selected country. This dataframe will still contain most of the original columns
	if country != "ALL":
		filteredDf = newDfAddedColumn[newDfAddedColumn['REGISTRATION_COUNTRY'] == country]
	else:
		filteredDf = newDfAddedColumn.copy()

	# create buckets with `DAYS_TO_FIRST_PURCHASE` (e.g. - same day, 1-7 days, etc). This dataframe does NOT
	# contain most of the original dataframe columns.
	createBuckets(filteredDf)
	
	# Visualization of data on table by country (options: FIN, DNK, GRC, ALL)
	# visualizeFirstPurchase(dfWithBuckets, country)
		