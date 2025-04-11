import pandas as pd
import matplotlib.pyplot as plt
from parsing import parseDf

listOfPlatforms = ["ios", "android", "web"]
listOfCountries = ["FIN", "DNK", "GRC"]

# safe calculation function to handle potential NaN or empty series
# in case of failure it returns nan
def safeCalculation(series, func, decimals=2):
	try:
		result = func(series)
		if hasattr(result, 'round'):
			return result.round(decimals)
		else:
			return round(result, decimals)
	except:
		return float('nan')

def totalUsers(argument: str) -> int:
	"""
	Function to calculate and return the total number of users by
	country or OS.

	:Returns:
	users
		number of total users of OS or country. In case of failure it returns -1
	"""
	# Determine if argument is a country or platform
	if argument in listOfPlatforms:
		df = parseDf()
		users = df[df['PREFERRED_DEVICE'] == argument].shape[0]
		return users
	elif argument in listOfCountries:
		df = parseDf()
		users = df[df['REGISTRATION_COUNTRY'] == argument].shape[0]
		return users
	else:
		return -1

def diffBetweenFirstAndLastPurchase(df: pd.DataFrame, country: str=None) -> pd.DataFrame:
	"""
	Function to view data measuring on active users. An active users is characterized
	as someone that has made at least one purchase. Inside the active users group there
	is another group of single day users; single day users are people that have only made
	a single purchase and therefore `FIRST_PURCHASE_DATE` and `LAST_PURCHASE_DATE` sums
	up to zero.

	:Parameters:
	df
		pd.DataFrame parsed dataframe

	:Parameters:
	country
		string that should contain desired country to visualize. Available countries
		are FIN, DNK, and GRC. Leave blank to view all.

	:Returns:
	df
		pd.DataFrame parsed dataframe containing new column `DIFF_FROM_FIRST_TO_LAST`
	"""
	# find if string `country` is in the list of valid countries
	if country in listOfCountries:
		dfCountry = (df[df['REGISTRATION_COUNTRY'] == country]).copy()
	elif country == None:
		dfCountry = df.copy()
	else:
		print("Error: no such country")
		return None

	if country == "DNK":
		country = "Denmark"
	elif country == "FIN":
		country = "Finland"
	else:
		country = "Greece"

	# get difference from first to last day
	firstPurchase = pd.to_datetime(dfCountry['FIRST_PURCHASE_DAY'].str[:10])
	lastPurchase = pd.to_datetime(dfCountry['LAST_PURCHASE_DAY'].str[:10])
	daysBetweenPurchases = (lastPurchase - firstPurchase).dt.days

	# create new column
	dfCountry['DIFF_FROM_FIRST_TO_LAST'] = daysBetweenPurchases

	# separate by OS using boolean mask
	dfIos = (dfCountry[dfCountry['PREFERRED_DEVICE'] == "ios"])
	dfAndroid = (dfCountry[dfCountry['PREFERRED_DEVICE'] == "android"])
	dfWeb = (dfCountry[dfCountry['PREFERRED_DEVICE'] == "web"])

	# extract column with differences series
	differenceIos = dfIos['DIFF_FROM_FIRST_TO_LAST']
	differenceAndroid = dfAndroid['DIFF_FROM_FIRST_TO_LAST']
	differenceWeb = dfWeb['DIFF_FROM_FIRST_TO_LAST']

	# count total rows
	iosTotal = len(dfIos)
	androidTotal = len(dfAndroid)
	webTotal = len(dfWeb)

	# calculate percentages
	singleDayIosValue = safeCalculation((differenceIos == 0).sum() / iosTotal * 100 if iosTotal > 0 else 0, lambda x: x)
	singleDayAndroidValue = safeCalculation((differenceAndroid == 0).sum() / androidTotal * 100 if androidTotal > 0 else 0, lambda x: x)
	singleDayWebValue = safeCalculation((differenceWeb == 0).sum() / webTotal * 100 if webTotal > 0 else 0, lambda x: x)

	# add percentage (%)
	singleDayIos = f"{singleDayIosValue}%" if not pd.isna(singleDayIosValue) else "N/A"
	singleDayAndroid = f"{singleDayAndroidValue}%" if not pd.isna(singleDayAndroidValue) else "N/A"
	singleDayWeb = f"{singleDayWebValue}%" if not pd.isna(singleDayWebValue) else "N/A"

	# calculate maximum active period
	maxIos = safeCalculation(differenceIos, lambda x: x.max())
	maxAndroid = safeCalculation(differenceAndroid, lambda x: x.max())
	maxWeb = safeCalculation(differenceWeb, lambda x: x.max())
	
	stats = {
		'web': {
			'Total Users': totalUsers("web"),
			'Mean Active Period': safeCalculation(differenceWeb, lambda x: x.mean()),
			'Median Active Period': safeCalculation(differenceWeb, lambda x: x.median()),
			'Single Day Users': singleDayWeb,
			'Maximum Active Period': maxWeb
		},
		'ios': {
			'Total Users': totalUsers("ios"),
			'Mean Active Period': safeCalculation(differenceIos, lambda x: x.mean()),
			'Median Active Period': safeCalculation(differenceIos, lambda x: x.median()),
			'Single Day Users': singleDayIos,
			'Maximum Active Period': maxIos
		},
		'android': {
			'Total Users': totalUsers("android"),
			'Mean Active Period': safeCalculation(differenceAndroid, lambda x: x.mean()),
			'Median Active Period': safeCalculation(differenceAndroid, lambda x: x.median()),
			'Single Day Users': singleDayAndroid,
			'Maximum Active Period': maxAndroid
		}
	}

	if country == None:
		pass
	else:
		print(country)
	
	statsDf = pd.DataFrame(stats)
	
	return statsDf

