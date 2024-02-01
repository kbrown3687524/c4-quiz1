import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns



df = pd.read_csv("movie_dataset.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
for column in df:
	#print(column)
	if ' ' in column:
		new_name = column.replace(' ', '')
		df.rename(columns={column:new_name}, inplace=True)
for column in df:
	#print(column)
	column_type = df[column].dtypes
	if column_type == 'float64':
		x_val = df[column].mean()
		df[column].fillna(x_val, inplace=True)	
df2 = df.sort_values(by='Rating', ascending=False)
revenue = df['Revenue(Millions)'].mean()
#print(df2)
#print(revenue)
#df3 = df.sort_values(by='Year', ascending=True)
df3 = (df.loc[(df['Year'] >= 2015) & (df['Year'] <= 2017)])
#print(df3['Revenue(Millions)'].mean())

df4 = df.loc[df['Year'] == 2016]
#print(df4['Year'].count())

df5 = df.loc[df['Director']== 'Christopher Nolan']
#print(df5['Director'].count())
#print(df5)
#print(df5['Rating'].mean())

df6 = df.loc[df['Rating'] >= 8.0]
#print(df6['Rating'].count())

min_year = df['Year'].min()
max_year = df['Year'].max()

#print(min_year, max_year)
highest_rate = {}
for i in range(min_year,max_year + 1):
	highest_rate.setdefault('year',[]).append(i)
	df7 = df.loc[df['Year'] == i]
	avg_year_rating = df7['Rating'].mean()
	year_count = df7['Year'].count()
	highest_rate.setdefault('avg_rating',[]).append(avg_year_rating)
	highest_rate.setdefault('year_count',[]).append(year_count)
df8 = pd.DataFrame.from_dict(highest_rate)

#print(df8.sort_values(by='avg_rating', ascending = False))

#print(df8)
year_2006 = df8.loc[df8['year']== 2006]
year_2016 = df8.loc[df8['year'] == 2016]

#print(year_2016)
#print(year_2006)


all_actors_in_all_movies = []
for i in range(len(df)):
	actors = (df['Actors'].iloc[i,]).split(',')
	for i in actors:
		all_actors_in_all_movies.append(i.replace(' ', '').lower())
	
a = dict(Counter(all_actors_in_all_movies))

highest_movie = 0
highest_actor = ''
for key in a:
	if a[key] > highest_movie:
		highest_movie = a[key]
		print(key, highest_movie)


all_genres_in_all_movies = []
for i in range(len(df)):
        genres = (df['Genre'].iloc[i,]).split(',')
        for i in genres:
                all_genres_in_all_movies.append(i.replace(' ', '').lower())

new_list = []
for i in all_genres_in_all_movies:
	if i not in new_list:
		new_list.append(i)

#print(len(new_list))

#plt.bar(df['Revenue(Millions)'], df['Metascore'])
#plt.show()
#fig = px.scatter(x=df['Revenue(Millions)'], y=df['Metascore'], labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Scatter Plot')
#fig.write_html("plot.html")


#sns.lmplot(x="Revenue(Millions)", y="Metascore", data=df);
#sns.lmplot(x="Runtime(Minutes)",y="Metascore", data=df)
#sns.lmplot(x="Runtime(Minutes)",y="Rating", data=df)
#sns.lmplot(x="Revenue(Millions)",y="Rating", data=df)
#print(df)
plt.show()


df_iso = df.iloc[:,7:-1]
print(df_iso)

df_iso = df_iso.astype(float)
df_matrix = df_iso.corr()
print(df_matrix)

sns.heatmap(df_matrix);
plt.show()
