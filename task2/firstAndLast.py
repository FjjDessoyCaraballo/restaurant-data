import pandas as pd
import matplotlib.pyplot as plt

def diffBetweenFirstAndLastPurchase(df: pd.DataFrame) -> None:
	"""
	Function 

	:Parameters:
	df
		pd.DataFrame parsed dataframe

	:Returns:
	df
		pd.DataFrame parsed dataframe containing new column `DIFF_FROM_FIRST_TO_LAST`
	"""
	firstPurchase = pd.to_datetime(df['FIRST_PURCHASE_DAY'].str[:10])
	lastPurchase = pd.to_datetime(df['LAST_PURCHASE_DAY'].str[:10])

	daysToPurchase = (firstPurchase - lastPurchase).dt.days

	df['DIFF_FROM_FIRST_TO_LAST'] = daysToPurchase
	return df

def	tableDiffFirstAndLast(df: pd.DataFrame) -> None:
	
	return

def	scatterplotDiffFirstAndLast(df: pd.DataFrame) -> None:
	
	return
	
def firstAndLast(df: pd.DateFrame) -> None:
	"""
	placeholder
	"""
	dfCopy = df.copy()
	dfCopy = diffBetweenFirstAndLastPurchase(dfCopy)
	tableDiffFirstAndLast(dfCopy)
	scatterplotDiffFirstAndLast(dfCopy)
	return