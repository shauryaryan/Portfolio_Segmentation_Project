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

### Prerequisites

- Python 3.6 or higher
- Git

### Installation Steps

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
    Navigate to `http://127.0.0.1:5000/` to access the application.
   
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



