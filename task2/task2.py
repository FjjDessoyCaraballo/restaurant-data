import os
import pandas as pd
import numpy as np
import sys

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

def sliceByCountry(df: pd.DataFrame, country: str) -> pd.DataFrame:
	"""
	Slice dataframe by selected country.
	:param df: dataframe
	:param country: country of choice
	:return: df containing results of country specified in `country`
	"""
	return df[df['REGISTRATION_COUNTRY'] == country]

def main():
	df: pd.DataFrame = loadCsvData(findPath())
	df = deleteNonPurchasers(df)
	finDf: pd.DataFrame = sliceByCountry(df, "FIN")
	dnkDf: pd.DataFrame = sliceByCountry(df, "DNK")
	greDf: pd.DataFrame = sliceByCountry(df, "GRE")
	
	country_code: str = None
	if len(sys.argv) == 2:
		country_code = sys.argv[1].upper()
	else:
		print("Insert either FIN, DNK, or GRE as third parameter")

	if country_code == "FIN":
		if finDf is not None:
			print(f"Below you will see the dataframe for Finland:\n{finDf}")
	if country_code == "DNK":
		if dnkDf is not None:
			print(f"Below you will see the dataframe for Denmark:\n{dnkDf}")
	if country_code == "GRE":
		if greDf is not None:
			print(f"Below you will see the dataframe for Greece:\n{greDf}")
	

if __name__ == "__main__":
	main()