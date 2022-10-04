Description of what each file/folder contains:

	Final Data
		Contains the final versions of the data files
		Contains the final merge of all data files

	Raw Data
		Contains the original data as downloaded

	Reformatted Data
		Contains file versions after some manual reformatting of columns
		(Also did some equivalent of pivoting)

	DataCleaning.py
		This file allows us to go from Reformatted Data --> Final Data

	DataMerging.py
		This file allows us to take all final files --> EstimatesFinal.csv

	CategoryReduction.py
		This file allows us to transform the categories needed to pivot wider

	DataWidening.Rmd
		This file pivots two files so our final merged file will have fewer rows, more columns