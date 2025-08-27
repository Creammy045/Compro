def main():
    #Open a file named philosophers.txt
    outfile = open('philosopher.txt', 'w')
    
    #Write the names of three philosophers
    #to the file
    outfile.write('John Loke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')
    
    #Close the file.
    outfile.close()

main()