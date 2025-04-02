import os
import pandas as pd
import numpy as np

def findPath():
	"""
	This function returns the directory of the script and csv file
	"""
	directory_path = os.path.dirname(os.path.abspath(__file__))
	file_path = os.path.join(directory_path, "dataset_for_datascience_assignment.csv")
	return file_path

def loadCsvData(file_path) -> pd.DataFrame:
	"""
	Storage of csv in a pandas data type for wrangling
	"""
	df: pd.DataFrame = pd.read_csv(file_path)
	return df

def main():
	print(f"Path is: {findPath()}")
	df: pd.DataFrame = loadCsvData(findPath())
	if df is not None:
		print(f"Below you will see the dataframe:\n{df}")
	return 0

if __name__ == "__main__":
	main()