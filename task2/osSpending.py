import pandas as pd
import matplotlib.pyplot as plt

def	minMaxPurchase(df: pd.DataFrame, minOrMax: str):
	"""
	Display of table containing `MAX_PURCHASE_VALUE_EUR` and `PREFERRED_DEVICE`
	
	:Parameters:
	df
		Parsed pandas dataframe

	:Parameters:
	minOrMax
		string that should contain option 'min' or 'max' to define which column 
		the function should extract

	:Returns:
	statsDataframe
		Dataframe containing mean, median, 25th percentile, and 75th percentile of
		each different OS
	"""
	# separate by OS using boolean mask
	dfIos = (df[df['PREFERRED_DEVICE'] == "ios"])
	dfAndroid = (df[df['PREFERRED_DEVICE'] == "android"])
	dfWeb = (df[df['PREFERRED_DEVICE'] == "web"])

	if minOrMax == "max":
		# extract `MAX_PURCHASE_VALUE_EUR` column from specific OS'
		PurchaseWeb = dfWeb['MAX_PURCHASE_VALUE_EUR']
		PurchaseAndroid = dfAndroid['MAX_PURCHASE_VALUE_EUR']
		PurchaseIos = dfIos['MAX_PURCHASE_VALUE_EUR']
	elif minOrMax == "min":
		# extract `MIN_PURCHASE_VALUE_EUR` column from specific OS'
		PurchaseWeb = dfWeb['MIN_PURCHASE_VALUE_EUR']
		PurchaseAndroid = dfAndroid['MIN_PURCHASE_VALUE_EUR']
		PurchaseIos = dfIos['MIN_PURCHASE_VALUE_EUR']
	else:
		print("Error: second parameter can only contain the string [min] or [max] without brackets")

	# form dataframe with extracted information
	stats = {
		'web': {
			'mean': PurchaseWeb.mean().round(2),
			'median': PurchaseWeb.median().round(2),
			'25th percentile': PurchaseWeb.quantile(0.25).round(2),
			'75th percentile': PurchaseWeb.quantile(0.75).round(2)
		},
		'ios': {
			'mean': PurchaseIos.mean().round(2),
			'median': PurchaseIos.median().round(2),
			'25th percentile': PurchaseIos.quantile(0.25).round(2),
			'75th percentile': PurchaseIos.quantile(0.75).round(2)
		},
		'android': {
			'mean': PurchaseAndroid.mean().round(2),
			'median': PurchaseAndroid.median().round(2),
			'25th percentile': PurchaseAndroid.quantile(0.25).round(2),
			'75th percentile': PurchaseAndroid.quantile(0.75).round(2)
		}
	}

	# convert stats into pandas dataframe format
	statsDataframe = pd.DataFrame(stats)

	return statsDataframe

def plotPurchaseTable(maxDataFrame: pd.DataFrame, minDataFrame: pd.DataFrame) -> None:
	"""
	Function to visualize trend of spending through users OS'

	:Parameters:
	maxDataFrame
		Dataframe containing information regarding `MAX_PURCHASE_VALUE_EUR` 
	
	:Parameters:
	minDataFrame
		Dataframe containing information regarding `MIN_PURCHASE_VALUE_EUR`

	:Returns:
	None
	"""
	return

def	spendingByOs(df: pd.DataFrame):
	"""
	This module will verify the spending across users OS
	
	:Parameters:
	df
		Parsed dataframe
	"""
	maxDataFrame = minMaxPurchase(df, "min")
	minDataFrame = minMaxPurchase(df, "max")
	plotPurchaseTable(maxDataFrame, minDataFrame)
	return


"""
What are we doing?

Checking how much is spent across OS

columns to be used:

PREFERRED_DEVICE

against 

TOTAL_PURCHASES_EUR
DISTINCT_PURCHASE_VENUE_COUNT
MIN_PURCHASE_VALUE_EUR
MAX_PURCHASE_VALUE_EUR
AVG_PURCHASE_VALUE_EUR

"""