import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

def load_data(file_path):
    """Load cleaned data for modeling."""
    data = pd.read_csv(file_path)
    return data

def split_data(data):
    """Split data into training and testing sets."""
    X = data.drop('sales', axis=1)
    y = data['sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_linear_regression(X_train, y_train):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def train_decision_tree(X_train, y_train):
    """Train a decision tree model."""
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model performance."""
    predictions = model.predict(X_test)
    rmse = mean_squared_error(y_test, predictions, squared=False)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return rmse, mae, r2

if __name__ == "__main__":
    file_path = '../data/processed/sales_data_clean.csv'
    data = load_data(file_path)
    
    X_train, X_test, y_train, y_test = split_data(data)
    
    lin_reg_model = train_linear_regression(X_train, y_train)
    dt_model = train_decision_tree(X_train, y_train)
    
    lin_reg_metrics = evaluate_model(lin_reg_model, X_test, y_test)
    dt_model_metrics = evaluate_model(dt_model, X_test, y_test)
    
    print(f"Linear Regression - RMSE: {lin_reg_metrics[0]}, MAE: {lin_reg_metrics[1]}, R²: {lin_reg_metrics[2]}")
    print(f"Decision Tree - RMSE: {dt_model_metrics[0]}, MAE: {dt_model_metrics[1]}, R²: {dt_model_metrics[2]}")
    
    joblib.dump(lin_reg_model, '../models/trained_models/linear_regression_model.pkl')
    joblib.dump(dt_model, '../models/trained_models/decision_tree_model.pkl')
