import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

#setup
app = dash.Dash(__name__)

df = pd.read_csv("mtcars.tsv", sep='\t', skiprows=4)

print(df)

#Define the layout
app.layout = html.Div([
	html.H1(children='Dash Motors!'),

	html.Div(children='''
		Select a parameter from the drop-down and it will be visualized for you!
		'''),

	html.Div([
		dcc.Dropdown(
			id='drop-down',
			options=[
			{'label': 'Miles/Gallon', 'value': 'mpg'},
			{'label': 'Horsepower', 'value': 'hp'},
			{'label': 'Weight', 'value': 'wt'},
			],
		),
	]),

	dcc.Graph(id='Car Graph')
])


#Make the graph
@app.callback(
	Output(component_id='Car Graph', component_property='figure'), 
	[Input(component_id='drop-down', component_property='value')]
)
def update_figure(value):
	#isolate for the selected parameter
	df_segment = df[['model', value]]
	
	return{
		'data': [go.Bar(
			x=df_segment['model'].tolist(),
			y=df_segment[value].tolist()
			)],
		'layout': go.Layout(
			xaxis={
				'title': 'Model'
			},
			yaxis={
				'title': value
			}
		)
	}


if __name__ == '__main__':
    app.run_server(debug=True)