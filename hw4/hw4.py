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
        create_name = input('Please enter a file name: ') #TODO: Implement the Requirement 1 here
        create_file = open(create_name, 'w')

    elif option == '2':  # Read
        read_name = input('Please enter a file name: ') #TODO: Implement the Requirement 2 here
        read_file = open(read_name, 'r')
        f = read_file.read()
        print(f)

    elif option == '3':  # Append
        write_name = input('Please enter a file name: ') #TODO: Implement the Requirement 3 here
        write_data = input('Please enter the text to be added: ')
        with open(write_name, 'a') as write_file:
            write_file.write(write_data)

    elif option == '4':  # Find
        find_name = input('Please enter a file name: ') #TODO: Implement the Requirement 4 here
        find_data = input('Please enter the text to be found: ')
        with open(find_name, 'r') as find_file:
            f = find_file.read()
            if find_data in f:
                print(f.index(find_data))
            else:
                print('No result')

    elif option == '5':  # Export
        pass #TODO: Implement the Requirement 5 here
    else:
        print('Invalid option!')
    time.sleep(1.5)
    print('Going Back to main menu ',end='')
    for i in range(4):
        print('.', end='')
        time.sleep(.4)
    print()
    option = chooseOption()
