import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from firstPurchase import filterFirstPurchase

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


	# Safe calculation function to handle potential NaN or empty series
	def safe_calc(series, func, decimals=2):
		try:
			result = func(series)
			if hasattr(result, 'round'):
				return result.round(decimals)
			else:
				return round(result, decimals)
		except:
			return float('nan')

	# form dataframe with extracted information
	stats = {
		'web': {
			'mean (€)': safe_calc(PurchaseWeb, lambda x: x.mean()),
			'median (€)': safe_calc(PurchaseWeb, lambda x: x.median()),
			'25th percentile (€)': safe_calc(PurchaseWeb, lambda x: x.quantile(0.25)),
			'75th percentile (€)': safe_calc(PurchaseWeb, lambda x: x.quantile(0.75))
		},
		'ios': {
			'mean (€)': safe_calc(PurchaseIos, lambda x: x.mean()),
			'median (€)': safe_calc(PurchaseIos, lambda x: x.median()),
			'25th percentile (€)': safe_calc(PurchaseIos, lambda x: x.quantile(0.25)),
			'75th percentile (€)': safe_calc(PurchaseIos, lambda x: x.quantile(0.75))
		},
		'android': {
			'mean (€)': safe_calc(PurchaseAndroid, lambda x: x.mean()),
			'median (€)': safe_calc(PurchaseAndroid, lambda x: x.median()),
			'25th percentile (€)': safe_calc(PurchaseAndroid, lambda x: x.quantile(0.25)),
			'75th percentile (€)': safe_calc(PurchaseAndroid, lambda x: x.quantile(0.75))
		}
	}

	print(minOrMax)

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

def scatterPlotTotalPurchases(df: pd.DataFrame, os: str=None, country: str=None) -> None:
	"""
	Function to make a scatterplot to visualize trend between total purchases
	and days to first purchase.

	:Parameters:
	df
	    pd.DataFrame that should be parsed beforehand to exclude useless data
	
	:Returns:
	None
	"""
	# Apply strict filtering to get meaningful data
	filteredDf = df.copy()

	# Select OS
	if os:
		filteredDf = filteredDf[filteredDf["PREFERRED_DEVICE"] == os]
	
	if country:
		filteredDf = filteredDf[filteredDf["REGISTRATION_COUNTRY"] == country]
	
	# add the DAYS_TO_FIRST_PURCHASE column
	filteredDf = filterFirstPurchase(filteredDf)

	# remove rows with zero or negative values
	filteredDf = filteredDf[filteredDf['DAYS_TO_FIRST_PURCHASE'] > 0]

	# remove extreme values
	q1Days = filteredDf['DAYS_TO_FIRST_PURCHASE'].quantile(0.05)
	q3Days = filteredDf['DAYS_TO_FIRST_PURCHASE'].quantile(0.95)
	iqrDays = q3Days - q1Days

	q1_purchases = filteredDf['TOTAL_PURCHASES_EUR'].quantile(0.05)
	q3_purchases = filteredDf['TOTAL_PURCHASES_EUR'].quantile(0.95)
	iqr_purchases = q3_purchases - q1_purchases

	# remove outliers
	days_upper = q3Days + 3 * iqrDays
	purchases_upper = q3_purchases + 3 * iqr_purchases

	filteredDf = filteredDf[filteredDf['DAYS_TO_FIRST_PURCHASE'] <= days_upper]
	filteredDf = filteredDf[filteredDf['TOTAL_PURCHASES_EUR'] <= purchases_upper]

	# scatterplot creation
	plt.figure(figsize=(12, 8))

	# creating scatterplot with different density for aesthetic reasons
	plt.scatter(
	    filteredDf['DAYS_TO_FIRST_PURCHASE'], 
	    filteredDf['TOTAL_PURCHASES_EUR'], 
	    alpha=0.5,
	    s=30,
	    color='#3498db'
	)

	# linear regression
	z = np.polyfit(filteredDf['DAYS_TO_FIRST_PURCHASE'], filteredDf['TOTAL_PURCHASES_EUR'], 1)
	p = np.poly1d(z)
	xLine = np.linspace(filteredDf['DAYS_TO_FIRST_PURCHASE'].min(), filteredDf['DAYS_TO_FIRST_PURCHASE'].max(), 100)
	plt.plot(xLine, p(xLine), "r--", linewidth=2, alpha=0.8)

	# correlation coefficient
	corr = filteredDf['DAYS_TO_FIRST_PURCHASE'].corr(filteredDf['TOTAL_PURCHASES_EUR'])
	plt.annotate(
		f'Correlation: {corr:.2f}', 
		xy=(0.05, 0.95), 
		xycoords='axes fraction',
		fontsize=12,
		bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
	)

	# enhancing readability
	plt.xlabel('Days to First Purchase', fontsize=12)
	plt.ylabel('Total Purchases (€)', fontsize=12)

	if country == None:
		country = "All Countries"

	if os:
		plt.title(f'{os} in {country}: Relationship Between Days Until First Purchase and Total Amount (€)', fontsize=14)
	else:
		plt.title('Relationship Between Days Until First Purchase and Total Amount (€)', fontsize=14)		
	plt.grid(True, alpha=0.3, linestyle='--')
    
	# text box
	statsText = (
    	f"Data points: {len(filteredDf)}\n"
    	f"Mean days: {filteredDf['DAYS_TO_FIRST_PURCHASE'].mean():.1f}\n"
    	f"Mean purchases: {filteredDf['TOTAL_PURCHASES_EUR'].mean():.1f}€"
    )
	plt.figtext(0.15, 0.02, statsText, fontsize=10,
			 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
	plt.tight_layout()
	plt.show()

