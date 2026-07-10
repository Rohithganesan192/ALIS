"""
Dataset Loader for ALIS.

Purpose:
--------
This module is responsible for loading the assembly shop dataset
from the CSV file into a Pandas DataFrame. It also performs
basic validation before making the dataset available to the
rest of the application.
"""

import pandas as pd  # Import the Pandas library for reading CSV files

from config import DATASET_FILE

# Import the dataset file path from the centralized configuration file.
# This avoids hardcoding file paths throughout the project

def load_dataset():

    """
    Loads the assembly shop dataset.

    Returns:
        pandas.DataFrame:
            The loaded dataset.

    Raises:
        FileNotFoundError:
            If the dataset CSV file cannot be found.

        ValueError:
            If the dataset exists but contains no records.
    """

    try:
        dataset=pd.read_csv(DATASET_FILE)

        # Read the CSV file into a Pandas DataFrame.
        # A DataFrame is similar to an Excel table where rows are records
        # and columns are fields.


    except FileNotFoundError as error:

        # Raise a more descriptive error message so debugging becomes easier.

        raise FileExistsError(
            f"Dataset file not found:\n{DATASET_FILE}"
        ) from error
    
    if dataset.empty:
        raise ValueError("The assembly shop dataset is empty.")

        # Check whether the DataFrame contains any records.
        # A CSV with only column headers is considered empty.
    
    return dataset 

    # Return the validated DataFrame to the calling module.

# ------------------------------------------------------------------
# This block executes ONLY when this file is run directly.
#
# Example:
#     python dataset_loader.py
#
# It does NOT execute when another module imports load_dataset().
# This allows us to test this module independently.
# ------------------------------------------------------------------

if __name__ == "__main__":
    
    # Load the dataset

    dataset=load_dataset()

    print("Dataset loaded successfully.\n")

    # Display the number of records (rows)

    print(f"Number of records:{len(dataset)}")

    # Display the number of fields (columns)

    print(f"Number of columns:{len(dataset.columns)}\n")

    # Display the first five records.
    # Useful for verifying that the dataset has been loaded correctly.
    
    print(dataset.head())