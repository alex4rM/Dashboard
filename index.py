from dash import dcc, html, dash
import plotly.express as px
import pandas as pd
from dash.dependencies import Input,Output

df = pd.read_excel('BD_Dash_Entrega.xlsx')

empleados = df.Empleado.unique()
"""for x in empleados:
    print(x)"""

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.H1('Empleados'),
    ]),

    html.Div([
        html.Div([
            html.P('Selecciona el Empleado'),
            dcc.RadioItems(
                id= 'empleado-item',
                labelStyle = {'display': 'inline-block'},
                    options =[
                        {'label': str(empleados[0]),'value':empleados[0] },
                        {'label': str(empleados[1]),'value':empleados[1] },
                        {'label': str(empleados[2]),'value':empleados[2] },
                        {'label': str(empleados[3]),'value':empleados[3] },
                        {'label': str(empleados[4]),'value':empleados[4] },
                        {'label': str(empleados[5]),'value':empleados[5] },
                        {'label': str(empleados[6]),'value':empleados[6] },
                        {'label': str(empleados[7]),'value':empleados[7] }
                    ], value = empleados[0]
                )
        ]),

        html.Div([
            dcc.Graph(id='grafico1', figure = {})
        ]),
        
        html.Div([
            dcc.Graph(id='pie_grafico', figure={})
        ])
    ])

])

@app.callback(
    Output('grafico1', component_property='figure'),
    [Input('empleado-item', component_property='value')]
)

def update_graph(value):

    if value == str(empleados[0]):
        fig = px.bar(
            data_frame=df,
            x = 'Empleado',
            y = 'Ventas'
        )
    else:
         if value == str(empleados[1]):
            fig = px.bar(
                data_frame=df,
                x = 'Empleado',
                y = 'Ventas'
            )
    
    return fig

if __name__ == ('__main__'):
    app.run_server(
        debug=True
    )