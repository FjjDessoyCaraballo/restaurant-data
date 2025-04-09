import pandas as pd
import matplotlib.pyplot as plt

def	plotMinPurchase(df: pd.DataFrame):
	"""
	Display of table containing `MIN_PURCHASE_VALUE_EUR` and `PREFERRED_DEVICE`
	
	:Parameters:
	df
		Parsed pandas dataframe

	:Returns:
	None
	"""
	return

def	plotMaxPurchase(df: pd.DataFrame):
	"""
	Display of table containing `MAX_PURCHASE_VALUE_EUR` and `PREFERRED_DEVICE`
	
	:Parameters:
	df
		Parsed pandas dataframe

	:Returns:
	None
	"""
	return

def	osBySpending(df: pd.DataFrame):
	"""
	This module will verify the spending across users OS
	
	:Parameters:
	df
		Parsed dataframe
	"""
	plotMinPurchase(df)
	plotMaxPurchase(df)
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