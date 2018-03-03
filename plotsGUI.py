# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 12:40:43 2018

@author: VISHWA
"""

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

df = pd.read_csv('hack.csv')

sample_data_table = FF.create_table(df.head())
py.iplot(sample_data_table, filename='Cryptocuurency data table')


trace1 = go.Scatter(
                    x=df['Time Stamp'], y=df['Bitcoin'], # Data
                    mode='lines', name='Bitcoin' # Additional options
                   )
trace2 = go.Scatter(x=df['Time Stamp'], y=df['Etherium'], mode='lines', name='Etherium' )
trace3 = go.Scatter(x=df['Time Stamp'], y=df['Ripple'], mode='lines', name='Ripple')

layout = go.Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

# Plot data in the notebook
py.iplot(fig, filename='simple-plot-from-csv')
py.plot(fig, filename='simple-plot-from-csv')