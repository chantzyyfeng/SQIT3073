import pandas as pd
import os

def verify_user(ic_number, password):
    """
    Verify the user's identity by checking if the IC number is 12 digits long
    and if the password matches the last 4 digits of the IC number.
    """
    return len(ic_number) == 12 and ic_number[-4:] == password

def calculate_tax(income, tax_relief):
    """
    Calculate the tax payable based on Malaysian tax rates for the current year.
    This is a simplified example and may not reflect actual Malaysian tax rates.
    """
    taxable_income = income - tax_relief
    if taxable_income <= 5000:
        tax_payable = 0
    elif taxable_income <= 20000:
        tax_payable = taxable_income * 0.05
    elif taxable_income <= 35000:
        tax_payable = 1000 + (taxable_income - 20000) * 0.1
    else:
        tax_payable = 2500 + (taxable_income - 35000) * 0.15
    
    return tax_payable

def save_to_csv(data, filename):
    """
    Save the user's data (IC number, income, tax relief, and tax payable) to a CSV file.
    If the file doesn't exist, create a new file with a header row.
    If the file exists, append the new data to the existing file.
    """
    df = pd.DataFrame([data])
    if not os.path.isfile(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)

def read_from_csv(filename):
    """
    Read data from the CSV file and return a pandas DataFrame containing the data.
    If the file doesn't exist, return None.
    """
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        return None
