import pandas as pd
import os

def findPath():
	"""
	This function returns the directory of the script and csv file
	:return: the path to the `.csv` file
	"""
	directory_path = os.path.dirname(os.path.abspath(__file__))
	file_path = os.path.join(directory_path, "dataset_for_datascience_assignment.csv")
	return file_path

def loadCsvData(file_path) -> pd.DataFrame:
	"""
	Storage of csv in a pandas data type for wrangling
	:param file_path: the path to the `.csv` file with our data
	:return: dataframe type pandas `.DataFrame`
	"""
	df: pd.DataFrame = pd.read_csv(file_path)
	return df

def deleteNonPurchasers(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Delete rows (users) that have never made a single purchase
	:param df: dataframe
	:return: sliced dataframe
	"""
	return df[df['PURCHASE_COUNT'] > 0]

def sliceByCountry(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Slice dataframe by selected countries. Considering that FIN, DNK, and GRC
	consist of 97% of the dataset, we will slice only these countries
	:param df: dataframe
	:return: df containing results of country specified in `country`
	"""
	countries = ['FIN', 'DNK', 'GRC']
	return df[df['REGISTRATION_COUNTRY'].isin(countries)]

def removeInconsistentPurchase(df: pd.DataFrame) -> pd.DataFrame:
	return df[~df['TOTAL_PURCHASES_EUR'].isna()]

def parseDf():
	"""
	Point of entry for parsing dataframe. User can input the country of leave
	it blank to get all countries together
	:country: desired country to view
	"""
	df: pd.DataFrame = loadCsvData(findPath())
	df = deleteNonPurchasers(df)
	df = removeInconsistentPurchase(df)
	df = sliceByCountry(df)
	return df