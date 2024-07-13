import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_clean_data(file_path):
    """Load cleaned data for analysis."""
    data = pd.read_csv(file_path)
    return data

def generate_summary_statistics(data):
    """Generate summary statistics for the dataset."""
    summary = data.describe()
    return summary

def plot_histograms(data):
    """Plot histograms for the dataset."""
    data.hist(figsize=(10, 8), bins=30)
    plt.tight_layout()
    plt.savefig('../reports/histograms.png')

def plot_correlation_matrix(data):
    """Plot correlation matrix for the dataset."""
    correlation_matrix = data.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.savefig('../reports/correlation_matrix.png')

if __name__ == "__main__":
    file_path = '../data/processed/sales_data_clean.csv'
    data = load_clean_data(file_path)
    
    summary_stats = generate_summary_statistics(data)
    print(summary_stats)
    
    plot_histograms(data)
    plot_correlation_matrix(data)
