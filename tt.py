import numpy as np
import plotly.graph_objects as go
from scipy.signal import find_peaks,argrelmin

import requests


data = []
response = requests.get("https://api.binance.com/api/v3/klines?symbol=DNTUSDT&interval=4h")
res = response.json()
for x in res:
    #print(datetime.datetime.fromtimestamp(x[0]/1000), x[2])
    data.append(x[2])


data = np.array(data, dtype='float16')

indices = find_peaks(data, distance=20)[0]

min = find_peaks(data*(-1), distance=20)[0]

mmax = [data[j] for j in indices]
mmin = [data[j] for j in min]

print(indices)
print(min)

fig = go.Figure()
fig.add_trace(go.Scatter(
    y =data,
    mode='lines+markers',
    name='Original Plot'
))

for j in indices:


        fig.add_trace(go.Scatter(
            x=[j],
            y=[data[j]],
            mode='markers',
            marker=dict(
                size=8,
                color='red',
                symbol='cross'
            ),
            name='Detected Peaks'
        ))

for k in min:

        fig.add_trace(go.Scatter(
            x=[k],
            y=[data[k]],
            mode='markers',
            marker=dict(
                size=8,
                color='green',
                symbol='cross'
            ),
            name='Detected Peaks22'
        ))


fig.show()
