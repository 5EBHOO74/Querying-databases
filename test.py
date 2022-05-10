# def greeting():
#     greetings = ("Sales and Profit Data")
#     length = len(greetings) * '-'
#     print (length, greetings, length)
#
# greeting()
# import csv
# relative_file_path = 'data/sales.csv'
#
# def file_path():
#     return relative_file_path()
#
# def load_data():
#     relative_file_path = 'data/sales.csv'
#
#     file_path = relative_file_path
#
#     print ("Loading data from sales file")
#     try:
#         with open(file_path) as file:
#             csv_reader = csv.reader(file)
#             headings = next(csv_reader)
#             print(headings)
#     except IOError:
#         print("Cannot read file.")
#
#     print("Appending list of headings and list of records in a tuple called New_tuple")
#     with open(file_path) as file:
#         csv_reader = csv.reader(file)
#         headings = next(csv_reader)
#         head = []
#         head.append(headings)
#         record1 = []
#         for line in csv_reader:
#             record1.append(line)
#             new_tuple = (head, '\n', record1)
#
#
# load_data()

print('Please select an option:\n[1] Process Data\n[2] Query Database\n[3] Visualise Data\n[4] Exit')
