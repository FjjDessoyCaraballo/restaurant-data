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
			'mean (€)': PurchaseWeb.mean().round(2),
			'median (€)': PurchaseWeb.median().round(2),
			'25th percentile (€)': PurchaseWeb.quantile(0.25).round(2),
			'75th percentile (€)': PurchaseWeb.quantile(0.75).round(2)
		},
		'ios': {
			'mean (€)': PurchaseIos.mean().round(2),
			'median (€)': PurchaseIos.median().round(2),
			'25th percentile (€)': PurchaseIos.quantile(0.25).round(2),
			'75th percentile (€)': PurchaseIos.quantile(0.75).round(2)
		},
		'android': {
			'mean (€)': PurchaseAndroid.mean().round(2),
			'median (€)': PurchaseAndroid.median().round(2),
			'25th percentile (€)': PurchaseAndroid.quantile(0.25).round(2),
			'75th percentile (€)': PurchaseAndroid.quantile(0.75).round(2)
		}
	}

	# convert stats into pandas dataframe format
	statsDataframe = pd.DataFrame(stats)

	return statsDataframe

def plotPurchaseTable(df: pd.DataFrame, minOrMax: str) -> None:
	"""
	Function to visualize trend of spending through users OS'
	
	:Parameters:
	df
		Dataframe containing information regarding `MIN_PURCHASE_VALUE_EUR`

	:Parameters:
	minOrMax
		String to output correct title on table. There are not safeguards to
		what is inserted here, so it will display whatever one inserts here.

	:Returns:
	None
	"""
	fig, ax = plt.subplots(figsize=(7,2.5))

	ax.axis('tight')
	ax.axis('off')

	# Converting first three columns from float to int

	table = ax.table(
		cellText=df.values,
		colLabels=df.columns,
		rowLabels=df.index,
		cellLoc='center',
		loc='center'
	)

	table.auto_set_font_size(False)
	table.set_fontsize(12)
	table.scale(0.8, 2.0)
	plt.title(f"Expenditure stats by platform {minOrMax}", pad=0.5)
	
	# layout adjustment
	plt.tight_layout(pad=1.0)
	plt.show()
	return

def	spendingByOs(df: pd.DataFrame):
	"""
	This module will verify the spending across users OS
	
	:Parameters:
	df
		Parsed dataframe
	
	:Returns:
	None
	"""
	maxDataFrame = minMaxPurchase(df, "min")
	minDataFrame = minMaxPurchase(df, "max")
	plotPurchaseTable(maxDataFrame, "max")
	plotPurchaseTable(minDataFrame, "min")
