import dash
from dash import html

# Create the app
app = dash.Dash(__name__)

app.layout = app.layout = html.Div("مرحبا بالعالم", style={'textAlign': 'center'})

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=9111)
    
