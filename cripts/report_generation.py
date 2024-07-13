import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import pdfkit

def load_data(file_path):
    """Load cleaned data for reporting."""
    data = pd.read_csv(file_path)
    return data

def load_models():
    """Load trained models."""
    lin_reg_model = joblib.load('../models/trained_models/linear_regression_model.pkl')
    dt_model = joblib.load('../models/trained_models/decision_tree_model.pkl')
    return lin_reg_model, dt_model

def generate_report(data, lin_reg_model, dt_model):
    """Generate a detailed report."""
    X = data.drop('sales', axis=1)
    y = data['sales']
    
    lin_reg_predictions = lin_reg_model.predict(X)
    dt_predictions = dt_model.predict(X)
    
    lin_reg_metrics = {
        'RMSE': mean_squared_error(y, lin_reg_predictions, squared=False),
        'MAE': mean_absolute_error(y, lin_reg_predictions),
        'R²': r2_score(y, lin_reg_predictions)
    }
    
    dt_metrics = {
        'RMSE': mean_squared_error(y, dt_predictions, squared=False),
        'MAE': mean_absolute_error(y, dt_predictions),
        'R²': r2_score(y, dt_predictions)
    }
    
    report_html = f"""
    <html>
    <head><title>Predictive Analytics Report</title></head>
    <body>
    <h1>Predictive Analytics Report</h1>
    <h2>Linear Regression Model</h2>
    <p>RMSE: {lin_reg_metrics['RMSE']}</p>
    <p>MAE: {lin_reg_metrics['MAE']}</p>
    <p>R²: {lin_reg_metrics['R²']}</p>
    
    <h2>Decision Tree Model</h2>
    <p>RMSE: {dt_metrics['RMSE']}</p>
    <p>MAE: {dt_metrics['MAE']}</p>
    <p>R²: {dt_metrics['R²']}</p>
    </body>
    </html>
    """
    
    with open('../reports/predictive_analytics_report.html', 'w') as file:
        file.write(report_html)
    
    pdfkit.from_file('../reports/predictive_analytics_report.html', '../reports/predictive_analytics_report.pdf')

if __name__ == "__main__":
    file_path = '../data/processed/sales_data_clean.csv'
    data = load_data(file_path)
    
    lin_reg_model, dt_model = load_models()
    
    generate_report(data, lin_reg_model, dt_model)
