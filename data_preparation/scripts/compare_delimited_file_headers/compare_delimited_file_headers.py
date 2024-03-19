import os
import pandas as pd
import openpyxl


def compare_delimited_file_headers(input_directory, output_directory, correct_header_string,
                                   correct_header_delimiter=',', file_extension='.csv',
                                   files_delimiter=',', files_encoding='utf-8', result_file=None):
    """
    Process delimited text files in a specified directory.

    This function checks whether the header of each file matches the provided correct header and
    generates a .tsv or .xlsx file with the comparison.
    Parameters:
        input_directory (str): Path to the directory containing the delimited text files.
        output_directory (str): Path to the directory where the comparison file will be saved.
        correct_header_string (str): A delimited string of the correct header.
        correct_header_delimiter (str, optional): Delimiter used in the correct header. Default is ','.
        file_extension (str, optional): Extension of the files to be checked. Default is '.csv'.
        files_delimiter (str, optional): Delimiter used in the delimited text files. Default is ','.
        files_encoding (str, optional): Encoding used in the delimited text files. Default is 'utf-8'.
        result_file (str, optional): The format of the result file. Must be '.tsv' or '.xlsx'.
                                     Default is None.
    Returns:
        None. The function saves a .tsv or .xlsx file with the comparison in the specified directory.
    
    Example:
        compare_delimited_file_headers(
            input_directory='/path/to/input/directory',
            output_directory='/path/to/output/directory',
            correct_header_string='COLUMN1,COLUMN2,COLUMN3',
            correct_header_delimiter=',',
            file_extension='.csv',
            files_delimiter=',',
            files_encoding='utf-8',
            result_file='.xlsx'
        )
    """
    # Check if the result_file parameter is valid
    if result_file not in ['.tsv', '.xlsx']:
        raise ValueError("The result_file parameter must be '.tsv' or '.xlsx'.")

    # Initialize a DataFrame for comparison
    comparison_df = pd.DataFrame(columns=["File", "Status", "Missing Columns",
                                          "Columns not present in the correct header"])

    # Iterate over all files in the specified directory
    for file in os.listdir(input_directory):
        # Check if the file is a delimited text file
        if file.endswith(file_extension):
            # Build the full path to the file
            file_path = os.path.join(input_directory, file)

            # Read the .csv file into a DataFrame
            df = pd.read_csv(file_path, delimiter=files_delimiter, encoding=files_encoding)

            # Convert all column names to uppercase
            df.columns = [col.upper() for col in df.columns]

            # Identify missing and excess columns
            correct_header = set(correct_header_string.split(correct_header_delimiter))
            missing_columns = correct_header - set(df.columns)
            excess_columns = set(df.columns) - correct_header

            # Determine the status of the file
            status = "correct" if not missing_columns and not excess_columns else "incorrect"

            # Convert the column sets to lists
            missing_columns_list = list(missing_columns)
            excess_columns_list = list(excess_columns)

            # Add the results to the comparison DataFrame
            comparison_df = pd.concat([comparison_df, pd.DataFrame({
                "File": [file],
                "Status": [status],
                "Missing Columns": [" --- ".join(missing_columns_list)],
                "Columns not present in the correct header": [" --- ".join(excess_columns_list)]
            })], ignore_index=True)

    # Save the comparison DataFrame as a .tsv or .xlsx file
    if result_file == '.tsv':
        comparison_df.to_csv(os.path.join(output_directory, 'header_comparison_result.tsv'), sep='\t', index=False)
    elif result_file == '.xlsx':
        comparison_df.to_excel(os.path.join(output_directory, 'header_comparison_result.xlsx'), index=False)