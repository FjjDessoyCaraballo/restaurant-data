import pandas as pd
import matplotlib.pyplot as plt

def conversionRate(df: pd.DataFrame):
	"""
	Calculates the conversion rate between users who have never made a purchase
	(PURCHASE_COUNT == 0) and those who have (PURCHASE_COUNT > 0),
	broken down by platform (ios, android, web).

	:Parameters:
	df
	    DataFrame containing `PREFERRED_DEVICE` and `PURCHASE_COUNT` columns
	
	:Returns:
	pd.DataFrame
	    DataFrame with platforms as index and conversion metrics as columns
	"""
	# new column of `HAS_PURCHASED` users
	df['HAS_PURCHASED'] = (df['PURCHASE_COUNT'] > 0).astype(int)

	# aggregate result
	result = df.groupby('PREFERRED_DEVICE').agg(
		totalUsers=('HAS_PURCHASED', 'count'),
		purchasers=('HAS_PURCHASED', 'sum'),
		nonPurchasers=('HAS_PURCHASED', lambda x: (x == 0).sum())
	)

	# conversion rate
	result['conversionRate'] = ((result['purchasers'] / result['totalUsers']) * 100).round(2)
	result['nonPurchaserPercentage'] = ((result['nonPurchasers'] / result['totalUsers']) * 100).round(2)

	# After creating the result DataFrame
	result = result.rename(columns={
	    'totalUsers': 'Total Users',
	    'nonPurchasers': 'Zero Purchasers',
		'purchasers': 'Purchasers',
	    'conversionRate': 'Conversion Rate (%)',
	    'nonPurchaserPercentage': 'Zero Purchases (%)'
	})
	return result

def visualizeConversionTable(conversionTable: pd.DataFrame):
	"""
	Creates a visual table of conversion metrics using matplotlib.

	:Parameters:
	conversion_metrics
	    DataFrame with conversion metrics to display in a table
	
	:Returns:
	fig - table object that can be used later for saving it as pdf or image
	"""
	fig, ax = plt.subplots(figsize=(13,2.5))

	# set title
	plt.title('Conversion Metrics by Operating System', pad=0.5)

	ax.axis('tight')
	ax.axis('off')

	formattedData = conversionTable.copy()

	# Converting first three columns from float to int
	for col in formattedData.columns[:3]:
		formattedData[col] = formattedData[col].astype(int)
	cellText = []
	for row in formattedData.values:
		cellText.append([str(int(row[0])), str(int(row[1])), str(int(row[2])), 
						  f"{row[3]:.2f}", f"{row[4]:.2f}"])

	table = ax.table(
		cellText=cellText,
		colLabels=conversionTable.columns,
		rowLabels=conversionTable.index,
		cellLoc='center',
		loc='center'
	)

	table.auto_set_font_size(False)
	table.set_fontsize(12)
	table.scale(1.5, 2.0)
	plt.tight_layout(pad=3.0)
	plt.show()
	return fig

def conversionByOs(df: pd.DataFrame):
	"""
	Entry point for calling conversion rate and visualizing functions

	:Parameters:
	df
	    DataFrame parsed previously
	"""
	conversionMetric = conversionRate(df)
	visualizeConversionTable(conversionMetric)