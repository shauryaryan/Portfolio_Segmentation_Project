import pandas as pd

def anonymize_data(data):
    columns_to_drop = ['name', 'email', 'phone']
    for column in columns_to_drop:
        if column in data.columns:
            data = data.drop(columns=[column])
    return data

def check_gdpr_compliance(data):
    # Ensure data minimization
    required_columns = ['name', 'email', 'phone']
    for column in required_columns:
        if column in data.columns:
            raise ValueError(f"Column {column} should be removed for GDPR compliance")

    # Check for explicit consent flag
    if 'consent' in data.columns:
        assert all(data['consent'] == True)

    print("Data is GDPR compliant.")
    return True

# Example usage
if __name__ == "__main__":
    # Sample data
    sample_data = pd.DataFrame({
        'name': ['John Doe', 'Jane Smith'],
        'email': ['john@example.com', 'jane@example.com'],
        'phone': ['1234567890', '0987654321'],
        'investment': [10000, 15000],
        'consent': [True, True]
    })

    anonymized_data = anonymize_data(sample_data)
    check_gdpr_compliance(anonymized_data)

