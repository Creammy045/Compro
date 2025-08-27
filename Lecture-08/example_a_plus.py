def example_w_plus_mode():
    #Open the file for reading and writing (truncsting it)
    with open('example_a+.txt', 'a+') as file: 
        #Move the file pointer back to the beginning to read the content
        file.seek(0)
        
        #Read the current content of the file
        content = file.read()
        print('Current Content of the file:')
        print(content)
        
        #Append new content to the file
        file.write('Appending a new line at the end.\n')
        
        #Move the file pointer back to the beginning again to read the updated content
        file.seek(0)
        updated_content = file.read()
        print('\nUpdated content of the file:')
        print(updated_content)
        
example_w_plus_mode()