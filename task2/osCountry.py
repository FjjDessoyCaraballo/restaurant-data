import pandas as pd
import matplotlib.pyplot as plt

def registrationComparedToOs(df: pd.DataFrame):
	"""
	Filter to extract two variables to visualize in a table
	
	:Parameters:
	df
		Pandas dataframe containing csv file provided previously
	
	:Returns (1): 
	deviceCounts
		percentage number of users OS by country

	:Returns (2): 	
	deviceAbs 
		absolute number of users OS by country
	"""
	reg_country = df['REGISTRATION_COUNTRY']
	device = df['PREFERRED_DEVICE']
	
	# percentage of users OS by country
	deviceCounts = pd.crosstab(
		reg_country,
		device,
		normalize='index') * 100
	
	# brute users OS by country
	deviceAbs = pd.crosstab(
		reg_country,
		device
	)
	return deviceCounts, deviceAbs

def visualizeOsByCountry(deviceCounts, deviceAbs):
	"""
	Function that enables visualization of tables

	:Parameters:
	deviceCounts
		Percentage value of users device OS
	
	:Paramterers:
	deviceAbs
		Brute value of users device OS


	"""
	fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

	deviceCounts.plot(kind='bar', ax=ax1)
	ax1.set_title('Device preference by country (%)', fontsize=14, pad=20)
	ax1.set_xlabel('Country', fontsize=12)
	ax1.set_ylabel('Percentage', fontsize=12)

	# spacing between plots
	for tick in ax1.get_xticklabels():
		tick.set_rotation(45)

	ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
	deviceAbs.plot(kind='bar', ax=ax2)
	ax2.set_title('Device preference by country (absolute)', fontsize=14, pad=20)
	ax2.set_xlabel('Country', fontsize=12)
	ax2.set_ylabel('Count', fontsize=12)

	# more spacing
	for tick in ax2.get_xticklabels():
		tick.set_rotation(45)

	# adjustments that go easier on the eye
	ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
	plt.subplots_adjust(hspace=0.4)
	plt.tight_layout(pad=3.0)
	fig.set_tight_layout(True)
	plt.show()

def osPlot(df: pd.DataFrame):
	"""
	Staging area to visualize tables of users OS by country.

	:Parameters:
	df
		Pandas dataframe containing csv file provided previously
	"""
	deviceCounts, deviceAbs = registrationComparedToOs(df)
	visualizeOsByCountry(deviceCounts, deviceAbs)