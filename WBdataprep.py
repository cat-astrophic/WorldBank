# This script converts an input list of variables from World Bank data into a panel dataset

# Importing required modules

import pandas as pd

# Specifying the location of the World Bank data file

fp = input('Filepath for World Bank data file: ')

# Reading in the data

wb = pd.read_csv(fp)
paneldf = pd.DataFrame()

# Specifying the data you are want

n = input('Input desired number of data fields: ')

for i in range(int(n)):
    
    f = input('Input name of data field ' + str(i+1) + ' of ' + str(n) + ': ')
    t = wb[wb['Indicator Name'] == f]
    t1 = [c for c in list(t['Country Name'])]*61
    t2 = [1960 + i for i in range(61) for c in list(t['Country Name'])]
    t3 = [x for y in range(1960,2021) for x in list(t[str(y)])]
    paneldf = pd.concat([paneldf, pd.Series(t3, name = f)], axis = 1)

paneldf = pd.concat([pd.Series(t1, name = 'Country Name'), pd.Series(t2, name = 'Year'), paneldf], axis = 1)

rowdrops = ['Arab World', 'Caribbean small states', 'Central Europe and the Baltics',
'Early-demographic dividend', 'East Asia & Pacific', 'East Asia & Pacific (excluding high income)',
'East Asia & Pacific (IDA & IBRD countries)', 'Euro area', 'Europe & Central Asia',
'Europe & Central Asia (excluding high income)', 'Europe & Central Asia (IDA & IBRD countries)',
'European Union', 'Fragile and conflict affected situations', 'Heavily indebted poor countries (HIPC)',
'High income', 'IBRD only', 'IDA & IBRD total', 'IDA blend', 'IDA only', 'IDA total',
'Late-demographic dividend', 'Latin America & Caribbean', 'Latin America & Caribbean (excluding high income)',
'Latin America & the Caribbean (IDA & IBRD countries)', 'Least developed countries: UN classification',
'Low & middle income', 'Low income', 'Lower middle income', 'Middle East & North Africa',
'Middle East & North Africa (excluding high income)', 'Middle East & North Africa (IDA & IBRD countries)',
'Middle income', 'North America', 'Not classified', 'OECD members', 'Other small states',
'Pacific island small states', 'Post-demographic dividend', 'Pre-demographic dividend',
'Small states', 'South Asia', 'South Asia (IDA & IBRD)', 'Sub-Saharan Africa',
'Sub-Saharan Africa (excluding high income)', 'Sub-Saharan Africa (IDA & IBRD countries)',
'Upper middle income', 'World'] # Rermoving non-nations from the data

rowkeeps = [c for c in list(set(t1)) if c not in rowdrops]

paneldf = paneldf[paneldf['Country Name'].isin(rowkeeps)]

# Saving data to file

s = input('Where would you like this file to be saved? ')
paneldf.to_csv(s, index = False)

