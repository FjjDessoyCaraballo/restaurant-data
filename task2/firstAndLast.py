import pandas as pd
import matplotlib.pyplot as plt
from parsing import parseDf

listOfPlatforms = ["ios", "android", "web"]
listOfCountries = ["FIN", "DNK", "GRC"]

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

def diffBetweenFirstAndLastPurchase(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Function 

	:Parameters:
	df
		pd.DataFrame parsed dataframe

	:Returns:
	df
		pd.DataFrame parsed dataframe containing new column `DIFF_FROM_FIRST_TO_LAST`
	"""
	# get difference from first to last day and create new column
	firstPurchase = pd.to_datetime(df['FIRST_PURCHASE_DAY'].str[:10])
	lastPurchase = pd.to_datetime(df['LAST_PURCHASE_DAY'].str[:10])
	daysToPurchase = (lastPurchase - firstPurchase).dt.days
	df['DIFF_FROM_FIRST_TO_LAST'] = daysToPurchase
	
	# separate by OS using boolean mask
	dfIos = (df[df['PREFERRED_DEVICE'] == "ios"])
	dfAndroid = (df[df['PREFERRED_DEVICE'] == "android"])
	dfWeb = (df[df['PREFERRED_DEVICE'] == "web"])
	
	differenceIos = dfIos['DIFF_FROM_FIRST_TO_LAST']
	differenceAndroid = dfAndroid['DIFF_FROM_FIRST_TO_LAST']
	differenceWeb = dfWeb['DIFF_FROM_FIRST_TO_LAST']

	# safe calculation function to handle potential NaN or empty series
	def safeCalculation(series, func, decimals=2):
		try:
			result = func(series)
			if hasattr(result, 'round'):
				return result.round(decimals)
			else:
				return round(result, decimals)
		except:
			return float('nan')
	
	# calculate single day users
	singleDayIos = (differenceIos == 0).sum()
	singleDayAndroid = (differenceAndroid == 0).sum()
	singleDayWeb = (differenceWeb == 0).sum()

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
	return stats

def	tableDiffFirstAndLast(df: pd.DataFrame) -> None:

	return

def	scatterplotDiffFirstAndLast(df: pd.DataFrame) -> None:
	
	return
	
def firstAndLast(df: pd.DataFrame) -> None:
	"""
	placeholder
	"""
	dfCopy = df.copy()
	dfCopy = diffBetweenFirstAndLastPurchase(dfCopy)
	tableDiffFirstAndLast(dfCopy)
	scatterplotDiffFirstAndLast(dfCopy)
	return

# def getSingleDayUsers(df: pd.DataFrame , os: str) -> int:
# 	if os in listOfPlatforms:
# 		firstPurchase = pd.to_datetime(df['FIRST_PURCHASE_DAY'].str[:10])
# 		lastPurchase = pd.to_datetime(df['LAST_PURCHASE_DAY'].str[:10])
		
# 		if df['']

# 		return users
# 	else:
# 		return -1