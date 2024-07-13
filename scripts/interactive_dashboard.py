import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import joblib

def load_data(file_path):
    """Load cleaned data for visualization."""
    data = pd.read_csv(file_path)
    return data

def load_models():
    """Load trained models."""
    lin_reg_model = joblib.load('../models/trained_models/linear_regression_model.pkl')
    dt_model = joblib.load('../models/trained_models/decision_tree_model.pkl')
    return lin_reg_model, dt_model

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Predictive Analytics Dashboard"),
    dcc.Dropdown(
        id='model-dropdown',
        options=[
            {'label': 'Linear Regression', 'value': 'LR'},
            {'label': 'Decision Tree', 'value': 'DT'}
        ],
        value='LR'
    ),
    dcc.Graph(id='sales-forecast'),
    html.Div(id='model-metrics')
])

@app.callback(
    [Output('sales-forecast', 'figure'),
     Output('model-metrics', 'children')],
    [Input('model-dropdown', 'value')]
)
def update_dashboard(selected_model):
    data = load_data('../data/processed/sales_data_clean.csv')
    X = data.drop('sales', axis=1)
    y = data['sales']
    
    lin_reg_model, dt_model = load_models()
    
    if selected_model == 'LR':
        predictions = lin_reg_model.predict(X)
        rmse = mean_squared_error(y, predictions, squared=False)
        mae = mean_absolute_error(y, predictions)
        r2 = r2_score(y, predictions)
        model_metrics = f"Linear Regression - RMSE: {rmse}, MAE: {mae}, R²: {r2}"
    else:
        predictions = dt_model.predict(X)
        rmse = mean_squared_error(y, predictions, squared=False)
        mae = mean_absolute_error(y, predictions)
        r2 = r2_score(y, predictions)
        model_metrics = f"Decision Tree - RMSE: {rmse}, MAE: {mae}, R²: {r2}"
    
    fig = px.line(data, x=data.index, y=predictions, title='Sales Forecast')
    return fig, model_metrics

if __name__ == '__main__':
    app.run_server(debug=True)
