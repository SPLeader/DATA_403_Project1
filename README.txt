Description of what each file/folder contains:

	Beta Estimates
		
		Within this folder are data files containing different beta 
		estimates for different train/validation splits. We use the
		data in this folder to analyze how sensitive our model is
		to the input data.

	Data Cleaning

		Within this folder are python and R scripts that we used to manipulate
		and clean the raw data. It involves data pivots, removing nulls, and 
		cleaning up county names, among many other things.

		We do not recommend running any of the files in here, because 
		data is not in the proper directories for the code to run.

	Data

		Within this folder are all the data files we used. It contains the
		final versions of data, the raw data we reformatted, as well as the 
		final population estimates data.

	Model Building

		Within this folder are the python scripts we used to manually 
		implement linear regression. There is also code here used to do
		the EDA as well as best subsets.