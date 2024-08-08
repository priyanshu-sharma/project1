import pandas as pd

def add_modified_code(csv):
	df = pd.read_csv(csv)
	print("\nInput - \n{}\n".format(df))
	modified_code = []
	for _, r in df.iterrows():
		if '_' in r['targetcode']:
			modified_code.append(r['intermediatecode'] + '_' + r['targetcode'].split('_')[1])
		elif '-' in r['targetcode']:
			modified_code.append(r['intermediatecode'] + '-' + r['targetcode'].split('-')[0])
		else:
			raise NotImplementedError

	df['modifiedcode'] = modified_code
	print("\nOutput - \n{}\n".format(df))
	return df

csv = 'input_two.csv'
add_modified_code(csv)