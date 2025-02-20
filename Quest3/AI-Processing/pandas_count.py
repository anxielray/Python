import pandas as pd

def count_rows_and_columns(csv_file):
    df = pd.read_csv(csv_file)
    num_rows, num_columns = df.shape
    return num_rows, num_columns

# Example usage
csv_file_path = 'your_file.csv'  # Replace with your CSV file path
rows, columns = count_rows_and_columns(csv_file_path)
print(f'Number of rows: {rows}')
print(f'Number of columns: {columns}')

