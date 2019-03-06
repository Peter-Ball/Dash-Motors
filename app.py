import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

df = pd.read_csv("mtcars.tsv", sep='t')

app.layout = html.Div([
	html.H1(children='Dash Motors!'),

	html.Div(children='''
		Select a parameter from the drop-down and it will be visualized for you!
		'''),

	html.Div([
		dcc.Dropdown(
			options=[
			{'label': 'Miles/Gallon', 'value': 'mpg'},
			{'label': 'Horsepower', 'value': 'hp'},
			{'label': 'Weight', 'value': 'wt'},
			],
		),
	]),

	dcc.Graph(id='Car Graph')
])

if __name__ == '__main__':
    app.run_server(debug=True)