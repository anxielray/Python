# We will learn about reading, parsing and writing to a .csv file
# Csv files, can have any delimiters
import csv

# We will use the built-in Python csv module for reading and writing
# the csv module makes handling this kind of data

# open the file  using a context manager. The second argument is the action that we will perform in the file
# in the background, our reader will use a  dialect, that defines the expected format, (default, by a comma)
with open('random_users.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    #Step over the titles(i.e email)
    # next(csv_reader)

    # with open('new_random_users.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')
        
    #     for line in csv_reader:
    #             csv_writer.writerow(line)

#   Using the dictionary readers and the dictionary writers
# with open('new_random_users.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter='\t')

    #Step over the titles(i.e email)
    # next(csv_reader)

    # with open('new_random_users.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')
        
    # for line in csv_reader:
        # print(line['email'])

# Writing to a csv file using a dictionary writer
    with open('new_random_users.csv', 'w') as new_csv_file:
        fieldnames=['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email'] # the modifications only remove the email values, but retain the keys
            csv_writer.writerow(line)
        
with open('new_random_users.csv', 'r') as new_csv_file:
    # print(new_csv_file.read())
    csv_reader = csv.DictReader(new_csv_file, delimiter='\t')
    for line in csv_reader:
        print(line)
