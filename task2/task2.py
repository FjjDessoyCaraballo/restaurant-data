import pandas as pd
from osCountry import osPlot
from parsing import parseDf

def main():
	# extract by country
	df: pd.DataFrame = parseDf()

	## OS by country
	osPlot(df)

	## biggest spenders
	# osBySpending(df)

if __name__ == "__main__":
	main()