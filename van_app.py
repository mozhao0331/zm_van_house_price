from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import altair as alt

# Read data
df = pd.read_csv("data/van_house_data.csv")

# data process
# df = df = df.sample(n=4000, random_state=123)
df = df.sort_values('YEAR_BUILT')
df['REPORT_YEAR'] = df['REPORT_YEAR'].astype('category')
df['YEAR_BUILT'] = df['YEAR_BUILT'].astype('category')

# levels
report_year = df['REPORT_YEAR'].unique()
legal_type = df['LEGAL_TYPE'].unique()
year_built = df['YEAR_BUILT'].unique()

# Build the components
app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

app.layout = (
    html.Div(
        children=[
            html.Div(
                children=[
                    # create title
                    html.H1(
                        children="Vancouver Houses Price Analytics Dashboard", className="Title"
                    ),
                    # create subtitle
                    html.P(
                        children="(Data from 2020 to 2023)", className="Sub-Title",
                    ),
                ],
                className="headers",
            ),
        
        # Create Dropdown
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Year Built", className="menu-drop"),
                        dcc.Dropdown(id='year_built',
                            options=year_built,
                            value=1999)
                    ]
                ),
            ],
        ),
        
        # create slide bar for price
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children="Price Range", className="menu-slide"),
                        dcc.Slider(
                            id='price_range', 
                            min=300000, 
                            max=5000000,
                            step=1000,
                            value=5000000,
                            marks={i: str(i) for i in range(300000, 5000000, 500000)},
                            className="slidebar",
                        ),
                    ]
                ),
            ],
        ),
        
        # plots
        html.Div(
            children=[
                # first plot
                html.Iframe(
                    id='plot1',
                    style={'border-width': '20',
                        'width': '60%', 
                        'height': '200px'}),
                
                # second plot
                html.Iframe(
                    id='plot2',
                    style={'border-width': '20',
                        'width': '60%', 
                        'height': '200px'})
            ],
        ),
    ]
))

# create callback
@app.callback(
    Output('plot1', 'srcDoc'),
    Output('plot2', 'srcDoc'),
    Input('year_built', 'value'),
    Input('price_range', 'value'))

# plots function
def plot_altair(year_built, price_range):
    
    df_filtered = df[(df['CURRENT_LAND_VALUE'] <= price_range) & (df['YEAR_BUILT'] == year_built)]
    
    chart1 = alt.Chart(df_filtered).mark_bar().encode(
        x=alt.X("CURRENT_LAND_VALUE", title="Current Land Value"),
        y=alt.Y("REPORT_YEAR", title="Report Year"),
        tooltip='CURRENT_LAND_VALUE'
    ).properties(
        title="Land Value by Year"
    )
    
    chart2 = alt.Chart(df_filtered).mark_bar().encode(
        x=alt.X("CURRENT_LAND_VALUE", title="Current Land Value"),
        y=alt.Y("LEGAL_TYPE", title="Legal Type"),
        tooltip='CURRENT_LAND_VALUE'
    ).properties(
        title="Land Value by Legal Type"
    )
    
    return chart1.to_html(), chart2.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)