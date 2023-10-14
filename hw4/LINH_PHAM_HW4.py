import csv
import time

def chooseOption():
    print('--- --- --- Main Menu --- --- ---')
    option = input('Choose option:\n' \
         '[1] Create new text file\n' \
         '[2] Read text file content\n'
         '[3] Append to text file\n'
         '[4] Search text file\n' \
         '[5] Export to CSV\n' \
         '[6] Exit program\n'
         'option = ')
    return option

option = chooseOption()
while option != '6':
    if option == '1': #Create
        try:
            create_name = input('Please enter a file name: ') #TODO: Implement the Requirement 1 here
            create_file = open(create_name+".txt", 'w')
            create_file.close()
        except:
            print('An error occurred during the CREATE operation!')
    elif option == '2':  # Read
        try:
            read_name = input('Please enter a file name: ') #TODO: Implement the Requirement 2 here
            read_file = open(read_name+".txt", 'r')
            f = read_file.read()
            print(f)
            read_file.close()
        except:
            print('An error occurred during the READ operation!')

    elif option == '3':  # Append
        try:
            write_name = input('Please enter a file name: ')
            write_check = open(write_name+".txt", 'r') #check for file existence
            write_check.close()
            write_data = input('Please enter the text to be added: ')
            with open(write_name + ".txt", 'a') as write_file:
                write_file.write(write_data)
        except:
            print('An error occurred during the APPEND operation!')

    elif option == '4':  # Find
        try:
            find_name = input('Please enter a file name: ') #TODO: Implement the Requirement 4 here
            find_data = input('Please enter the text to be found: ')
            with open(find_name+".txt", 'r') as find_file:
                f = find_file.read()
                if find_data in f:
                    print(f'Index: {f.index(find_data)}')
                else:
                    print('No result')
        except:
            print('An error occurred during the FIND operation!')

    elif option == '5':  # Export
        try:
            export_name = input('Please enter a file name: ')#TODO: Implement the Requirement 5 here
            csv_name = input('Please enter a CSV file name: ')

            with open(export_name+".txt", 'r') as export_file:
                csv_data = export_file.read()
                rows = csv_data.split(' ')
                with open(csv_name+".csv", 'w') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(rows)
        except:
            print('An error occurred during the EXPORT operation!')

    else:
        print('Invalid option!')
    time.sleep(1.5)
    print('Going Back to main menu ',end='')
    for i in range(4):
        print('.', end='')
        time.sleep(.4)
    print()
    option = chooseOption()
