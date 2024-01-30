import pandas as pd
import os
path = "/home/akuma/css2024/css2024_day1/data_01/data_01/"
for file in os.listdir(path):	
	if file.endswith('.csv'):
		print(file)
		file_data = pd.read_csv(path+file)
		print(file_data.info())
		print(file_data.describe())

"""data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}
"""
#df = pd.DataFrame(data)

#print(df['age'])
#print(df['gender'])
#print(df['age'].min())
#print(df['age'].max())
#print(df['age'].mean())

#print(df[df['age']>30])

#print(df[1:4])

#df["new column"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#df.drop(columns=["new column"], inplace=True)
#print(df)

