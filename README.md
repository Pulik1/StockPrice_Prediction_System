# Stock Price Prediction System

This project implements a stock price prediction system using the Random Forest algorithm, integrated with a user-friendly interface built with Streamlit. The system allows users to predict future stock prices based on historical data and visualize results in real time.

## Features

- Predict stock prices using the Random Forest regression algorithm.
- Interactive Streamlit web application for user interaction.
- Visualize historical and predicted stock prices using dynamic plots.
- Flexible data upload: users can input their own datasets.

## Installation

To run the project locally, follow these steps:

### Prerequisites

Ensure you have the following installed:
- Python 3.7+
- pip (Python package manager)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-price-prediction.git
   cd stock-price-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to the provided URL (usually `http://localhost:8501`).

## How It Works

### Data Preprocessing
- The system processes historical stock price data, handling missing values and scaling features as necessary.
- The dataset should include features like `Date`, `Open`, `High`, `Low`, `Close`, and `Volume`.

### Prediction Model
- The Random Forest algorithm is used for regression tasks.
- The model is trained on historical data to predict future stock prices.

### Visualization
- Historical data and predictions are displayed using line charts for easy comparison.
- Users can adjust parameters such as the training-test split ratio and the number of trees in the Random Forest.

