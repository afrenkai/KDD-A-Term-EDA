import zipfile
import os
import pandas as pd

def unzip_and_read_csv(zip_path, extract_to='.'):
    """
    Unzips a zip file and reads all CSV files into pandas DataFrames.

    Parameters:
    zip_path (str): The path to the zip file.
    extract_to (str): The directory to extract files to. Defaults to current directory.

    Returns:
    dict: A dictionary where keys are CSV filenames and values are pandas DataFrames.
    DOCSTRING WRITTEN WITH GENERATIVE AI (GPT 4o Mini)
    """
    csv_data = {}

    # Unzipping the file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    for file_name in os.listdir(extract_to):
        if file_name.endswith('.csv'):
            file_path = os.path.join(extract_to, file_name)
            csv_data[file_name] = pd.read_csv(file_path)

    return csv_data

zip_path = 'archive (5).zip'
extract_to = 'data'
csv_files_data = unzip_and_read_csv(zip_path, extract_to)

for file_name, df in csv_files_data.items():
    print(f"Data from {file_name}:")
    print(df.head())
    print("\n")
