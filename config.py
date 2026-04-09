# Complete Configuration for NeuralProphet and LSTM

# Project Paths
DATA_PATH = './data/'
MODEL_SAVE_PATH = './models/'
VISUALIZATION_PATH = './visualizations/'

# Stock Symbols
STOCK_SYMBOLS = ['AAPL', 'GOOGL', 'MSFT']

# Model Hyperparameters
NEURALPROPHE_HYPERPARAMS = {
    'n_changepoints': 10,
    'changepoint_range': 0.9,
    'seasonality_mode': 'additive',
    'epochs': 100,
    'batch_size': 64,
    'learning_rate': 1.0,
}

LSTM_HYPERPARAMS = {
    'sequence_length': 30,
    'hidden_units': 50,
    'dropout_rate': 0.2,
    'epochs': 100,
    'batch_size': 64,
}

# Technical Indicators
TECHNICAL_INDICATORS = {
    'SMA': [30, 60],
    'EMA': [12, 26],
    'RSI': [14],
    'MACD': True,
}

# Visualization Settings
VISUALIZATION_SETTINGS = {
    'plot_size': (10, 6),
    'show_grid': True,
    'marker_style': 'o',
}

# Data Processing Options
DATA_PROCESSING_OPTIONS = {
    'scaling_method': 'minmax',
    'train_test_split': 0.8,
    'time_series': True,
}