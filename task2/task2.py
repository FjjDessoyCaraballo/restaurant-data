import os
import pandas as pd
import numpy as np
# from osCountry import osCountry
from parsing import parseDf

def main():
	# extract by country
	finDf: pd.DataFrame = parseDf("FIN")
	dnkDf: pd.DataFrame = parseDf("DNK")
	grcDf: pd.DataFrame = parseDf("GRC")
	allDf: pd.DataFrame = parseDf("")

	# Dictionary for dataframes
	dataframes = {
		"FIN": finDf,
		"DNK": dnkDf,
		"GRC": grcDf,
		"ALL": allDf,
	}

	## OS by country
	

	## for testing
	country_code: str = None
	country_code = input(f"input country of choice (FIN/DNK/GRE/ALL): ")
	if country_code == "FIN":
		if finDf is not None:
			print(f"Below you will see the dataframe for Finland:\n{finDf}")
	elif country_code == "DNK":
		if dnkDf is not None:
			print(f"Below you will see the dataframe for Denmark:\n{dnkDf}")
	elif country_code == "GRE":
		if grcDf is not None:
			print(f"Below you will see the dataframe for Greece:\n{grcDf}")
	elif country_code == "all":
		if allDf is not None:
			print(f"Below you will see the dataframe for Greece:\n{allDf}")
	else:
		print("Not a valid country")

if __name__ == "__main__":
	main()