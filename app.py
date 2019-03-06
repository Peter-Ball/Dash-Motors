import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.plotly as py
import plotly.graph_objs as go

#setup
app = dash.Dash(__name__)

df = pd.read_csv("mtcars.tsv", sep='\t', skiprows=4)

#Define the layout
app.layout = html.Div([
	html.H1(children='Dash Motors!'),

	html.Div(children='This application graphs 3 different aspects of the design of 32 car models, and shows how they relate to each other in a 3D scatter plot.'),

	html.P(children='Note: for the scatter plot: x: Miles/Gallon   y: Horsepower   z: Weight (Tons)'),
	html.Div(children='''
		Select a parameter...
		''', className="Instruction"),

	html.Div([
		dcc.Dropdown(
			id='drop-down',
			options=[
			{'label': "Full 3D Scatter", 'value': 'fullscat'},
			{'label': 'Miles/Gallon', 'value': 'mpg'},
			{'label': 'Horsepower', 'value': 'hp'},
			{'label': 'Weight', 'value': 'wt'},
			],
			value='fullscat'
		),
	]),

	dcc.Graph(id='Car Graph'),

	#could not figure out how to make this go away when
	#showing the bar graphs.
	html.Div(children='Colour switcher:'),

	dcc.RadioItems(
		id='colour-radial',
		options=[
		{'label': 'Miles/Gallon', 'value': 'mpg'},
		{'label': 'Horsepower', 'value': 'hp'},
		{'label': 'Weight', 'value': 'wt'},
		],
		value='mpg'
		)
])


#Make the graph
@app.callback(
	Output(component_id='Car Graph', component_property='figure'), 
	[Input(component_id='drop-down', component_property='value'),
	Input(component_id='colour-radial', component_property='value')]
)
def update_figure(value, colour):
	#isolate for the selected parameter
	if (value == 'fullscat'):
		df_slices = df[['model', 'mpg', 'hp', 'wt']]

		return{
			'data': [go.Scatter3d(
				x=df_slices.mpg,
				y=df_slices.hp,
				z=df_slices.wt,
				text=df_slices.model,
				mode='markers',
				marker=dict(
					color=df_slices[colour],
					colorbar=dict(title=colour),
					colorscale='Viridis',
					opacity=0.8
					)
				)],
			'layout': go.Layout(
			)
		}
	else:
		df_segment = df[['model', value]]

		return{
			'data': [go.Bar(
				x=df_segment['model'].tolist(),
				y=df_segment[value].tolist(),
				marker=dict(color='#A387FF')
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