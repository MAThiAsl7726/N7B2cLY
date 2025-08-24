# 代码生成时间: 2025-08-24 09:08:07
import pandas as pd
from gradio import Interface

"""
Data Cleaning and Preprocessing Tool

This tool provides a simple interface for users to upload a CSV file, 
process it by cleaning and preprocessing data, and then download the cleaned data.
"""

def clean_data(df):
    """
    Clean the data by handling missing values and duplicates.

    Parameters:
    df (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    # Handle missing values by filling them with the mean of the column
    df = df.fillna(df.mean())

    # Drop duplicate rows
    df = df.drop_duplicates()

    return df

# Define the input and output components
input_csv = gr.Interface.input(type="file", label="Upload CSV file")
output_csv = gr.Interface.output(type="file", label="Download Cleaned CSV file")

# Define the function to be executed when the input is received
def process_data(input_file):
    """
    Process the uploaded CSV file by cleaning and preprocessing the data.

    Parameters:
    input_file: The uploaded CSV file.

    Returns:
    pd.DataFrame: The cleaned DataFrame to be downloaded.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_file)

        # Clean the data
        cleaned_df = clean_data(df)

        # Convert the cleaned DataFrame to a CSV file
        cleaned_csv = cleaned_df.to_csv(index=False)

        return cleaned_csv
    except Exception as e:
        # Handle any errors that occur during processing
        print(f"Error processing file: {e}")
        return None

# Create the Gradio interface
iface = Interface(
    fn=process_data,
    inputs=input_csv,
    outputs=output_csv,
    title="Data Cleaning and Preprocessing Tool",
    description="Upload a CSV file to clean and preprocess the data."
)

# Launch the interface
iface.launch()