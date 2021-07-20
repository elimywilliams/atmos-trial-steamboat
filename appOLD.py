# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
#from dash.dependencies import Input, Output
import plotly.express as px
#import base64
import json
#from textwrap import dedent as d
import bs4 as bs
import dash_html_components as html
import requests 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/header2.css'  ,
                        'https://github.com/plotly/dash-app-stylesheets/blob/master/dash-oil-and-gas.css'
                        ]
px.set_mapbox_access_token('pk.eyJ1IjoiZXdpbGxpYW1zMjAyMCIsImEiOiJja2FpdTIxOXMwM2wzMnFtbmVmb3IzZDJ6In0.TVsQ-iu8bN4PQLkBCr6tQQ')

allLeaks = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allLeaks.csv')



import plotly.express as px
import plotly.io as pio

fig = px.scatter_mapbox(allLeaks, lat="Latitude", lon="Longitude",  color="LEAKNUM",
                   color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                   hover_data = {'POLYGON','LEAKNUM'})
# fig.show()



projOPTS = [
            {'label': 'ACLARA (NY)', 'value': 'Aclara'},
            {'label': 'Con Edison', 'value': 'ConEd'},
            #{'label': 'CPS (TX)', 'value': 'CPS_TX'},

            {'label': 'Dom Questar (UT)', 'value': 'DomQuest'},
            
            #{'label': 'Dominion (NC)', 'value': 'DominionNC'},
            #{'label': 'Dominion (SC)', 'value': 'DominionSC'},
            
            {'label': 'Duke IPI', 'value': 'DukeIPI'},
            {'label': 'Duke Ohio', 'value': 'DukeOH'},
            {'label': 'Norwhich Public Utilities', 'value': 'norwhich'},

            {'label': 'Peoples (IL)', 'value': 'PeoplesIL'},
            #{'label': 'Trussville (AL)', 'value': 'Trussville'},

            {'label': 'WEC Energy (WI)', 'value': 'WEC_WI'},
            {'label': 'WPS MMD (WI)', 'value': 'WPS_WI'}
        ]

whichAvgOPTS = [
        {'label': '7 Day Avg ', 'value': 'sevenday'},
        {'label': '3 Day Avg', 'value': 'threeday'},
        {'label': 'Daily ', 'value': 'daily'},
        {'label': 'Cumulative ','value':'total'}
    ]

popOPTS = [
    {'label':'Relative to Population','value':'relpop'},
    {'label':'Raw Cases', 'value':'nonrelpop'}
    
    
    ]

countryOPTS = [
            {'label': 'United States of America', 'value': 'US'},
            {'label': 'Italy', 'value': 'Italy'},

            {'label': 'Spain', 'value': 'Spain'},
            {'label': 'United Kingdom', 'value': 'United Kingdom'},

            {'label': 'Australia', 'value': 'Australia'},

            
            {'label': 'Sweden', 'value': 'Sweden'},
            {'label': 'Switzerland', 'value': 'Switzerland'},
            {'label': 'Austria', 'value': 'Austria'},
            {'label': 'France', 'value': 'France'},
            {'label': 'Germany', 'value': 'Germany'},
            {'label': 'Turkey', 'value': 'Turkey'},
            
            {'label': 'New Zealand', 'value': 'New Zealand'},
            ]

stateOPTS = [
    {'label':'Polygon 1','value':"P1"},
    {'label':'Polygon 2','value':"P2"},
    {'label':'Polygon 3','value':"P3"},
    {'label':'Polygon 4','value':"P4"}
    ]


