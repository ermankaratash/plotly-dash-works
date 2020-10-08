import pandas as pd

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv(r"../Plotly-Dashboards-with-Dash-master/Data/2010YumaAZ.csv")
# print(df.head())
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']