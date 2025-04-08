import pandas as pd
import numpy as np
from osCountry import osPlot
from parsing import parseDf

def main():
	# extract by country
	df: pd.DataFrame = parseDf()

	## OS by country
	osPlot(df)

	# ## for testing
	# country_code: str = None
	# country_code = input(f"input country of choice (FIN/DNK/GRC/all): ")
	# if country_code == "FIN":
	# 	if finDf is not None:
	# 		print(f"Below you will see the dataframe for Finland:\n{finDf}")
	# elif country_code == "DNK":
	# 	if dnkDf is not None:
	# 		print(f"Below you will see the dataframe for Denmark:\n{dnkDf}")
	# elif country_code == "GRC":
	# 	if grcDf is not None:
	# 		print(f"Below you will see the dataframe for Greece:\n{grcDf}")
	# elif country_code == "all":
	# 	if allDf is not None:
	# 		print(f"Below you will see the dataframe for all countries:\n{allDf}")
	# else:
	# 	print("Not a valid country")

if __name__ == "__main__":
	main()