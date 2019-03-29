#!/usr/bin/env python
# coding: utf-8

# In[7]:


# making a basic Bokeh line graph

#import Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x = [1,2,3,4,5]
y = [6,7,8,9,10]

#prepare the output file
output_file('BasicLine.html')

#create figure object
fig = figure()

#create line plot, using x & y arrays
fig.line(x,y)

# write the plot to html file & show
show(fig)


# In[8]:


#triangle, circle
dir(fig)


# In[9]:


# exercise 17-195 (i) - plot triangles

# making a basic Bokeh scatter graph with triangular glyph markers

#import Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x = [3, 7.5, 10]
y = [3, 6, 9]

#prepare the output file
output_file('17-195TriangleScatter.html')

#create figure object
fig = figure()

#create **triangle-glyph scatter** plot, using x & y arrays
fig.triangle(x,y)

# write the plot to html file & show
show(fig)


# In[10]:


# exercise 17-195 (ii) - plot circles

# making a basic Bokeh scatter graph with triangular glyph markers

#import Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x = [3, 7.5, 10]
y = [3, 6, 9]

#prepare the output file
output_file('17-195CircleScatter.html')

#create figure object
fig = figure()

#create **circle-glyph scatter** plot, using x & y arrays - see dir(figure)
fig.circle(x,y)

# write the plot to html file & show
show(fig)


# In[11]:


# making a basic Bokeh line graph from pandas

#import Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare some data
df = pandas.read_csv('data.csv')    # read csv file into data frame
x = df['x']      # use x-column of data frame
y = df['y']      # use y-column of data frame

#prepare the output file
output_file('BasicLineFromCSV.html')

#create figure object
fig = figure()

#create line plot, using x & y arrays
fig.line(x,y)

# write the plot to html file & show
show(fig)


# In[12]:


df
# showing data frame, and the columns (series) within


# In[17]:


# 17-198 practice plotting data from CSV
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#read columns into dataframe
dataframe = pandas.read_csv('bachelors.csv')
year_x = dataframe['Year']                          # NB case-sensitive
engineering_students_y = dataframe['Engineering']

# name the output file, ready
output_file('EngineeringStudentsByYear.html')

# instantiate a figure on which to plot
fig = figure()

# plot the line of data
fig.line(year_x, engineering_students_y)

# show the plot by drawing the output file
show(fig)


# In[29]:


# 17-202 practice formatting plot/graph
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

# read columns into dataframe
# scale temperature and pressure down by a factor of 10
dataframe = pandas.read_excel('verlegenhuken.xlsx')    #  sheet_name=None
temperature_x = dataframe['Temperature'].divide(10)
pressure_y = dataframe['Pressure'].divide(10)

output_file('17-202TemperatureAirPressure.html')

# instantiate a figure on which to plot
fig = figure(plot_height=1000, plot_width=1000, tools='pan')

fig.title.text = "Temperature and Air Pressure"
fig.title.text_color = "gray"
fig.title.text_font = "times"
fig.title.text_font_style = "bold"
fig.title.text_font_size = "36pt"
fig.xaxis.axis_label = "Pressure (hPa)"
fig.yaxis.axis_label = "Temperature(°C)"

# draw scatter plot
fig.scatter(temperature_x, pressure_y)

# output result
show(fig)


# In[5]:


#df=pandas.read_csv('http://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C+2009&enddate=Aug+2%2C+2012&output=csv', parse_dates=['Date'])
from bokeh.plotting import figure, output_file, show
import pandas

dataframe=pandas.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&outputsize=full&apikey=<0U1XJSQJG1EXCE3V>&datatype=csv', parse_dates=['timestamp']) 
dataframe  # show inread data, to see, while coding, what columns there are

fig = figure(width=500, height=500, x_axis_type="datetime", sizing_mode='scale_both')

fig.line(dataframe['timestamp'], dataframe['close'], color='Orange', alpha=0.5)  # alpha for transparency

output_file('Timeseries.html')
show(fig)


# See 6MotionDetector for 17-207 & 17-208
