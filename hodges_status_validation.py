import os
from csv import reader

good_values = [0, 1]
file_counter = 0
bad_file_list = []

# user provides pagit th to Recommendation folder
# path = input('Please enter directory path: ')

path = 'D:\FTP\SmartlinkPROD\Hodges\INBOUND'
all_good_files = True
for (root, _, files) in os.walk(path):
    # use os.walk read/print directory path and all filenames in said folder
    # skipping subdirectory parameter bc don't need it
    # returns files in a tuple
    for file in files:
        error_parsing = False
        file_counter += 1  # to identify total files scanned
        bad_file = False
        # for every item in the tuple of filenames...
        # aka for every file
        file_path = os.path.join(root, file)
        """use os.path.join to concatenate directory path
        to each filename in the tuple"""
        with open(file_path, 'r') as file_obj:
            # use open to open file at filepath and return as file object (f)
            csv_reader = reader(file_obj)
            # read file contents
            next(csv_reader)  # skip over header since only looking for 0 or 1
            for row in csv_reader:
                try:
                    if int(row[1]) not in good_values:  # cast to int bc read as string from csv
                        bad_file = True
                        all_good_files = False
                except ValueError as e:
                    if error_parsing == False:
                        bad_file = True
                        all_good_files = False
                        print(f"Could not parse second column in {file_path}")
                        print("Reason for error: value is not an integer.")
                        print("-----")
                        error_parsing = True
        if bad_file:
            bad_file_list.append(file)

print('\n')

if all_good_files:
    print('No errors found')
else:
    print('Files with errors found:')
    for file in bad_file_list:
        print(file)

print(f'{file_counter} files scanned')  # print total files scanned

input('Please press enter to close')