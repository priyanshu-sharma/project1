import pandas as pd

def add_country_name(csv, code_name_dict):
	df = pd.read_csv(csv)
	print("\nInput - \n{}\n".format(df))
	country_name = []
	for _, r in df.iterrows():
		country_name.append(code_name_dict[r['countrycode']])

	df['countryname'] = country_name
	print("\nOutput - \n{}\n".format(df))
	return df

csv = 'input.csv'
code_name_dict = {'IND': 'India', 'UKA': 'Ukraine', 'IRN': 'Iran', 'CHA': 'China', 'US': 'United States'}
add_country_name(csv, code_name_dict)