tab1=html.Div([
    html.Div(
            [
                html.Div(
                    [

                        html.P("Choose Polygon:", className="control_label"),
                       dcc.Dropdown(
                            id="whichPoly",
                            #options=well_status_options,
                            options = stateOPTS,
                            #multi=True,
                            #value=list(WELL_STATUSES.keys()),
                            value = 'P1',
                            className="dcc_control",
                        ),
                        #html.P("Choose Related City:", className="control_label"),
                        #dcc.Dropdown(
                        #    id="whichCity",
                            #options=[{'label':opt, 'value':opt} for opt in stat_nestedOptions],
                            #value = stat_nestedOptions[0],
                            #options=well_type_options,
                            #multi=True,
                            #value=list(WELL_TYPES.keys()),
                         #   className="dcc_control",
                        #),
                       # dcc.RadioItems(
                       #     id="whichavgstate",
                       #     options=whichAvgOPTS,
                       #     value="sevenday",
                       #     labelStyle={"display": "inline-block"},
                       #     className="dcc_control"
                            
                       # ),
                       # dcc.RadioItems(
                       #     id="popratiostate",
                       #     options=popOPTS,
                       #     value="nonrelpop",
                       #     labelStyle={"display": "inline-block"},
                       #     className="dcc_control",
                       # ),
                        
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options-state",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                 html.Div(
                                     [html.H6(id="well_text"), html.P("Polygon:")],
                                     id="polygon",
                                     className="mini_container",
                                 ),
                                 html.Div(
                                     [html.H6(id="gasText"), html.P("Status:")],
                                     id="polygonLks",
                                     className="mini_container",
                                 ),
                                # html.Div(
                                #     [html.H6(id="oilText"), html.P("")],
                                #     id="oil",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="waterText"), html.P("")],
                                #     id="water",
                                #     className="mini_container",
                                # ),
                            ],
                            id="info-container-state",
                            className="row container-display",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="leakGraph")],
                    className="pretty_container seven columns",
                ),
                #html.Div(
                #    [dcc.Graph(id="statePredGraph")],
                #    className="pretty_container five columns",
                #),
                html.Div(
                    [dcc.Graph(id='hover-data-plot')],#,id="hover-data-plot")],
                    className="pretty_container five columns"),
            ],
            className="row flex-display",
        ),
        html.Div(
             [
                 html.Div(id='hover-data-info',
                     #[dcc.Markdown(id="hover-data-info")],
                     className="pretty_container seven columns",
                 ),
        #         html.Div(
        #             [dcc.Graph(id="aggregate_graph")],
        #             className="pretty_container five columns",
        #         ),
             ],
             className="row flex-display",
         )
        ])

tab2=html.Div([
    html.Div(
            [
                html.Div(
                    [

                        html.P("Choose State Specific Information:", className="control_label"),
                       dcc.Dropdown(
                            id="whichState",
                            #options=well_status_options,
                            options = stateOPTS,
                            #multi=True,
                            #value=list(WELL_STATUSES.keys()),
                            value = 'CO',
                            className="dcc_control",
                        ),
                        #html.P("Choose Related City:", className="control_label"),
                        #dcc.Dropdown(
                        #    id="whichCity",
                            #options=[{'label':opt, 'value':opt} for opt in stat_nestedOptions],
                            #value = stat_nestedOptions[0],
                            #options=well_type_options,
                            #multi=True,
                            #value=list(WELL_TYPES.keys()),
                         #   className="dcc_control",
                        #),
                        dcc.RadioItems(
                            id="whichavgstate",
                            options=whichAvgOPTS,
                            value="sevenday",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control"
                            
                        ),
                        dcc.RadioItems(
                            id="popratiostate",
                            options=popOPTS,
                            value="nonrelpop",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                        
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options-state",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                # html.Div(
                                #     [html.H6(id="well_text"), html.P("State:")],
                                #     id="stateName",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="gasText"), html.P("Status:")],
                                #     id="stateStatus",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="oilText"), html.P("")],
                                #     id="oil",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="waterText"), html.P("")],
                                #     id="water",
                                #     className="mini_container",
                                # ),
                            ],
                            id="info-container-state",
                            className="row container-display",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="state_graph")],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id='hover-data-plot')],#,id="hover-data-plot")],
                    className="pretty_container five columns"
                ),
            ],
            className="row flex-display",
        ),
        # html.Div(
        #     [
        #         html.Div(
        #             [dcc.Graph(id="pie_graph2")],
        #             className="pretty_container seven columns",
        #         ),
        #         html.Div(
        #             [dcc.Graph(id="aggregate_graph")],
        #             className="pretty_container five columns",
        #         ),
        #     ],
        #     className="row flex-display",
        # )
        ])

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True,
                 meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

