import pandas as pd

def integrate_user_data(file_path):
    user_data = pd.read_csv(file_path)
    return user_data
