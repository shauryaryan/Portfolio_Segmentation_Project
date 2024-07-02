# from flask import Flask, render_template, request
# import pandas as pd
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         data = pd.read_csv(file)
#         # Process data here
#         return "File uploaded successfully!"
#
# if __name__ == '__main__':
#     app.run(debug=True)
# import sys
# import os
# from flask import Flask, render_template, request, jsonify
# import pandas as pd
#
# # Ensure the project root is in the PYTHONPATH
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#
# from data_ingestion.realtime_feeds import fetch_live_stock_data
# from security_compliance.gdpr_checks import anonymize_data, check_gdpr_compliance
#
# # Explicitly set the template folder path
# template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
# app = Flask(__name__, template_folder=template_dir)
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         data = pd.read_csv(file)
#         # Process data here
#         anonymized_data = anonymize_data(data)
#         check_gdpr_compliance(anonymized_data)
#         return "File uploaded and processed successfully!"
#
# @app.route('/live-data', methods=['GET'])
# def live_data():
#     symbol = request.args.get('symbol', 'AAPL')
#     data = fetch_live_stock_data(symbol)
#     return data.to_html()
#
# @app.route('/api/data', methods=['GET'])
# def get_data():
#     # Mock data for demonstration
#     data = {'message': 'This is a test data response.'}
#     return jsonify(data)
#
# if __name__ == '__main__':
#     app.run(debug=True)

# import sys
# import os
# from flask import Flask, render_template, request, jsonify
# import pandas as pd
#
# # Ensure the project root is in the PYTHONPATH
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#
# from data_ingestion.realtime_feeds import fetch_live_stock_data
# from security_compliance.gdpr_checks import anonymize_data, check_gdpr_compliance
#
# # Explicitly set the template folder path
# template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
# app = Flask(__name__, template_folder=template_dir)
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         data = pd.read_csv(file)
#         # Process data here
#         anonymized_data = anonymize_data(data)
#         check_gdpr_compliance(anonymized_data)
#
#         # Perform analysis (this is just a placeholder; replace with actual analysis)
#         analysis_result = anonymized_data.describe().to_html()
#
#         return render_template('results.html', tables=[analysis_result], titles=['Portfolio Analysis'])
#
# @app.route('/live-data', methods=['GET'])
# def live_data():
#     symbol = request.args.get('symbol', 'AAPL')
#     data = fetch_live_stock_data(symbol)
#     return data.to_html()
#
# @app.route('/api/data', methods=['GET'])
# def get_data():
#     # Mock data for demonstration
#     data = {'message': 'This is a test data response.'}
#     return jsonify(data)
#
# if __name__ == '__main__':
#     app.run(debug=True)

import sys
import os
import logging
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pandas as pd
import requests
from urllib.parse import urlencode

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Ensure the project root is in the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_ingestion.realtime_feeds import fetch_live_stock_data
from security_compliance.gdpr_checks import anonymize_data, check_gdpr_compliance

# Explicitly set the template folder path
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

# Fetch secret key from environment variable
# secret_key = os.environ.get('Jc95Z2hHdUkN3ndcgD7GxWatG6C40ZXe')
# if secret_key is None:
#     logging.error("FLASK_SECRET_KEY environment variable is not set.")
# else:
#     logging.debug(f"Using secret key: {secret_key}")
# app.secret_key = secret_key
app.secret_key = 'Jc95Z2hHdUkN3ndcgD7GxWatG6C40ZXe'




# Coinbase OAuth configurations
COINBASE_CLIENT_ID = '380a47509a5b673ea06490de8dd0ff0f5b53a89a729595e417f08ff8bfedfae1'
COINBASE_CLIENT_SECRET = """a5acd0e604bc5cb1e1feff8c3d74f393ef49a954547a7ebecbb52bad14e5f215
"""
COINBASE_REDIRECT_URI = 'http://127.0.0.1:5000/login/coinbase/callback'

# Helper functions for OAuth
def get_coinbase_oauth_token(code):
    try:
        url = 'https://api.coinbase.com/oauth/token'
        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': COINBASE_REDIRECT_URI,
            'client_id': COINBASE_CLIENT_ID,
            'client_secret': COINBASE_CLIENT_SECRET
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.debug("Successfully fetched OAuth token.")
        return response.json().get('access_token')
    except requests.RequestException as e:
        logging.error(f"Error fetching OAuth token: {e}")
        return None

def fetch_coinbase_portfolio(oauth_token):
    try:
        url = 'https://api.coinbase.com/v2/accounts'
        headers = {'Authorization': f'Bearer {oauth_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        accounts = response.json().get('data', [])
        portfolio = pd.DataFrame(accounts)
        logging.debug(f"Successfully fetched portfolio data: {portfolio}")
        return portfolio
    except requests.RequestException as e:
        logging.error(f"Error fetching portfolio data: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    portfolio_data = session.get('portfolio_data')
    analysis_result = session.get('analysis_result')

    logging.debug(f"Rendering portfolio page with data: {portfolio_data} and analysis: {analysis_result}")
    return render_template('portfolio.html', portfolio_data=portfolio_data, analysis_result=analysis_result)

@app.route('/login/coinbase')
def login_coinbase():
    query_params = {
        'response_type': 'code',
        'client_id': COINBASE_CLIENT_ID,
        'redirect_uri': COINBASE_REDIRECT_URI,
        'scope': 'wallet:accounts:read'
    }
    url = f"https://www.coinbase.com/oauth/authorize?{urlencode(query_params)}"
    logging.debug(f"Redirecting to Coinbase OAuth URL: {url}")
    return redirect(url)

@app.route('/login/coinbase/callback')
def coinbase_callback():
    code = request.args.get('code')
    logging.debug(f"Received OAuth callback with code: {code}")
    oauth_token = get_coinbase_oauth_token(code)
    if oauth_token:
        session['coinbase_token'] = oauth_token
        logging.debug("OAuth token stored in session.")

        # Fetch the portfolio and perform analysis
        portfolio_data = fetch_coinbase_portfolio(oauth_token)
        if portfolio_data is not None:
            session['portfolio_data'] = portfolio_data.to_html()
            analysis_result = portfolio_data.describe().to_html()
            session['analysis_result'] = analysis_result
            logging.debug("Portfolio data and analysis result stored in session.")
        else:
            logging.error("Failed to fetch portfolio data.")
    else:
        logging.error("Failed to obtain OAuth token.")

    return redirect(url_for('portfolio'))

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        data = pd.read_csv(file)
        # Process data here
        anonymized_data = anonymize_data(data)
        check_gdpr_compliance(anonymized_data)

        # Perform analysis (this is just a placeholder; replace with actual analysis)
        analysis_result = anonymized_data.describe().to_html()
        return render_template('results.html', tables=[analysis_result], titles=['Portfolio Analysis'])

@app.route('/live-data', methods=['GET'])
def live_data():
    symbol = request.args.get('symbol', 'AAPL')
    data = fetch_live_stock_data(symbol)
    return data.to_html()

@app.route('/api/data', methods=['GET'])
def get_data():
    # Mock data for demonstration
    data = {'message': 'This is a test data response.'}
    return jsonify(data)

if __name__ == '__main__':
    logging.debug("Starting Flask application...")
    app.run(debug=True)

