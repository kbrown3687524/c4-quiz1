import matplotlib.pyplot as plt
import plotly.express as px

x_line =  [1,2,3,4,5]
y_line = [2,4,6,8,10]

plt.plot(x_line, y_line, '-o')
plt.xlabel('x_line')
plt.ylabel('y_line')

plt.title('Line Plot')
#plt.show()


fig = px.scatter(x=x_line, y=y_line, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Scatter Plot')
fig.write_html("plot.html")

import webbrowser
webbrowser.open("plot.html")
