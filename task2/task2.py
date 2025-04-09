import pandas as pd
import matplotlib.pyplot
from osCountry import osPlot
from parsing import parseDf, findPath, loadCsvData, sliceByCountry
from osSpending import osBySpending
from conversionOs import conversionByOs
from firstPurchase import firstPurchase

def main():
	"""
	Main point of entry of the program. The first line ever is parsing the
	`csv` data that is provided for the assignment. We filter uselesss data, such
	as users that have never made a single purchase, and the three main countries
	(FIN, DNK, GRC) which should provide useful insights.

	The remaining lines are modules that are used for the notebook.
	"""
	# clean dataframe
	df: pd.DataFrame = parseDf()
	firstPurchase(df)

	# OS by country
	# osPlot(df)

	# original dataframe
	# originalDf: pd.DataFrame = loadCsvData(findPath())
	# originalDf = sliceByCountry(originalDf)
	# conversionByOs(originalDf, True)

	# How long it takes for a first purchase
	 

	# biggest spenders
	# osBySpending(df)

	# next in line: frequency

if __name__ == "__main__":
	main()