#Get the number of employee records to create.
num_emps = int(input('How many employee records do you want to create? : '))
#Open a file for writing using with statement.
with open('emplyees.txt', 'w') as emp_file:
    #Get each employee's data and write it to the file.
    for count in range(1, num_emps + 1):
        #Get the data for an emplyee.
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        id_num = input('ID number : ')
        dept = input('Department : ')
        #Write the data as a record to the file.
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        #Display a blank line.
        print()
        
print('Employee records written to employees.txt')