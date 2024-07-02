import pandas as pd

def export_to_csv(data, file_name):
    data.to_csv(file_name, index=False)
