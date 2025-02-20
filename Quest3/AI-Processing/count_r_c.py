import csv


def count_rows_and_columns(csv_file):
    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        num_rows = len(rows) - 1  # Subtract 1 for the header row
        num_columns = len(rows[0]) if rows else 0

    return num_rows, num_columns


# Example usage
csv_file_path = "your_file.csv"  # Replace with your CSV file path
rows, columns = count_rows_and_columns(csv_file_path)
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")
