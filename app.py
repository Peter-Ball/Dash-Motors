import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

df = pd.read_csv("mtcars.tsv", sep='t')