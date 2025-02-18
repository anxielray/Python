import csv

def count_columns_and_rows(file_path):

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Get the number of columns from the first row (header)
        headers = next(csv_reader)
        num_columns = len(headers)
        
        # Initialize row count
        num_rows = 0
        
        # Count the number of rows
        for _ in csv_reader:
            num_rows += 1

    return num_columns, num_rows

if __name__ == "__main__":
    file_path = 'random_users.csv'
    columns, rows = count_columns_and_rows(file_path)
    print(f"Number of columns: {columns}")
    print(f"Number of rows: {rows}")