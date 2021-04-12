#! python3
import pandas as pd

col_names=['Row', 'LC', 'Member', 'End', 'Axial', 'Vy', 'Vz', 'Mx', 'My', 'Mz']
# read in RISA-3D flat file.  Note that empty values are a string with two ' characters,
# so in order for it to read those in properly, the string "''" is included in na_values.
# This is needed in order to forward propagate load combination numbers and member names.
df = pd.read_table('forces.txt', na_values=["''"], delimiter=',', header=0, names=col_names, index_col=0)

# forward pad load combination numbers to replace NaN and convert column to int
df['LC'] = df['LC'].fillna(method='pad')
df['LC'] = df['LC'].astype('int')

# remove single apostrophe on each end of member labels and forward propagate labels to replace NA
df['Member'] = df['Member'].str.strip("'")
df['Member'] = df['Member'].fillna(method='pad')
print(df.head())
print(df.tail())

#will use 1.6+million lines, need to dump in two files

#df.to_csv(open(''))