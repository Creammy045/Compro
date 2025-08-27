def main():
    #Open a file named philosophers.txt
    infile = open('philosopher.txt', 'r' )
    
    #Read the file's contents.
    file_contents = infile.read()
    
    #Close the file.
    infile.close()
    
    #Print the data that was read into
    #Memory.
    print(file_contents)
    
main()