def	tableDiffFirstAndLast(stats: dict) -> None:
	"""
	Function that displays table with: total users, mean active period,
	median active period, single day users, and maximum active period.

	:Parameters:
	stats
		dict containing parsed information from df

	:Returns:
	None
	"""
	# turn dictionary into dataframe
	dataframe = pd.DataFrame(stats)

	# matrix for display
	formattedValues = []

	# loop for formatting values into float and integers
	for idx in dataframe.index:
		row = []
		for col in dataframe.columns:
			value = dataframe.at[idx, col]
			if idx in ['Mean Active Period', 'Median Active Period']:
				row.append(f"{value:.2f}")
			elif isinstance(value, (int, float)):
				row.append(f"{int(value)}")
			else:
				row.append(str(value))
		formattedValues.append(row)

	fig, ax = plt.subplots(figsize=(6,2.8))

	ax.axis('tight')
	ax.axis('off')

	table = ax.table(
		cellText=formattedValues,
		colLabels=dataframe.columns,
		rowLabels=dataframe.index,
		cellLoc='center',
		loc='center'
	)

	table.auto_set_font_size(False)
	table.set_fontsize(12)
	table.scale(0.8, 2.0)
	plt.title("Overall Activity Period Length by Device", pad=0.5)
	
	# layout adjustment
	plt.tight_layout(pad=1.0)
	plt.show()
	return

def activityPeriodCorrelation(df: pd.DataFrame, country: str=None) -> pd.DataFrame:
	"""
    Correlation Between Activity Period and Purchase Count
    
    :Parameters:
	df
		pd.DataFrame parsed dataframe
	
	:Parameters:
	country
		string that should contain desired country to visualize. Available countries
		are FIN, DNK, and GRC. Leave blank to view all.
	
	:Returns:
	statsDf
		pd.DataFrame dataframe containing mean active days,
		mean purchase, and correlation values by platform.
	"""
	# find if string `country` is in the list of valid countries
	if country in listOfCountries:
		dfCountry = (df[df['REGISTRATION_COUNTRY'] == country]).copy()
	elif country == None:
		dfCountry = df.copy()
	else:
		print("Error: no such country")
		return None

	if country == "DNK":
		country = "Denmark"
	elif country == "FIN":
		country = "Finland"
	else:
		country = "Greece"

	# get difference from first to last day
	firstPurchase = pd.to_datetime(dfCountry['FIRST_PURCHASE_DAY'].str[:10])
	lastPurchase = pd.to_datetime(dfCountry['LAST_PURCHASE_DAY'].str[:10])
	daysBetweenPurchases = (lastPurchase - firstPurchase).dt.days

	# add active days to the dataframe (individual values, not the mean)
	dfCountry['ACTIVE_DAYS'] = daysBetweenPurchases

	# separate by OS using boolean mask
	dfIos = dfCountry[dfCountry['PREFERRED_DEVICE'] == "ios"]
	dfAndroid = dfCountry[dfCountry['PREFERRED_DEVICE'] == "android"]
	dfWeb = dfCountry[dfCountry['PREFERRED_DEVICE'] == "web"]

	# calculate mean active days for each platform separately
	meanActivityPeriodWeb = dfWeb['ACTIVE_DAYS'].mean()
	meanActivityPeriodIos = dfIos['ACTIVE_DAYS'].mean()
	meanActivityPeriodAndroid = dfAndroid['ACTIVE_DAYS'].mean()

	# calculate mean purchase count for each platform
	meanPurchaseCountWeb = dfWeb['PURCHASE_COUNT'].mean()
	meanPurchaseCountIos = dfIos['PURCHASE_COUNT'].mean()
	meanPurchaseCountAndroid = dfAndroid['PURCHASE_COUNT'].mean()

	# calculate correlation between active days and purchase count for each platform
	corrWeb = dfWeb['ACTIVE_DAYS'].corr(dfWeb['PURCHASE_COUNT'])
	corrIos = dfIos['ACTIVE_DAYS'].corr(dfIos['PURCHASE_COUNT'])
	corrAndroid = dfAndroid['ACTIVE_DAYS'].corr(dfAndroid['PURCHASE_COUNT'])

	stats = {
		'web': {
			'Correlation': corrWeb.round(2),
			'Mean Active Period': meanActivityPeriodWeb.round(2),
			'Mean Purchases': meanPurchaseCountWeb.round(2),
		},
		'ios': {
			'Correlation': corrIos.round(2),
			'Mean Active Period': meanActivityPeriodIos.round(2),
			'Mean Purchases': meanPurchaseCountIos.round(2),
		},
		'android': {
			'Correlation': corrAndroid.round(2),
			'Mean Active Period': meanActivityPeriodAndroid.round(2),
			'Mean Purchases': meanPurchaseCountAndroid.round(2),
		}
	}

	if country == None:
		pass
	else:
		print(country)

	# convert to DataFrame for better display
	statsDf = pd.DataFrame(stats).T

	return statsDf

def firstAndLast(df: pd.DataFrame) -> None:
	"""
	Staging to retrieve data from first to last day of purchase. 
	The objective is to show that there is correlation between higher
	number of overall purchases and higher active days.

	This function is unnecessary inside the notebook.

	:Parameters:
	df
		pd.DataFrame parsed previously

	:Returns:
	None
	"""
	dfCopy = df.copy()
	diffBetweenFirstAndLastPurchase(dfCopy)
	# tableDiffFirstAndLast(dfCopy)
	activityPeriodCorrelation(dfCopy)
