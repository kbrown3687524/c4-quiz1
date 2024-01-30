import pandas as pd

df = pd.read_csv("data_02/data_02/country_data_index.csv", index_col=0)
#print(df)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
#print(df2)

df2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None, names=column_names)
grouped = df2.groupby('class')
mean_squared_values = grouped['sepal_length'].mean()
sum_squared_values = grouped['sepal_length'].sum()
count_squared_values = grouped['sepal_length'].count()
iris_versicolor = df2[df2['class'] == 'Iris-versicolor']
#print(iris_versicolor)
avg_iris_versicolor = iris_versicolor['sepal_length'].mean()
#print(avg_iris_versicolor)
df2['class'] = df2['class'].str.replace('Iris-', '')
#print("Mean of Sepal Length Squared:", mean_squared_values)
#print("Sum of Sepal Length Squared:", sum_squared_values)
#print("Count of Sepal Length Squared:", count_squared_values)
#print(df2)

df3 = pd.read_csv("data_02/data_02/Geospatial Data.txt", sep=";")
#print(df3) 

df4 = pd.read_excel("data_02/data_02/residentdoctors.xlsx")
#print(df4)
df4["LOWER_AGE"] = df4["AGEDIST"].str.extract('(\d+)-')
df4["LOWER_AGE"] = df4["LOWER_AGE"].astype(int)
#print(df4["LOWER_AGE"])


df5 = pd.read_json("data_02/data_02/student_data.json")
#print(df5)


df6 = pd.read_csv("data_02/data_02/insurance_data.csv", skiprows=5)
#print(df6)

column_names = ["duration", "pulse", "max_pulse", "calories"]
df7 = pd.read_csv("data_02/data_02/patient_data.csv")
#print(df7)


df8 = pd.read_csv("data_02/data_02/time_series_data.csv", index_col=0)
df8['Date'] = pd.to_datetime(df8['Date'])
df8['Year'] = df8['Date'].dt.year
df8['Month'] = df8['Date'].dt.month
df8['Day'] = df8['Date'].dt.day
#print(df8)

df9 = pd.read_csv("data_02/data_02/patient_data_dates.csv")
pd.set_option('display.max_rows', None)
df9.drop(['Index'], inplace=True, axis=1)
x = df9["Calories"].mean()
df9["Calories"].fillna(x, inplace=True)
df9['Date'] = pd.to_datetime(df9['Date'], format='mixed')
df9.dropna(subset=['Date'], inplace = True)
df9 .loc[7, 'Duration']=45
df9.drop_duplicates(inplace=True)
df9 = df9.reset_index(drop=True)
print(df9)

df10 = pd.read_csv("data_02/data_02/person_split1.csv")
df11 = pd.read_csv("data_02/data_02/person_split2.csv")
#print(df10)
#print(df11)
df12 = pd.concat([df10,df11], ignore_index=True)
#print(df12)


df13 = pd.read_csv("data_02/data_02/person_education.csv")
df14 = pd.read_csv("data_02/data_02/person_work.csv")
df_merged = pd.merge(df13,df14, on="id", how='outer')
#print(df_merged)

