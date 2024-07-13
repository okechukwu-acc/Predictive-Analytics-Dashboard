import pandas as pd
import numpy as np

def load_data(file_path):
    """Load data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Clean the dataset."""
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    
    # Convert data types if necessary
    # Example: data['date'] = pd.to_datetime(data['date'])
    
    # Remove outliers (optional)
    # Example: data = data[(data['sales'] > lower_bound) & (data['sales'] < upper_bound)]
    
    return data

def preprocess_data(file_path):
    """Load, clean, and preprocess data."""
    data = load_data(file_path)
    clean_data = clean_data(data)
    return clean_data

if __name__ == "__main__":
    file_path = '../data/raw/sales_data.csv'
    processed_data = preprocess_data(file_path)
    processed_data.to_csv('../data/processed/sales_data_clean.csv', index=False)
