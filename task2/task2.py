import pandas as pd
from osCountry import osPlot
from parsing import parseDf, findPath, loadCsvData, sliceByCountry
from osSpending import osBySpending
from conversionOs import conversionByOs

def main():
	"""
	Main point of entry of the program. The first line ever is parsing the
	`csv` data that is provided for the assignment. We filter uselesss data, such
	as users that have never made a single purchase, and the three main countries
	(FIN, DNK, GRC) which should provide useful insights.

	The remaining lines are modules that are used for the notebook.
	"""
	# original dataframe
	originalDf: pd.DataFrame = loadCsvData(findPath())
	originalDf = sliceByCountry(originalDf)
	conversionByOs(originalDf)
	exit()

	# clean dataframe
	df: pd.DataFrame = parseDf()

	# OS by country
	osPlot(df)

	# biggest spenders
	osBySpending(df)

if __name__ == "__main__":
	main()