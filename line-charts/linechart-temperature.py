import pandas as pd
import plotly.offline as pyo 
import plotly.graph_objs as go 

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv(r"../Plotly-Dashboards-with-Dash-master/Data/2010YumaAZ.csv")
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']

# Use a for Loop (or List comprehensive to create traces for the data list)
data = []

for day in days:
    # What should go inside this Scatter call?
    trace = go.Scatter(x=df['LST_TIME'],
                      y=df[df['DAY'] == day]['T_HR_AVG'],
                      mode='lines',
                      name=day
                      )
    data.append(trace)

#Alternative with list comp
""" data = [{
    'x' : df['LST_TIME'],
    'y' : df[df['DAY'] == day]['T_HR_AVG'],
    'name' : day
} for day in df['DAY'].unique() ]
 """
# Define the layout
layout = go.Layout(
            title='Daily temp avgs',
            xaxis=dict(
                title="Hour"
            ),
            yaxis=dict(
                title="Average Temp"
            )
)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart-census-data.html')