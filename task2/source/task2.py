import pandas as pd
import matplotlib.pyplot
from osCountry import osPlot
from parsing import parseDf, findPath, loadCsvData, sliceByCountry
from osSpending import minMaxPurchase, scatterPlotTotalPurchases, plotPurchaseTable
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
	
	# Uncomment below to view users spending behavior
	# scatterPlotTotalPurchases(df)
	# maxDataFrame = minMaxPurchase(df, "min")
	# minDataFrame = minMaxPurchase(df, "max")
	# plotPurchaseTable(maxDataFrame, "(MAX_PURCHASE_VALUE_EUR)")
	# plotPurchaseTable(minDataFrame, "(MIN_PURCHASE_VALUE_EUR)")

	# Uncomment below to view time that it takes from registration day to first purchase
	# firstPurchase(df)

	# Uncomment line below to view OS by country
	# osPlot(df)

	# Uncomment lines bellow to view conversion rate
	# original dataframe
	# originalDf: pd.DataFrame = loadCsvData(findPath())
	# originalDf = sliceByCountry(originalDf)
	# conversionByOs(originalDf, True)


if __name__ == "__main__":
	main()