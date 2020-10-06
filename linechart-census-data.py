import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 

df = pd.read_csv(r'C:\Users\KÜRŞAT\Desktop\Desktop\plotly-dash\udemy-course-portillo\Plotly-Dashboards-with-Dash-master\SourceData\nst-est2017-alldata.csv', engine='python')
df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME', inplace=True)

list_of_pop = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop]

data = [go.Scatter(x=df2.columns,
                   y=df2.loc[name],
                   mode='lines',
                   name=name) for name in df2.index]

layout = go.Layout(
            title='US Population Estimates (2010-2017)',
            xaxis=dict(
                title="Year"
            ),
            yaxis=dict(
                title="Population"
            )
)
# print(df2.columns)
# print(df2.index)

# n = [name for name in df2.index]
# print(df2.loc['Connecticut'])
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart-census-data.html')