server=app.server

app.layout = html.Div(
    [
        dcc.Store(id="aggregate_data"),
        html.Div(id="output-clientside"),
        html.Div(
            [
                html.Div(
                    [
                        #html.Img(
                        #    src = img,
                            #src='data:image/png;base64,{}'.format(encoded_image.decode()),
                         #   id="plotly-image",
                         #   style={
                         #       "height": "60px",
                         #       "width": "auto",
                         #       "margin-bottom": "25px",
                         #   },
                       # )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Southern Cross Gap and Leak Indication",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Trussville, AL", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Last Updated",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    '6.19.20', style={"margin-top": "0px"}
                                ),
                              dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
                                  dcc.Tab(id="tab-1", label='Leak Indications', value='tab-1-example'),
                                  #dcc.Tab(id="tab-2", label='State', value='tab-2-example'),
                                 # dcc.Tab(id= 'tab-4',label = 'Weekly Info',value = 'tab-4-example')
                                  ])

                            ]
                        )
                    ],
                    className="one-fourth row",
                    id="title2",
                ),

                
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(id='tabs-content-example',
             children = tab1),
       
        
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column",'backgroundColor':'white'},
)


@app.callback(dash.dependencies.Output('tabs-content-example', 'children'),
             [dash.dependencies.Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab1
    #elif tab == 'tab-2-example':
    #    return tab2
    #elif tab == 'tab-4-example':
    #    return tab4

@app.callback(dash.dependencies.Output('leakGraph', 'figure'),
              [dash.dependencies.Input('whichPoly', 'value')]
              )
def update_polyLeak(whichPolygon):
    usedat = allLeaks.loc[allLeaks.POLYGON == whichPolygon,:]
    fig = px.scatter_mapbox(usedat, lat="Latitude", lon="Longitude",  
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                  hover_data = {'PolyLK'})
    fig.update_layout(
        autosize=True,
        width = 800,
        height = 800,
        showlegend = False
        )
    fig.update()
    return fig

@app.callback(
    dash.dependencies.Output('hover-data-plot', 'figure'),
    [dash.dependencies.Input('leakGraph', 'hoverData')])
def updatePlot(hoverData):
     plk = hoverData['points'][0]['customdata'][0]
     dat = allLeaks[allLeaks.PolyLK==str(plk)]
     #dat=allLeaks
     title = "Leak " + str(int(dat.reset_index().LEAKNUM)) + '. '+ " Location: " + str(float(dat.reset_index().loc[0,['Longitude']])) + ',' + str(float(dat.reset_index().loc[0,['Latitude']]))
     fig = px.scatter_mapbox(dat, lat="Latitude", lon="Longitude", 
                   size_max=25, zoom=15,
                  hover_data = {'PolyLK'})
                                                  
     fig.update_layout(
        autosize=True,
        width = 800,
        height = 800,
        title =title
        )
     fig.update_traces(marker = dict(size = 20))
     fig.update()
     return fig

@app.callback(
    dash.dependencies.Output('hover-data-info', 'children'),
    [dash.dependencies.Input('leakGraph', 'hoverData')])
def updatename(hoverData):
     plk = hoverData['points'][0]['customdata']
     title = plk
     return title
 
@app.callback(dash.dependencies.Output('polygon', 'children'),
              [dash.dependencies.Input('whichPoly', 'value')]
              )
def updateText(whichPolygon):
    return "Polygon " + str(whichPolygon[1:])

@app.callback(dash.dependencies.Output('polygonLks', 'children'),
              [dash.dependencies.Input('whichPoly', 'value')]
              )
def updatePolyLk(whichPolygon):
    dat = allLeaks[allLeaks.POLYGON==str(whichPolygon)]
    return "Number of Leaks: " + str(dat.shape[0])

    
if __name__ == '__main__':
    app.run_server(debug=False)



                
