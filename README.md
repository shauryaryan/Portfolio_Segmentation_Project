Portfolio Segmentation Project
I created this project which is a web application that performs portfolio segmentation and analysis. It allows users to upload their portfolio data, connect their Coinbase account to fetch live portfolio data, and perform various analyses on the data. The application is built using Flask for the backend and integrates with the Coinbase API for portfolio data retrieval.

Features
- Upload portfolio CSV files for analysis
- Connect to Coinbase to fetch live portfolio data
- Perform portfolio segmentation and exploratory analysis
- Display results and analysis in a user-friendly format

Technologies Used
- Python
- Flask
- Pandas
- Requests
- HTML/CSS
- Coinbase API

Setup and Installation
Prereqs
- Python 3.6 or higher
- Git

Installation Steps

1. Clone the repository**:
    git clone https://github.com/shauryaryan/Portfolio_Segmentation_Project.git

2. Create a virtual environment**:
    python3 -m venv .venv
    source .venv/bin/activate
    On Windows:
    .venv\Scripts\activate

4. Install the required packages**:
    pip install -r requirements.txt

5. Set up the Flask secret key:

    Open user_interface/web_app.py and ensure the secret key is set:
    app.secret_key = ''

6. Run the application**:
    python user_interface/web_app.py
 

7. Open the application in your browser**:
    Navigate to localhost server to access the application.
   
Testing 
Uploading a Portfolio CSV File
1. Navigate to the home page.
2. Click on the "Upload" button to upload your portfolio CSV file.
3. The application will process the file and display the analysis results.

Connecting to Coinbase

1. Navigate to the "Portfolio" page.
2. Click on the "Connect to Coinbase" button.
3. Log in to your Coinbase account and authorize the application.
4. The application will fetch your portfolio data from Coinbase and display the analysis results.


Analysis Performed

Data Anonymization
To ensure user privacy, personal data such as names, email addresses, and phone numbers are anonymized before performing any analysis. This is in compliance with GDPR guidelines.

AI and Data Analysis Techniques

Descriptive Statistics
- Summary Statistics: Provides an overview of the central tendency, dispersion, and shape of the dataset’s distribution, excluding NaN values. This includes mean, median, standard deviation, minimum, and maximum values.

Segmentation Analysis
- Asset Allocation: Segments the portfolio into different asset classes (e.g., cryptocurrencies, stocks) and provides insights into the distribution of investments. This helps in understanding the diversification of the portfolio.
- Clustering: Uses clustering algorithms (e.g., K-means) to group similar assets based on their characteristics such as risk, return, and volatility. This helps in identifying patterns and making informed decisions about asset allocation.

Performance Metrics
- Return on Investment (ROI): Calculates the ROI for individual assets and the overall portfolio to assess the profitability. This metric helps in understanding the gains or losses from the investments.
  
- Volatility and Standard Deviation**: Measures the volatility of assets to understand the risk and return dynamics. Volatility is a statistical measure of the dispersion of returns for a given security or market index.
- Sharpe Ratio: Calculates the Sharpe ratio to evaluate the risk-adjusted return of the portfolio. The Sharpe ratio is the average return earned in excess of the risk-free rate per unit of volatility or total risk.
  
Predictive Analysis
Time Series Analysis: Uses time series analysis techniques to predict future prices and trends based on historical data. This includes techniques like ARIMA (AutoRegressive Integrated Moving Average) for forecasting asset prices.

