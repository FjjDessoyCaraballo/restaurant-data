import pandas as pd
import matplotlib.pyplot as plt

def conversionRate(df: pd.DataFrame):
	"""
	Calculates the conversion rate between users who have never made a purchase
	(PURCHASE_COUNT == 0) and those who have (PURCHASE_COUNT > 0),
	broken down by platform (ios, android, web).

	:Parameters:
	df : pd.DataFrame
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
	result['conversionRate'] = (result['purchasers'] / result['totalUsers']) * 100

	result['purchaserPercentage'] = (result['purchasers'] / result['totalUsers']) * 100
	result['nonPurchaserPercentage'] = (result['nonPurchasers'] / result['totalUsers']) * 100
	return result

def conversionByOs(df: pd.DataFrame):
	conversionMetric = conversionRate(df)
	print(conversionMetric)