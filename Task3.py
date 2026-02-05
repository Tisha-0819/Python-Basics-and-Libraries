# Task 3: Load a CSV file with Pandas, 
# clean it (handle missing values), and export a summary.

import pandas as pd

data = pd.read_csv('data.csv')
# Read TAB separated file
Score = data['Score'].min()  

data.fillna({'Score':Score}, inplace=True)
data['Score'] = data['Score'].astype(int)


print(data)
