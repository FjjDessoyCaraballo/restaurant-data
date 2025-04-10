import pandas as pd
import os

validDevices = ["ios", "android", "web"]

def findPath():
	"""
	This function returns the directory of the script and csv file
	
	:Returns: 
	filePath
		the path to the `.csv` file
	"""
	directoryPath = os.path.dirname(os.path.abspath(__file__))
	filePath = os.path.join(directoryPath, "dataset_for_datascience_assignment.csv")
	return filePath

def loadCsvData(file_path) -> pd.DataFrame:
	"""
	Storage of csv in a pandas data type for wrangling
	
	:Parameters:
	file_path
		the path to the `.csv` file with our data
	
	:Returns: 
		pd.DataFrame parsed dataframe
	"""
	df: pd.DataFrame = pd.read_csv(file_path)
	return df

def sliceByCountry(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Slice dataframe by selected countries. Considering that FIN, DNK, and GRC
	consist of 97% of the dataset, we will slice only these countries
	
	:Parameters:
	dataframe
		pd.DataFrame
	
	:Returns:
	df
		pd.DataFrame parsed dataframe
	"""
	countries = ['FIN', 'DNK', 'GRC']
	return df[df['REGISTRATION_COUNTRY'].isin(countries)]

def removeZeroPurchaseCount(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Function to remove rows that contain '0' in the `PURCHASE_COUNT` column

	:Returns:
	df
		pd.DataFrame parsed dataframe
	"""
	return df[df['PURCHASE_COUNT'] > 0]

def removeNaTotalPurchase(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Function to remove rows that contain NA/na/NaN in the `TOTAL_PURCHASES_EUR` column

	:Returns:
	df
		pd.DataFrame parsed dataframe
	"""
	return df[~df['TOTAL_PURCHASES_EUR'].isna()]

def removeZeroTotalPurchase(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Function to remove rows that contain '0' in the `TOTAL_PURCHASES_EUR` column

	:Returns:
	df
		pd.DataFrame parsed dataframe
	"""
	return df[df['TOTAL_PURCHASES_EUR'] > 0]

def sliceByValidDevice(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Function to slice off rows that contain other devices that are not
	android, ios, and web.

	:Returns:
	df
		pd.DataFrame parsed dataframe
	"""
	return df[df['PREFERRED_DEVICE'].isin(validDevices)]

def parseDf():
	"""
	Point of entry for parsing dataframe. If one desires to add further parsing,
	one can add `.pipe()` to the return value with the corresponding new function
	removing or adding columns.
	
	:Returns:
	df
		pd.DataFrame completely parsed dataframe
	"""
	return (loadCsvData(findPath())
			.pipe(sliceByCountry)
			.pipe(sliceByValidDevice)
			.pipe(removeZeroPurchaseCount)
			.pipe(removeNaTotalPurchase)
			.pipe(removeZeroTotalPurchase))



