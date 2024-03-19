import pandas as pd
import os
from unidecode import unidecode
import chardet
import sqlite3


def remove_special_characters(input_directory, output_directory, original_delimiter=None):
    """
    Remove special characters and accents from the column values of all CSV and TSV files in a directory,
    and save the data back into TSV files.

    Parameters:
        input_directory (str): Path to the directory with the CSV and TSV files.
        output_directory (str): Path to the directory where the TSV files will be saved.
        original_delimiter (str, optional): Original delimiter used in the files. If None, the delimiter will be inferred.

    Returns:
        None
    """
    # Iterate over the files in the input directory
    for file in os.listdir(input_directory):
        # Process only CSV and TSV files
        if file.endswith('.csv') or file.endswith('.tsv'):
            
            # Get the full path of the file
            file_path = os.path.join(input_directory, file)
            
            # Detect the file encoding
            with open(file_path, 'rb') as f:
                result = chardet.detect(f.read(10000))  # Read only the first 10000 bytes
            encoding = result['encoding']
            
            # If original_delimiter is not provided, try to infer the delimiter
            if original_delimiter is None:
                with open(file_path, 'r', encoding=encoding) as f:
                    first_line = f.readline()
                if '\t' in first_line:
                    delimiter = '\t'
                elif ',' in first_line:
                    delimiter = ','
                elif ';' in first_line:
                    delimiter = ';'
                else:
                    raise ValueError("Delimiter not recognized. Please provide the original delimiter.")
            else:
                delimiter = original_delimiter
            
            # Define the name of the output file
            tsv_file_name = os.path.join(output_directory, file.rsplit('.', 1)[0] + '.tsv')
            
            # Process the file in chunks
            chunksize = 10 ** 6  # Adjust this value depending on your available memory
            for chunk in pd.read_csv(file_path, delimiter=delimiter, encoding=encoding, chunksize=chunksize):
                # Remove accents from each string value in the chunk
                chunk = chunk.apply(lambda x: x.map(lambda y: unidecode(y) if isinstance(y, str) else y))
                
                # Remove non-UTF-8 characters
                chunk = chunk.apply(lambda x: x.map(lambda y: y.encode('utf-8', 'ignore').decode('utf-8') if isinstance(y, str) else y))
                
                # Save the chunk to the output file
                chunk.to_csv(tsv_file_name, sep='\t', index=False, encoding='utf-8', mode='a')


# Usage of the function:
"""
remove_special_characters(input_directory='data_preparation\\datasets_tratados\\educandos\\tratados_google_sheets', 
output_directory='data_preparation\\datasets_tratados\\educandos\\tratados_unidecode', original_delimiter=';')

"""


def load_tsv_to_sqlite(tsv_dir, db_name, table_name, primary_key=None):
    """
    Load TSV files into an SQLite table.

    Args:
        tsv_dir (str): Directory containing the TSV files.
        db_name (str): Name of the SQLite database file.
        table_name (str): Name of the table where the data will be loaded.
        primary_key (str, optional): Name of the primary key column. If not provided, an artificial primary key called 'PK_EDUCANDOS' will be created.

    Returns:
        None
    """
    # Check if the table already exists in the database
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    table_exists = cur.fetchone()

    # Clear the table before loading the files
    if not table_exists:
        cur.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Get all files in the specified directory
    files = os.listdir(tsv_dir)

    # Filter the list of files to include only TSV files
    tsv_files = [file for file in files if file.endswith('.tsv')]

    # Iterate over each TSV file
    for tsv_file in tsv_files:
        # Read the TSV file into a DataFrame
        df = pd.read_csv(os.path.join(tsv_dir, tsv_file), sep='\t', encoding='utf-8')

        # Create the artificial key 'SK_CODESC_ANO'
        df['SK_CODESC_ANO'] = df['CODESC'].astype(str) + tsv_file[-8:-4]

        # If no primary_key was provided, create an artificial one
        if primary_key == 'PK_EDUCANDOS' and primary_key not in df.columns:
            df.insert(0, 'PK_EDUCANDOS', range(1, len(df) + 1))

        # Write the DataFrame to the SQLite database
        df.to_sql(table_name, conn, if_exists='append', index=False)

    # Close the connection to the SQLite database
    conn.close()

# Usage of the function:
# load_tsv_to_sqlite('data_preparation\\datasets_tratados\\educandos\\tratados_unidecode', 'escolas_educandos_sqlite.db', 'educandos')


def create_escolas_educandos_table():
    """
    This function creates a new table named 'escolas_educandos' in a SQLite database.
    The new table is based on two existing tables: 'escolas' and 'educandos'.
    The function keeps only one column for each name, except for the columns called DATABASE, which are differentiated by aliases.
    The common key between the tables is SK_CODESC_ANO.

    Returns:
    None
    """

    # Connect to the SQLite database 'escolas_educandos_sqlite.db'
    conn = sqlite3.connect('escolas_educandos_sqlite.db')

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Get the column names of the 'escolas' table
    cur.execute("PRAGMA table_info(escolas)")
    columns_escolas = [column[1] for column in cur.fetchall()]

    # Get the column names of the 'educandos' table
    cur.execute("PRAGMA table_info(educandos)")
    columns_educandos = [column[1] for column in cur.fetchall()]

    # Find the common columns between the 'escolas' and 'educandos' tables, except 'DATABASE'
    common_columns = list(set(columns_escolas) & set(columns_educandos))
    if 'DATABASE' in common_columns: common_columns.remove('DATABASE')

    # Create the column list for the SQL query
    columns_sql = []

    # Add the columns of the 'escolas' table to the list, differentiate 'DATABASE' column
    for column in columns_escolas:
        if column == 'DATABASE':
            columns_sql.append(f"esc.{column} AS DATABASE_ESCOLAS")
        else:
            columns_sql.append(f"esc.{column}")

    # Add the columns of the 'educandos' table that are not in the `common_columns` list to the list, differentiate 'DATABASE' column
    for column in columns_educandos:
        if column not in common_columns:
            if column == 'DATABASE':
                columns_sql.append(f"educ.{column} AS DATABASE_EDUCANDOS")
            else:
                columns_sql.append(f"educ.{column}")

    # SQL command to create a new table 'escolas_educandos' based on the 'escolas' and 'educandos' tables
    sql_command = f"""
    CREATE TABLE escolas_educandos AS
    SELECT 
        {', '.join(columns_sql)}
    FROM escolas esc
    JOIN educandos educ
    ON esc.SK_CODESC_ANO = educ.SK_CODESC_ANO;
    """

    # Execute the SQL command
    cur.execute(sql_command)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Usage of the function:
# create_escolas_educandos_table()