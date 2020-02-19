import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from scipy import signal
import json

import numpy as np
max = 7000000
resample_factor = 25
# get data
url = 'https://mapcore-bucket1.s3-us-west-2.amazonaws.com/ISAN/csv-data/use-case-2/Sample_1_18907001_channel_1.csv'
bigfile = "C:\\Users\jkho021\Downloads\\bigdata.csv"
data = np.loadtxt(bigfile, skiprows=1, usecols=tuple(range(0,3)), delimiter=",", max_rows=max)

data_array = data.view()
data_array = data_array.transpose()
data_array = np.nan_to_num(data_array)

data_resampled = signal.resample(data_array[1], int(max/resample_factor))


with open('resampled.json', 'w') as f:
    json.dump({'data':data_resampled.tolist()}, f)

# Create figure
fig = go.Figure()

fig.add_trace(
    go.Scattergl(
        x = np.linspace(0,len(data_array[1]),len(data_resampled)),
        y = data_resampled,
        mode = 'lines',
        name= 'resampled',

    )
)
fig.add_trace(
    go.Scattergl(
        x = np.linspace(0,len(data_array[1]),len(data_array[1])),
        y = data_array[1],
        name= 'original',
        mode = 'lines',

    )
)

plot(fig)
